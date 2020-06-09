from django.shortcuts import render
from ..models import Batch, Equipment
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views import DashboardView
from django.urls import reverse_lazy



class BatchCreateView(DashboardView, CreateView):
    model = Batch
    fields = ('category','serial_no','school','equipment_quantities')
    template_name = 'equipment/batches/add.html'

    def get_success_url(self):
        return reverse_lazy('equipment:batch_details', kwargs={'pk':self.object.pk})


class BatchListView(DashboardView, ListView):
    model = Batch
    template_name = 'equipment/batches/list.html'
    context_object_name = 'batches'


class BatchDetailView(DashboardView, DetailView):
    model = Batch
    template_name = 'equipment/batches/details.html'
    context_object_name = 'batch'


class BatchUpdateView(DashboardView, UpdateView):
    model = Batch
    template_name = 'equipment/batches/edit.html'
    fields = ('category','serial_no','school','equipment_quantities')

    def get_success_url(self):
        return reverse_lazy('equipment:batch_details', kwargs={'pk':self.object.pk})