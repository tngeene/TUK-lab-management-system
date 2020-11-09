from django.contrib import messages
from core.utils import generate_random_string
from dashboard.utils import send_activation_email
from dashboard.views.dashboard import DashboardView, TemplateView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from equipment.models import Allocation

from users.models import UserAccount


class LabTechnicianCreateView(DashboardView, CreateView):
    model = UserAccount
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'gender',
              'staff_id')
    template_name = 'dashboard/users/lab_technicians/add.html'

    def form_valid(self, form):
        random_password = generate_random_string()
        user = form.save(commit=False)
        user.username = user.email
        user.set_password(random_password)
        user.user_type = 'Lab_Tech'
        user.save()

        send_activation_email(user, random_password, self.request)

        return super(LabTechnicianCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Lab Technician Added Successfully")
        return reverse_lazy('dashboard:lab_technician_details',
                            kwargs={'pk': self.object.pk})


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
        context["equipment_allocations"] = Allocation.objects.filter(
            allocated_by=lab_technician)
        return context


class LabTechnicianSuspendView(DashboardView, DetailView):
    model = UserAccount
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'

    def get_success_url(self):
        return reverse_lazy('users:lab_technician_details',
                            kwargs={'pk': self.object.pk})
