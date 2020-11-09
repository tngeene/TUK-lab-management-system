from dashboard.views.dashboard import DashboardView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from ..models import Allocation


class AllocationCreateView(CreateView):
    model = Allocation
    fields = ('equipment','quantity','allocated_to',)
    template_name  = 'dashboard/equipment/allocations/add.html'


    def form_valid(self, form):
        form.instance.allocated_by = self.request.user

        form.instance.equipment.is_allocated = True

        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request,"Allocation saved")
        return reverse_lazy('equipment:allocation_details',kwargs = {'pk': self.object.pk})

class AllocationListView(DashboardView,ListView):
    model = Allocation
    template_name = 'dashboard/equipment/allocations/list.html'
    context_object_name = 'allocations'


class AllocationDetailView(DetailView):
    model = Allocation
    template_name = 'dashboard/equipment/allocations/details.html'
    context_object_name = 'allocation'


class AllocationUpdateView(DashboardView, UpdateView):
    model = Allocation
    fields = ('is_returned',)
    template_name = 'dashboard/equipment/allocations/edit.html'

    def form_valid(self, form):
        allocation_id = self.kwargs['pk']
        current_allocation = Allocation.objects.get(id=allocation_id)
        print(f"current allocation is {current_allocation}")

        if form.instance.is_returned == True:
            current_allocation.equipment.is_allocated = False
            current_allocation.equipment.save()
        elif form.instance.is_returned == False:
            current_allocation.equipment.is_allocated = True
            current_allocation.equipment.save()

        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request,"Allocation updated")
        return reverse_lazy('equipment:allocation_details', kwargs={'pk': self.object.pk})


def mark_as_returned(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)

    allocation.equipment.is_allocated = not allocation.equipment.is_allocated
    allocation.equipment.save()

    allocation.is_returned = True
    allocation.save()

    messages.success(request,"Allocation updated")
    return redirect('equipment:allocation_details', pk=pk)

def mark_as_damaged(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)

    allocation.equipment.is_damaged = True
    allocation.equipment.save()

    messages.success(request,"Equipment marked as damaged")
    return redirect('equipment:allocation_details', pk=pk)
