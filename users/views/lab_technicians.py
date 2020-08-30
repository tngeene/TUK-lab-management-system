from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from core.utils import generate_random_string
from dashboard.views import DashboardView, TemplateView
from equipment.models import Allocation
from users.models import UserAccount


class LabTechnicianCreateView(DashboardView, CreateView):
        model = UserAccount
        fields = ('first_name','last_name','email','phone_number','gender','staff_id')
        template_name = 'dashboard/users/lab_technicians/add.html'

        def form_valid(self, form):
            random_password = generate_random_string()
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(random_password)
            user.user_type = 'Lab_Tech'
            user.save()

            current_site = get_current_site(self.request)
            subject = 'TuK Account activation'
            message = render_to_string('account/password_reset_email.html', {
                'user': user.first_name,
                'email': user.email,
                'domain': current_site.domain,
                'password': random_password,
             })
            email = EmailMultiAlternatives(
            subject, message, from_email='tuklabs@tuk.ac.ke', to=[user.email, ])
            email.content_subtype = 'html'
            email.send()

            return super(LabTechnicianCreateView, self).form_valid(form)

        def get_success_url(self):
                return reverse_lazy('users:lab_technician_details', kwargs={'pk':self.object.pk})

class LabTechnicianListView(DashboardView, ListView):
        model = UserAccount
        template_name = 'dashboard/users/lab_technicians/list.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["users"] = UserAccount.objects.filter(user_type='Lab_Tech')
            return context

class LabTechnicianDetailView(DashboardView, DetailView):
    model = UserAccount
    template_name = 'dashboard/users/lab_technicians/details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        lab_technician = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipment_allocations"] = Allocation.objects.filter(allocated_by=lab_technician)
        return context

class LabTechnicianSuspendView(DashboardView, DetailView):
    model = UserAccount
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'

    def get_success_url(self):
        return reverse_lazy('users:lab_technician_details', kwargs={'pk': self.object.pk})

class LabTechnicianView(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.user_type == 'Lab_Tech':
            return True
        return False

class LabTechnicianDashboardView(LabTechnicianView, TemplateView):
    template_name = 'lab-technicians/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lab_technician = self.request.user
        context["my_allocations"] = Allocation.objects.filter(allocated_by=lab_technician).order_by('-pk')[:10]
