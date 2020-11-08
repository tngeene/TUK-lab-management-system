from django.contrib import messages
from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView)

from dashboard.views.dashboard import DashboardView
from users.models import UserAccount

from ..models import Course, Lab


class CourseCreateView(DashboardView, CreateView):
    model = Course
    fields = ('name','code','department')
    template_name = 'dashboard/schools/courses/add.html'

    def get_success_url(self):
        messages.success(self.request,"Course Added Successfully")
        return reverse_lazy('schools:course_details', kwargs={'pk': self.object.pk})


class CourseListView(DashboardView, ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'dashboard/schools/courses/list.html'


class CourseDetailView(DashboardView, DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'dashboard/schools/courses/details.html'

    def get_context_data(self, **kwargs):
        course = self.object.id
        context = super().get_context_data(**kwargs)
        context["users"] = UserAccount.objects.filter(course=course)
        context["course"] = Course.objects.filter(id=course).annotate(students_in_course_count=Count('useraccount')).first()
        return context


class CourseUpdateView(DashboardView, UpdateView):
    model = Course
    template_name = 'dashboard/schools/courses/edit.html'
    fields = ('name','department')

    def get_success_url(self):
        messages.success(self.request,"Course Updated")
        return reverse_lazy('schools:course_details', kwargs={'pk': self.object.pk})
