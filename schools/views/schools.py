from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from dashboard.views.dashboard import DashboardView
from django.urls import reverse_lazy
from ..models import School, Lab, Course, Department
from django.db.models import Count

# Create your views here.

class SchoolCreateView(DashboardView, CreateView):
    model = School
    fields = ('name',)
    template_name = 'dashboard/schools/schools/add.html'

    def get_success_url(self):
        messages.success(self.request,"School added successfully")
        return reverse_lazy('schools:school_details', kwargs={'pk': self.object.pk})


class SchoolListView(DashboardView, ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'dashboard/schools/schools/list.html'


class SchoolDetailView(DashboardView, DetailView):
    model = School
    template_name = 'dashboard/schools/schools/details.html'

    def get_context_data(self, **kwargs):
        school = self.object.id
        context = super().get_context_data(**kwargs)
        context["labs"] = Lab.objects.filter(school=school)
        context["courses"] = Course.objects.filter(department__school=school)
        context["departments"] = Department.objects.filter(school=school)
        context["school"] = School.objects.filter(id=school).annotate(labs_in_school_count=Count('lab')).first()
        return context


class SchoolUpdateView(DashboardView, UpdateView):
    model = School
    template_name = 'dashboard/schools/Schools/edit.html'
    fields = ('name',)

    def get_success_url(self):
        messages.success(self.request,"School updated")
        return reverse_lazy('schools:school_details', kwargs={'pk': self.object.pk})