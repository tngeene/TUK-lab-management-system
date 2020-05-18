from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from dashboard.views import DashboardView
from django.urls import reverse_lazy
from ..models import School, Lab, Course
from django.db.models import Count

# Create your views here.

class SchoolCreateView(DashboardView, CreateView):
    model = School
    fields = ('name','department')
    template_name = 'schools/Schools/add.html'

    def get_success_url(self):
        return reverse_lazy('schools:school_details', kwargs={'pk': self.object.pk})


class SchoolListView(DashboardView, ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'schools/schools/list.html'


class SchoolDetailView(DashboardView, DetailView):
    model = School
    template_name = 'schools/schools/details.html'

    def get_context_data(self, **kwargs):
        lab = self.object.id
        course = self.object.id
        context = super().get_context_data(**kwargs)
        context["labs"] = Lab.objects.filter(school=lab)
        context["courses"] = Course.objects.filter(school=course)
        context["school"] = School.objects.annotate(labs_in_school_count=Count('lab')).annotate(
            courses_in_school_count=Count('course')).first()
        return context


class SchoolUpdateView(DashboardView, UpdateView):
    model = School
    template_name = 'schools/Schools/edit.html'
    fields = ('name','department')

    def get_success_url(self):
        return reverse_lazy('schools:school_details', kwargs={'pk': self.object.pk})