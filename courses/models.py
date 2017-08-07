from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from io_school.utils import create_slug, make_display_price
from videos.models import Video
from .fields import PositionField
from django.db.models import Prefetch
from categories.models import Categories


POS_CHOICES = (
    ('main', 'Main'),
    ('sec', 'Secondary'),
)


class CourseQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def owned(self, user):
        return self.prefetch_related(
            Prefetch('owned',
                     queryset=MyCourses.objects.filter(user=user),
                     to_attr='is_owner'
                     )
        )


class CourseManager(models.Manager):
    def get_queryset(self):
        return CourseQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()


class MyCourses(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    courses = models.ManyToManyField('Course', related_name='owned', blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.courses.all().count())

    class Meta:
        verbose_name = 'My Courses'
        verbose_name_plural = 'My Courses'


def post_save_user_create(sender, instance, created, *args, **kwargs):
    if created:
        MyCourses.objects.get_or_create(user=instance)

post_save.connect(post_save_user_create, sender=settings.AUTH_USER_MODEL)


def handle_upload(instance, filename):
    if instance.slug:
        return "%s/images/%s" %(instance.slug, filename)
    return "unknown/images/%s" %(filename)


class Course(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(unique=True, max_length=120, blank=False, null=False)
    category = models.ForeignKey(Categories, related_name='primary_category', blank=True, null=True)
    secondary = models.ManyToManyField(Categories, related_name='secondary_category', blank=True)
    order = PositionField(collection='category')
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload,
                              height_field='image_height',
                              width_field='image_width',
                              blank=True,
                              null=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(unique=True, max_length=255, blank=False, null=False)
    active = models.BooleanField(default=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=False, null=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CourseManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']

    def get_absolute_url(self):
        return reverse('detail_course', kwargs={"slug": self.slug})

    def get_purchase_url(self):
        return reverse('purchase_course', kwargs={"slug": self.slug})

    def display_price(self):
        return make_display_price(self.price)


def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_course_receiver, sender=Course)


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, limit_choices_to={'lecture__isnull':True}, on_delete=models.SET_NULL, null=True)
    order = PositionField(collection='course')
    title = models.CharField(unique=True, max_length=120, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(unique=True, max_length=255, blank=False, null=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']

    def get_absolute_url(self):
        return reverse('detail_lecture', kwargs={"slug": self.slug})


def pre_save_lecture_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_lecture_receiver, sender=Lecture)