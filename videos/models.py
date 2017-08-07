from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from io_school.utils import create_slug
from django.db.models import Count


class VideoQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def unused(self):
        return self.filter(Q(lecture__isnull=True)&Q(categories__isnull=True))


class VideoManager(models.Manager):
    def get_queryset(self):
        return VideoQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()


class Video(models.Model):
    title = models.CharField(unique=True, max_length=120, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    free = models.BooleanField(default=True)
    member_required = models.BooleanField(default=False)
    embed_code = models.TextField(null=False, blank=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = VideoManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_video', kwargs={"slug": self.slug})


def pre_save_video_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_video_receiver, sender=Video)
