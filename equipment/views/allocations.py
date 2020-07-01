from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from ..models import Allocation
from dashboard.views import DashboardView


class AllocationCreateView(DashboardView,CreateView):
    model = Allocation
    fields = ('equipment','quantity','student',)
    template_name  = 'equipment/allocations/add.html'


    def form_valid(self, form):
        form.instance.allocated_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('equipment:allocation_details',kwargs = {'pk': self.object.pk})

class AllocationListView(DashboardView,ListView):
    model = Allocation
    template_name = 'equipment/allocations/list.html'
    context_object_name = 'allocations'


class AllocationDetailView(DashboardView, DetailView):
    model = Allocation
    template_name = 'equipment/allocations/details.html'
    context_object_name = 'allocation'


class AllocationUpdateView(DashboardView, UpdateView):
    model = Allocation
    fields = ('is_returned',)
    template_name = 'equipment/allocations/edit.html'

    def get_success_url(self):
        return reverse_lazy('equipment:allocation_details', kwargs={'pk': self.object.pk})
