from django.shortcuts import render
from ..models import Equipment, Category
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views import DashboardView
from django.urls import reverse_lazy



class EquipmentCreateView(DashboardView, CreateView):
    model = Equipment
    fields = ('serial_no','category','lab','storage_unit')
    template_name = 'equipment/equipment/add.html'

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_details', kwargs={'pk':self.object.pk})


class EquipmentListView(DashboardView, ListView):
    model = Equipment
    template_name = 'equipment/equipment/list.html'
    context_object_name = 'equipments'


class EquipmentDetailView(DashboardView, DetailView):
    model = Equipment
    template_name = 'equipment/equipment/details.html'
    context_object_name = 'equipment'


class EquipmentUpdateView(DashboardView, UpdateView):
    model = Equipment
    template_name = 'equipment/equipment/edit.html'
    fields = ('lab','storage_unit')

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_details', kwargs={'pk':self.object.pk})