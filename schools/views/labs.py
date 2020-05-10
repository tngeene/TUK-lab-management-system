from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from dashboard.views import DashboardView
from django.urls import reverse_lazy
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