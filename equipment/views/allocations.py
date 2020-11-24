from dashboard.views.dashboard import DashboardView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from users.views.forms import AllocationCreateForm
from ..models import Allocation, User


class AllocationCreateView(CreateView):
    model = Allocation
    form_class = AllocationCreateForm
    template_name  = 'dashboard/equipment/allocations/add.html'

    user_type = None
    def form_valid(self, form):
        allocation = form.save(commit=False)
        self.user_type = allocation.allocating_to
        allocation.allocated_by = self.request.user
        allocation.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        if self.user_type == 'Student':
            return reverse_lazy('equipment:allocate_to_student',kwargs = {'pk': self.object.pk})
        return reverse_lazy('equipment:allocate_to_lecturer',kwargs = {'pk': self.object.pk})


class AllocateToStudentView(ListView):
    model = User
    template_name  = 'dashboard/equipment/allocations/allocate-student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(user_type='Student')
        context["allocation"] = Allocation.objects.get(id=self.kwargs['pk'])
        return context

class AllocateToLecturerView(ListView):
    model = User
    template_name  = 'dashboard/equipment/allocations/allocate-lecturer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(user_type='Lecturer')
        context["allocation"] = Allocation.objects.get(id=self.kwargs['pk'])
        return context

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

    allocation.equipment.is_allocated = False
    allocation.equipment.save()

    allocation.is_returned = True
    allocation.save()

    messages.success(request,"Allocation updated")
    if request.user.user_type == 'Staff':
        return redirect('equipment:allocation_details', pk=pk)
    return redirect('users:allocation_details', pk=pk)

def allocation_mark_as_damaged(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)

    allocation.equipment.is_damaged = True
    allocation.equipment.save()

    messages.success(request,"Equipment marked as damaged")
    if request.user.user_type == 'Staff':
        return redirect('equipment:allocation_details', pk=pk)
    return redirect('users:allocation_details', pk=pk)


def allocation_mark_as_fixed(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)

    allocation.equipment.is_damaged = False
    allocation.equipment.save()

    messages.success(request,"Equipment marked as fixed")
    if request.user.user_type == 'Staff':
        return redirect('equipment:allocation_details', pk=pk)
    return redirect('users:allocation_details', pk=pk)


def allocate_equipment(request, pk, user_pk):
    allocation = get_object_or_404(Allocation, id=pk)
    user = get_object_or_404(User, id=user_pk)
    allocation.allocated_to = user
    allocation.equipment.is_allocated == True
    allocation.save()
    messages.success(request, "Equipment Allocated")
    return redirect("equipment:allocation_details", pk=pk)


def unallocate_equipment(request, pk, user_pk):
    allocation = get_object_or_404(Allocation, id=pk)
    user = get_object_or_404(User, id=user_pk)

    allocation.equipment.is_allocated = False
    allocation.equipment.save()

    allocation.allocated_to.remove(user)
    allocation.save()
    return redirect("equipment:allocation_details", pk=pk)

def allocation_mark_as_lost(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)

    allocation.equipment.is_lost = True
    allocation.equipment.save()

    allocation.is_returned = False
    allocation.save()

    messages.success(request,"Allocation updated")
    if request.user.user_type == 'Staff':
        return redirect('equipment:allocation_details', pk=pk)
    return redirect('users:allocation_details', pk=pk)

def allocation_mark_as_replaced(request, pk):
    allocation = get_object_or_404(Allocation, pk=pk)

    allocation.equipment.is_lost = False
    allocation.equipment.save()

    allocation.is_returned = True
    allocation.save()

    messages.success(request,"Allocation updated")
    if request.user.user_type == 'Staff':
        return redirect('equipment:allocation_details', pk=pk)
    return redirect('users:allocation_details', pk=pk)