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
from .models import Categories
from .forms import CategoriesForm
from io_school.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class CategoriesCreateView(StaffMemberRequiredMixin, CreateView):
    model = Categories
    form_class = CategoriesForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CategoriesCreateView, self).form_valid(form)


class CategoriesDetailView(DetailView):

    def get_object(self):
        slug = self.kwargs.get("slug")
        qs = Categories.objects.filter(slug=slug)
        if qs.exists():
            return qs.first()
        raise Http404


class CategoriesListView(ListView):
    template_name = 'categories_list.html'

    def get_queryset(self):
        request = self.request
        qs = Categories.objects.all()
        query = request.GET.get('q')

        if query:
            qs = qs.filter(title__icontains=query)
        return qs.order_by('title')

    # def get_context_data(self, *args, **kwargs):
    #     context = super(CategoriesListView, self).get_context_data(*args, **kwargs)
    #     context['team'] = 456
    #     return context


class CategoriesUpdateView(UpdateView):
    queryset = Categories.objects.all()
    form_class = CategoriesForm


class CategoriesDeleteView(DeleteView):
    model = Categories
    success_url = '/categories'

