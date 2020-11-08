from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from users.models import UserAccount
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from core.utils import generate_random_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site


class LabSecView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.user_type == 'Lab_Sec':
            return True
        return False

class LabSecDashboardView(LabSecView, TemplateView):
    template_name = 'lab-secretaries/dashboard.html'
