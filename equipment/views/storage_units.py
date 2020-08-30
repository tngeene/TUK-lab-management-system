from django.shortcuts import render
from ..models import StorageUnit, Category, Equipment, Batch
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views import DashboardView
from django.urls import reverse_lazy
from django.db.models import Count


class StorageUnitCreateView(DashboardView, CreateView):
    model = StorageUnit
    fields = ('name','lab')
    template_name = 'dashboard/equipment/storage_units/add.html'

    def get_success_url(self):
        return reverse_lazy('equipment:storage_unit_details', kwargs={'pk':self.object.pk})


class StorageUnitListView(DashboardView, ListView):
    model = StorageUnit
    template_name = 'dashboard/equipment/storage_units/list.html'
    context_object_name = 'units'


class StorageUnitDetailView(DashboardView, DetailView):
    model = StorageUnit
    template_name = 'dashboard/equipment/storage_units/details.html'

    def get_context_data(self, **kwargs):
        unit = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipments"] = Equipment.objects.filter(storage_unit=unit)
        context["unit"] = StorageUnit.objects.filter(id=unit).annotate(equipment_count=Count('equipment')).first()
        return context



class StorageUnitUpdateView(DashboardView, UpdateView):
    model = StorageUnit
    template_name = 'dashboard/equipment/storage_units/edit.html'
    fields = ('name','lab')

    def get_success_url(self):
        return reverse_lazy('equipment:storage_unit_details', kwargs={'pk':self.object.pk})