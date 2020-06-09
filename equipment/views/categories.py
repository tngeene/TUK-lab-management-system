from django.shortcuts import render
from ..models import Category, Equipment
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views import DashboardView
from django.urls import reverse_lazy



class CategoryCreateView(DashboardView, CreateView):
    model = Category
    fields = ('name',)
    template_name = 'equipment/categories/add.html'

    def get_success_url(self):
        return reverse_lazy('equipment:category_details', kwargs={'pk':self.object.pk})


class CategoryListView(DashboardView, ListView):
    model = Category
    template_name = 'equipment/categories/list.html'
    context_object_name = 'categories'


class CategoryDetailView(DashboardView, DetailView):
    model = Category
    template_name = 'equipment/categories/details.html'
    context_object_name = 'category'


class CategoryUpdateView(DashboardView, UpdateView):
    model = Category
    template_name = 'equipment/categories/edit.html'
    fields = ('name',)

    def get_success_url(self):
        return reverse_lazy('equipment:category_details', kwargs={'pk':self.object.pk})