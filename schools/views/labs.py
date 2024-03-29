from django.contrib import messages
from django.db.models import Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)
from django.contrib.auth import get_user_model
from dashboard.views.dashboard import DashboardView

from ..models import Lab, School

User = get_user_model()
# Create your views here.

class LabCreateView(DashboardView, CreateView):
    model = Lab
    fields = ('name', 'room', 'school')
    template_name = 'dashboard/schools/labs/add.html'

    def get_success_url(self):
        messages.success(self.request,"Lab Added Successfully")
        return reverse_lazy('schools:lab_details', kwargs={'pk': self.object.pk})


class LabListView(DashboardView, ListView):
    model = Lab
    context_object_name = 'labs'
    template_name = 'dashboard/schools/labs/list.html'


class LabDetailView(DashboardView, DetailView):
    model = Lab
    context_object_name = 'lab'
    template_name = 'dashboard/schools/labs/details.html'

    def get_context_data(self, **kwargs):
        lab = self.object.id
        context = super().get_context_data(**kwargs)
        context["schools"] = School.objects.filter(labs=lab)
        context["users"] = User.objects.filter(lab=lab)
        return context


class LabUpdateView(DashboardView, UpdateView):
    model = Lab
    template_name = 'dashboard/schools/labs/edit.html'
    fields = ('name', 'room', 'school')

    def get_success_url(self):
        messages.success(self.request,"Lab Details Updated")
        return reverse_lazy('schools:lab_details', kwargs={'pk': self.object.pk})

class SchoolAssignView(DashboardView, ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'dashboard/schools/labs/assign_school.html'

    def get_queryset(self):
        return School.objects.exclude(labs=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lab"] = Lab.objects.get(id=self.kwargs['pk'])
        return context

def school_assign_view(request, pk, school_pk):
    lab = Lab.objects.get(id=pk)
    school = School.objects.get(id=school_pk)
    lab.school.add(school)
    lab.save()
    messages.success(request,f"School assigned to {lab.name} lab")
    return redirect('schools:lab_details', pk=pk)

def school_unassign_view(request, pk, school_pk):
    lab = Lab.objects.get(id=pk)
    school = School.objects.get(id=school_pk)
    lab.school.remove(school)
    lab.save()

    messages.success(request,f"School removed from {lab.name} lab")
    return redirect('schools:lab_details', pk=pk)
