from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from io_school.utils import create_slug, make_display_price
from django.db.models import Count
from videos.models import Video

POS_CHOICES = (
    ('main', 'Main'),
    ('sec', 'Secondary'),
)


class CategoriesQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CategoriesManager(models.Manager):
    def get_queryset(self):
        return CategoriesQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active().annotate(courses_length=Count('primary_category') + Count("secondary_category")).prefetch_related('primary_category')


class Categories(models.Model):
    title = models.CharField(unique=True, max_length=120, blank=False, null=False)
    video = models.ForeignKey(Video, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(unique=True, max_length=255, blank=False, null=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_categories', kwargs={"slug": self.slug})


def pre_save_categories_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_categories_receiver, sender=Categories)


