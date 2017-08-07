from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.text import slugify


def create_slug(instance):
    slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).order_by('-id')
    if qs.exists():
        return slug + "-1"
    return slug


def make_display_price(price):
    dollars = round(price, 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])