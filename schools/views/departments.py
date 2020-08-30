from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from dashboard.views import DashboardView

from ..models import Course, Department, Lab

# Create your views here.

class DepartmentCreateView(DashboardView, CreateView):
    model = Department
    fields = ('name','school')
    template_name = 'dashboard/schools/departments/add.html'

    def get_success_url(self):
        return reverse_lazy('schools:department_details', kwargs={'pk': self.object.pk})


class DepartmentListView(DashboardView, ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'dashboard/schools/departments/list.html'


class DepartmentDetailView(DashboardView, DetailView):
    model = Department
    template_name = 'dashboard/schools/departments/details.html'

    def get_context_data(self, **kwargs):
        department = self.object.id
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(department=department)
        context["department"] = Department.objects.filter(id=department).first()
        # context["department"] = Department.objects.filter(id=department).annotate(courses_in_department_count=Count('course')).first()
        return context



class DepartmentUpdateView(DashboardView, UpdateView):
    model = Department
    template_name = 'schools/departments/edit.html'
    fields = ('name','school')

    def get_success_url(self):
        return reverse_lazy('schools:department_details', kwargs={'pk': self.object.pk})
