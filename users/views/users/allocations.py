from django.views.generic import DetailView, ListView
from equipment.models import Allocation

from .base import BaseUserMixin


class AllocationListView(BaseUserMixin, ListView):
    model = Allocation
    template_name = 'users/allocations/list.html'


    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        if user.user_type == 'Student' or user.user_type == 'Lecturer':
            context["allocations"] = Allocation.objects.filter(allocated_to=user)
            context["lost_allocations"] = Allocation.objects.filter(equipment__is_lost=True, allocated_to=user)
            context["damaged_allocations"] = Allocation.objects.filter(equipment__is_damaged=True, allocated_to=user)
            context["returned_allocations"] = Allocation.objects.filter(is_returned=True, allocated_to=user)
            context["unreturned_allocations"] = Allocation.objects.filter(is_returned=False, allocated_to=user)
            context["logged_in_user_allocations"] = Allocation.objects.filter(allocated_to=user)
        elif user.user_type == 'Lab_Tech':
            context["allocations"] = Allocation.objects.filter(allocated_by__lab=user.lab )
            context["lost_allocations"] = Allocation.objects.filter(equipment__is_lost=True, allocated_by__lab=user.lab )
            context["damaged_allocations"] = Allocation.objects.filter(equipment__is_damaged=True, allocated_by__lab=user.lab)
            context["returned_allocations"] = Allocation.objects.filter(is_returned=True, allocated_by__lab=user.lab)
            context["unreturned_allocations"] = Allocation.objects.filter(is_returned=False, allocated_by__lab=user.lab)
            context["logged_in_user_allocations"] = Allocation.objects.filter(allocated_by=user)
        return context

class AllocationDetailView(BaseUserMixin, DetailView):
    model = Allocation
    template_name = 'users/allocations/details.html'
    context_object_name = 'allocation'
