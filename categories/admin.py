from django.contrib import admin
from .models import Categories
from .forms import CategoriesAdminForm


class CategoriesAdmin(admin.ModelAdmin):
    list_filter = ['title', 'timestamp']
    list_display = ['title', 'timestamp', 'updated']
    readonly_fields = ['timestamp', 'updated']
    search_fields = ['title']
    form = CategoriesAdminForm

    #class Meta:
     #   model = Categories

admin.site.register(Categories, CategoriesAdmin)
