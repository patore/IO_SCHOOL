from django.contrib import admin
from .models import Course, Lecture, MyCourses
from .forms import LectureAdminForm


class LectureInline(admin.TabularInline):
    model = Lecture
    form = LectureAdminForm
    prepopulated_fields = {'slug': ('title', )}
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    inlines = [LectureInline]
    list_filter = ['title', 'timestamp']
    list_display = ['title', 'timestamp', 'updated']
    readonly_fields = ['timestamp', 'updated']
    search_fields = ['title']

    class Meta:
        model = Course

admin.site.register(Course, CourseAdmin)
admin.site.register(MyCourses)



