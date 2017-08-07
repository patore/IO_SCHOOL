from django import forms
from .models import Categories
from videos.models import Video


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = [
            'title',
            'slug',
            'description'
        ]


class CategoriesAdminForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = [
            'title',
            'slug',
            'video',
            'description'
        ]

    def __init__(self, *args, **kwargs):
        super(CategoriesAdminForm, self).__init__(*args, **kwargs)
        obj = kwargs.get('instance')
        qs = Video.objects.all().unused()
        if obj:
            if obj.video:
                this_ = Video.objects.filter(pk=obj.video.pk)
                qs = (qs | this_)
            self.fields['video'].queryset = qs
        else:
            self.fields['video'].queryset = qs
