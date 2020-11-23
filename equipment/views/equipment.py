from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from dashboard.views.dashboard import DashboardView

from ..models import Category, Equipment


class EquipmentCreateView(DashboardView, CreateView):
    model = Equipment
    fields = ('name', 'serial_no','category','lab','storage_unit', 'price')
    template_name = 'dashboard/equipment/equipment/add.html'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(EquipmentCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request,"Equipment Added successfully")
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
    fields = ('name', 'serial_no', 'lab','storage_unit', 'price')

    def get_success_url(self):
        return reverse_lazy('equipment:equipment_details', kwargs={'pk':self.object.pk})

def mark_as_damaged(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.is_damaged = not equipment.is_damaged
    equipment.save()

    messages.success(request,"Equipment marked as damaged")
    if request.user.user_type == 'Staff':
        return redirect("equipment:equipment_details", pk=pk)
    return redirect("users:equipment_details", pk=pk)

class EquipmentDeleteView(DashboardView, DeleteView):
    model = Equipment
    context_object_name = 'equipment'
    template_name = 'dashboard/equipment/equipment/delete.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Equipment Deleted Succefully")
        return reverse_lazy("equipment:equipment_list")

# logic for marking equipment as in good condition
def mark_as_working(request,pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.is_damaged = False
    if equipment.has_exceeded_shelf_life == True:
        equipment.has_exceeded_shelf_life = False
    equipment.save()

    messages.success(request,"Equipment marked as working")
    if request.user.user_type == 'Staff':
        return redirect("equipment:equipment_details", pk=pk)
    return redirect("users:equipment_details", pk=pk)


# logic for marking equipment as in good condition
def mark_as_out_service(request,pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.has_exceeded_shelf_life = True
    equipment.is_damaged = True
    equipment.save()

    messages.success(request,"Equipment marked as out of service")
    if request.user.user_type == 'Staff':
        return redirect("equipment:equipment_details", pk=pk)
    return redirect("users:equipment_details", pk=pk)

def mark_as_lost(request,pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.is_lost = True
    equipment.save()

    messages.success(request,"Equipment marked as lost")
    if request.user.user_type == 'Staff':
        return redirect("equipment:equipment_details", pk=pk)
    return redirect("users:equipment_details", pk=pk)

def mark_as_found(request,pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.is_lost = not equipment.is_lost
    equipment.save()

    messages.success(request,"Equipment marked as replaced")
    if request.user.user_type == 'Staff':
        return redirect("equipment:equipment_details", pk=pk)
    return redirect("users:equipment_details", pk=pk)
