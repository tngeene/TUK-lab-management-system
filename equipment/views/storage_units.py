from django.shortcuts import render
from ..models import StorageUnit, Category, Equipment, Batch
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views import DashboardView
from django.urls import reverse_lazy



class StorageUnitCreateView(DashboardView, CreateView):
    model = StorageUnit
    fields = ('name','lab')
    template_name = 'equipment/storage_units/add.html'

    def get_success_url(self):
        return reverse_lazy('equipment:storage_unit_details', kwargs={'pk':self.object.pk})


class StorageUnitListView(DashboardView, ListView):
    model = StorageUnit
    template_name = 'equipment/storage_units/list.html'
    context_object_name = 'units'


class StorageUnitDetailView(DashboardView, DetailView):
    model = StorageUnit
    template_name = 'equipment/storage_units/details.html'
    context_object_name = 'unit'


class StorageUnitUpdateView(DashboardView, UpdateView):
    model = StorageUnit
    template_name = 'equipment/storage_units/edit.html'
    fields = ('name','lab')

    def get_success_url(self):
        return reverse_lazy('equipment:storage_unit_details', kwargs={'pk':self.object.pk})