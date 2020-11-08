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

class DashboardBaseView(TemplateView):
    template_name = 'dashboard/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

class DashboardTemplateView(DashboardView, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        lab_technicians = UserAccount.objects.filter(user_type='Lab_Tech')
        lab_secretaries = UserAccount.objects.filter(user_type='Lab_Sec')
        students = UserAccount.objects.filter(user_type='Student')
        labs = Lab.objects.all()
        context = super().get_context_data(**kwargs)
        context["lab_technicians_count"] = lab_technicians.count()
        context["labs_count"] = labs.count()
        context["students_count"] = students.count()
        context["recent_lab_techs"] = lab_technicians.order_by("-pk")[:10]
        context["recent_lab_secs"] = lab_secretaries.order_by("-pk")[:10]
        return context


