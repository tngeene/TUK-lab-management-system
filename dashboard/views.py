from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from users.models import UserAccount
from schools.models import Lab

class DashboardView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return True
        return False

class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        lab_technicians = UserAccount.objects.filter(user_type='Lab_Tech')
        lab_secretaries = UserAccount.objects.filter(user_type='Lab_Sec')
        labs = Lab.objects.all()
        context = super().get_context_data(**kwargs)
        context["lab_technicians_count"] = lab_technicians.count()
        context["recent_lab_techs"] = lab_technicians.order_by("-pk")[:10]
        context["recent_lab_secs"] = lab_secretaries.order_by("-pk")[:10]
        context["labs_count"] = labs.count()
        return context


