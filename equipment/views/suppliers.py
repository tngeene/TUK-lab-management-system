from django.shortcuts import render
from django.contrib import messages
from ..models import Supplier, Batch
from django.db.models import Count
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views.dashboard import DashboardView
from django.urls import reverse_lazy

class SupplierCreateView(DashboardView, CreateView):
    model = Supplier
    fields = ('name', 'phone_number', 'email')
    template_name = 'dashboard/equipment/suppliers/add.html'

    def get_success_url(self):
        messages.success(self.request,"Supplier Added Successfully")
        return reverse_lazy("equipment:supplier_details", kwargs = { 'pk': self.object.pk})

class SupplierListView(DashboardView, ListView):
    model = Supplier
    context_object_name = 'suppliers'
    template_name = 'dashboard/equipment/suppliers/list.html'

class SupplierDetailView(DashboardView, DetailView):
    model = Supplier
    context_object_name = 'supplier'
    template_name = 'dashboard/equipment/suppliers/details.html'

    def get_context_data(self, **kwargs):
        supplier = self.object.id
        context = super().get_context_data(**kwargs)
        context["batches"] = Batch.objects.filter(supplier=supplier)
        return context



class SupplierUpdateView(DashboardView, UpdateView):
    model = Supplier
    fields = ('name', 'phone_number', 'email')
    template_name = 'dashboard/equipment/suppliers/edit.html'

    def get_success_url(self):
        messages.success(self.request,"Supplier Edited Successfully")
        return reverse_lazy("equipment:supplier_details", kwargs = { 'pk': self.object.pk})