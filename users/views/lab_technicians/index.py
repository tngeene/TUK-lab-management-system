from core.utils import generate_random_string
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)
from equipment.models import Allocation, Equipment
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
        lab_technician = self.request.user
        equipment = Equipment.objects.filter(added_by=lab_technician)
        context = super().get_context_data(**kwargs)
        context["my_allocations"] = Allocation.objects.filter(
            allocated_by=lab_technician).order_by('-pk')[:10]
        context["equipment_count"] = Equipment.objects.all().count()
        context["my_equipments"] = equipment.order_by('-pk')[:10]
        context["equipments"] = Equipment.objects.filter(lab=lab_technician.lab).order_by('-pk')[:10]
        return context
