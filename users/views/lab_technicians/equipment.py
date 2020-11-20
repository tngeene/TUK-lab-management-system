from django.contrib import messages
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from users.views.lab_technicians.index import LabTechnicianView

from equipment.models import Equipment, StorageUnit


class EquipmentCreateView(LabTechnicianView, CreateView):
    model = Equipment
    fields = ('name', 'serial_no', 'category', 'storage_unit', 'price')
    template_name = 'users/equipment/add.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.added_by = user
        form.instance.lab = user.lab
        return super(EquipmentCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Equipment Added successfully")
        return reverse_lazy('users:equipment_details', kwargs={'pk': self.object.pk})


class EquipmentListView(ListView):
    model = Equipment
    template_name = 'users/equipment/list.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        user = self.request.user
        return Equipment.objects.filter(lab=user.lab)


class EquipmentDetailView(LabTechnicianView, DetailView):
    model = Equipment
    template_name = 'users/equipment/details.html'
    context_object_name = 'equipment'


class EquipmentUpdateView(LabTechnicianView, UpdateView):
    model = Equipment
    template_name = 'users/equipment/edit.html'
    fields = ('name', 'serial_no', 'category', 'storage_unit', 'price')

    def get_success_url(self):
        messages.success(self.request, "Equipment Updated successfully")
        return reverse_lazy('users:equipment_details', kwargs={'pk': self.object.pk})


class StorageUnitListView(LabTechnicianView, ListView):
    model = StorageUnit
    context_object_name = 'units'
    template_name = 'users/equipment/storage_units/list.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["units"] = StorageUnit.objects.filter(lab=user.lab)
        return context


class StorageUnitDetailView(LabTechnicianView, DetailView):
    model = StorageUnit
    context_object_name = 'unit'
    template_name = 'users/equipment/storage_units/details.html'

    def get_context_data(self, **kwargs):
        storage_unit = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipments"] = Equipment.objects.filter(
            storage_unit=storage_unit)
        context["unit"] = StorageUnit.objects.filter(id=storage_unit).annotate(
            equipment_count=Count('equipment')).first()
        return context
