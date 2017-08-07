from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.shortcuts import render, Http404, redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    RedirectView
)
from .models import Course, Lecture, MyCourses
from .forms import CourseForm, LectureForm
from io_school.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class CourseCreateView(StaffMemberRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CourseCreateView, self).form_valid(form)


class CourseDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get("slug")
        qs = Course.objects.filter(slug=slug).owned(self.request.user)
        if qs.exists():
            return qs.first()
        raise Http404


class CoursePurchaseView(LoginRequiredMixin, RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, slug=None):

        qs = Course.objects.filter(slug=slug).owned(self.request.user)
        if qs.exists():
            user = self.request.user
            if user.is_authenticated():
                my_courses = user.mycourses
                # run transaction
                # if transaction successful:
                my_courses.courses.add(qs.first())
                return qs.first().get_absolute_url()
        raise "/courses/"


class CourseListView(ListView):
    template_name = 'course_list.html'

    def get_queryset(self):
        request = self.request
        qs = Course.objects.all()
        query = request.GET.get('q')
        user = self.request.user

        if query:
            qs = qs.filter(title__icontains=query)

        if user.is_authenticated():
            qs = qs.owned(user)
        return qs

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CourseListView, self).get_context_data(*args, **kwargs)
    #     context['team'] = 456
    #     return context


class CourseUpdateView(UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm


class CourseDeleteView(DeleteView):
    model = Course
    success_url = '/courses'


class LectureCreateView(StaffMemberRequiredMixin, CreateView):
    model = Lecture
    form_class = LectureForm
    template_name = 'lectures/lecture_form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(LectureCreateView, self).form_valid(form)


class LectureDetailView(DetailView):
    queryset = Lecture.objects.all()
    template_name = 'lectures/lecture_detail.html'


class LectureListView(ListView):
    template_name = 'lectures/lecture_list.html'

    def get_queryset(self):
        request = self.request
        qs = Lecture.objects.all()
        query = request.GET.get('q')

        if query:
            return qs.filter(title__icontains=query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(LectureListView, self).get_context_data(*args, **kwargs)
        context['team'] = 456
        return context


class LectureUpdateView(UpdateView):
    template_name = 'lectures/lecture_update.html'
    queryset = Lecture.objects.all()
    form_class = LectureForm


class LectureDeleteView(DeleteView):
    model = Lecture
    success_url = '/lectures'