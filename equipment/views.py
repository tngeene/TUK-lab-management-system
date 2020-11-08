from django.shortcuts import render
from .models import Category, Equipment
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from dashboard.views.dashboard import DashboardView



class CategoryCreateView(DashboardView, CreateView):
    model = Category
    fields = ("name")
    template_name = 'equipment/categories/add.html'


class CategoryListView(DashboardView, ListView):
    model = Category
    template_name = 'equipment/categories/list.html'
    context_object_name = 'categories'


class CategoryDetailView(DashboardView, DetailView):
    model = Category
    template_name = 'equipment/categories/details.html'
    context_object_name = 'category'