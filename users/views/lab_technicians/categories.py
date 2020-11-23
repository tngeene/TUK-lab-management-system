from .index import LabTechnicianView
from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from equipment.models import Category, Equipment


class CategoryCreateView(LabTechnicianView, CreateView):
    model = Category
    fields = ('name',)
    template_name = 'users/equipment/categories/add.html'

    def get_success_url(self):
        messages.success(self.request,"Category Added Successfully")
        return reverse_lazy('users:category_details', kwargs={'pk':self.object.pk})


class CategoryListView(LabTechnicianView, ListView):
    model = Category
    template_name = 'users/equipment/categories/list.html'
    context_object_name = 'categories'


class CategoryDetailView(LabTechnicianView, DetailView):
    model = Category
    template_name = 'users/equipment/categories/details.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        category = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipments"] = Equipment.objects.filter(category=category)
        context["category"] = Category.objects.filter(id=category).annotate(category_batch_count=Count('batch')
            ).annotate(category_equipment_count=Count('equipment_category')).first()
        return context

class CategoryUpdateView(LabTechnicianView, UpdateView):
    model = Category
    template_name = 'users/equipment/categories/edit.html'
    fields = ('name',)

    def get_success_url(self):
        messages.success(self.request,"Category Updated")
        return reverse_lazy('users:category_details', kwargs={'pk':self.object.pk})

class CategoryDeleteView(LabTechnicianView, DeleteView):
    model = Category
    context_object_name = 'category'
    template_name = 'users/equipment/categories/delete.html'

    def get_success_url(self) -> str:
        messages.success(self.request, "Category Deleted Succefully")
        return reverse_lazy("users:categories_list")