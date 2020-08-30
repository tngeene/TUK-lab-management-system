from django.shortcuts import render, redirect, get_object_or_404
from ..models import Equipment, Category
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views import DashboardView
from django.urls import reverse_lazy



class EquipmentCreateView(DashboardView, CreateView):
    model = Equipment
    fields = ('serial_no','category','lab','storage_unit')
    template_name = 'dashboard/equipment/equipment/add.html'

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_details', kwargs={'pk':self.object.pk})


class EquipmentListView(DashboardView, ListView):
    model = Equipment
    template_name = 'dashboard/equipment/equipment/list.html'
    context_object_name = 'equipments'


class EquipmentDetailView(DashboardView, DetailView):
    model = Equipment
    template_name = 'dashboard/equipment/equipment/details.html'
    context_object_name = 'equipment'


class EquipmentUpdateView(DashboardView, UpdateView):
    model = Equipment
    template_name = 'dashboard/equipment/equipment/edit.html'
    fields = ('lab','storage_unit')

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_details', kwargs={'pk':self.object.pk})

def mark_as_damaged(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.is_damaged = not equipment.is_damaged
    equipment.save()

    return redirect("equipment:equipment_details", pk=pk)

# logic for marking equipment as in good condition
def mark_as_working(request,pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.is_damaged = False
    equipment.save()

    return redirect("equipment:equipment_details", pk=pk)