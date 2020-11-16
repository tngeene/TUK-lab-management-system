from dashboard.views.dashboard import DashboardView
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..models import Batch, Category, Equipment


class CategoryCreateView(DashboardView, CreateView):
    model = Category
    fields = ('name',)
    template_name = 'dashboard/equipment/categories/add.html'

    def get_success_url(self):
        messages.success(self.request,"Category Added Successfully")
        return reverse_lazy('equipment:category_details', kwargs={'pk':self.object.pk})


class CategoryListView(DashboardView, ListView):
    model = Category
    template_name = 'dashboard/equipment/categories/list.html'
    context_object_name = 'categories'


class CategoryDetailView(DashboardView, DetailView):
    model = Category
    template_name = 'dashboard/equipment/categories/details.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        category = self.object.id
        context = super().get_context_data(**kwargs)
        context["batches"] = Batch.objects.filter(category=category)
        context["equipments"] = Equipment.objects.filter(category=category)
        context["category"] = Category.objects.filter(id=category).annotate(category_batch_count=Count('batch')
            ).annotate(category_equipment_count=Count('equipment_category')).first()
        return context

class CategoryUpdateView(DashboardView, UpdateView):
    model = Category
    template_name = 'dashboard/equipment/categories/edit.html'
    fields = ('name',)

    def get_success_url(self):
        messages.success(self.request,"Category Updated")
        return reverse_lazy('equipment:category_details', kwargs={'pk':self.object.pk})

class CategoryDeleteView(DashboardView, DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'dashboard/equipment/categories/delete.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Category Deleted Succefully")
        return reverse_lazy("equipment:categories_list")