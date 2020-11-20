from django.views.generic import DetailView, ListView
from equipment.models import Allocation

from .base import BaseUserMixin


class AllocationListView(BaseUserMixin, ListView):
    model = Allocation
    template_name = 'users/allocations/list.html'
    context_object_name = 'allocations'

    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'Lab_Tech':
            qs = Allocation.objects.filter(allocated_by__lab=user.lab)
            return qs
        elif user.user_type == 'Student' or user.user_type == 'Lecturer':
            qs = Allocation.objects.filter(allocated_to=user)
            return qs


class AllocationDetailView(BaseUserMixin, DetailView):
    model = Allocation
    template_name = 'users/allocations/details.html'
    context_object_name = 'allocation'
