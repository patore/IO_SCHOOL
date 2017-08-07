from django import forms
from django.db.models import Q
from .models import Course, Lecture
from videos.models import Video


class LectureAdminForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [
            'title',
            'slug',
            'order',
            'video',
            'description'
        ]

    def __init__(self, *args, **kwargs):
        super(LectureAdminForm, self).__init__(*args, **kwargs)
        obj = kwargs.get('instance')
        qs = Video.objects.all().unused()
        if obj:
            if obj.video:
                this_ = Video.objects.filter(pk=obj.video.pk)
                qs = (qs | this_)
            self.fields['video'].queryset = qs
        else:
            self.fields['video'].queryset = qs


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title',
            'order',
            'category',
            'secondary',
            'description',
            'price'
        ]


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [
            'course',
            'order',
            'video',
            'title',
            'description'
        ]
