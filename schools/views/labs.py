from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from dashboard.views import DashboardView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from ..models import School, Lab
from django.db.models import Count

# Create your views here.

class LabCreateView(DashboardView, CreateView):
    model = Lab
    fields = ('name','school')
    template_name = 'schools/labs/add.html'

    def get_success_url(self):
        return reverse_lazy('schools:lab_details', kwargs={'pk': self.object.pk})


class LabListView(DashboardView, ListView):
    model = Lab
    context_object_name = 'labs'
    template_name = 'schools/labs/list.html'


class LabDetailView(DashboardView, DetailView):
    model = Lab
    context_object_name = 'lab'
    template_name = 'schools/labs/details.html'

    def get_context_data(self, **kwargs):
        lab = self.object.id
        context = super().get_context_data(**kwargs)
        context["schools"] = School.objects.filter(lab=lab)
        return context


class LabUpdateView(DashboardView, UpdateView):
    model = Lab
    template_name = 'schools/labs/edit.html'
    fields = ('name','school')

    def get_success_url(self):
        return reverse_lazy('schools:lab_details', kwargs={'pk': self.object.pk})

class SchoolAssignView(DashboardView, ListView):
    model = School
    context_object_name = 'schools'
    template_name = 'schools/labs/assign_school.html'

    def get_queryset(self):
        return School.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lab"] = Lab.objects.get(id=self.kwargs['pk'])
        return context

def school_assign_view(request, pk, school_pk):
    lab = Lab.objects.get(id=pk)
    school = School.objects.get(id=school_pk)
    lab.school.add(school)
    lab.save()
    return redirect('schools:lab_details', pk=pk)

def school_unassign_view(request, pk, school_pk):
    lab = Lab.objects.get(id=pk)
    school = School.objects.get(id=school_pk)
    lab.school.remove(school)
    lab.save()
    return redirect('schools:lab_details', pk=pk)