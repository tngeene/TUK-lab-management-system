from core.utils import generate_random_string
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from equipment.models import Allocation
from users.models import UserAccount


class LabTechnicianView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.user_type == 'Lab_Tech':
            return True
        return False


class LabTechnicianDashboardView(LabTechnicianView, TemplateView):
    template_name = 'lab-technicians/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lab_technician = self.request.user
        context["my_allocations"] = Allocation.objects.filter(
            allocated_by=lab_technician).order_by('-pk')[:10]
