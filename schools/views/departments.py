from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from dashboard.views import DashboardView
from django.urls import reverse_lazy
from ..models import Department, School, Lab
from django.db.models import Count

# Create your views here.

class DepartmentCreateView(DashboardView, CreateView):
    model = Department
    fields = ('name',)
    template_name = 'schools/departments/add.html'

    def get_success_url(self):
        return reverse_lazy('schools:department_details', kwargs={'pk': self.object.pk})


class DepartmentListView(DashboardView, ListView):
    model = Department
    context_object_name = 'departments'
    template_name = 'schools/departments/list.html'


class DepartmentDetailView(DashboardView, DetailView):
    model = Department
    template_name = 'schools/departments/details.html'

    def get_context_data(self, **kwargs):
        department = self.object.id
        context = super().get_context_data(**kwargs)
        context["schools"] = School.objects.filter(department=department)
        context["department"] = Department.objects.filter(id=department).annotate(schools_in_department_count=Count('school')).first()
        return context
    


class DepartmentUpdateView(DashboardView, UpdateView):
    model = Department
    template_name = 'schools/departments/edit.html'
    fields = ('name',)

    def get_success_url(self):
        return reverse_lazy('schools:department_details', kwargs={'pk': self.object.pk})