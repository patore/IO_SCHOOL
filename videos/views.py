from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Video
from .forms import VideoForm
from io_school.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()


class VideoListView(ListView):
    template_name = 'video_list.html'

    def get_queryset(self):
        request = self.request
        qs = Video.objects.all()
        query = request.GET.get('q')

        if query:
            return qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(VideoListView, self).get_context_data(*args, **kwargs)
        context['team'] = 456
        return context


class VideoUpdateView(UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(DeleteView):
    model = Video
    success_url = '/videos'