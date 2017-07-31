from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_filter = ['title', 'timestamp']
    list_display = ['title', 'timestamp', 'updated']
    readonly_fields = ['timestamp', 'updated']
    search_fields = ['title']

    class Meta:
        model = Video

admin.site.register(Video, VideoAdmin)