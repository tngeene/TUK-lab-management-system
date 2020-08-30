from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from dashboard.views import DashboardView
from django.urls import reverse_lazy
from ..models import Course, Lab
from users.models import UserAccount
from django.db.models import Count

# Create your views here.

class CourseCreateView(DashboardView, CreateView):
    model = Course
    fields = ('name','code','department')
    template_name = 'dashboard/schools/courses/add.html'

    def get_success_url(self):
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
        return reverse_lazy('schools:course_details', kwargs={'pk': self.object.pk})