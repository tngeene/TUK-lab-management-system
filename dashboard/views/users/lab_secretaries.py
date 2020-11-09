from core.utils import generate_random_string
from dashboard.utils import send_activation_email
from dashboard.views.dashboard import DashboardView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from users.models import UserAccount


class LabSecCreateView(DashboardView, CreateView):
    model = UserAccount
    fields = ('first_name', 'last_name', 'email', 'phone_number', 'gender',
              'staff_id')
    template_name = 'dashboard/users/lab_secretaries/add.html'

    def form_valid(self, form):
        random_password = generate_random_string()
        user = form.save(commit=False)
        user.username = user.email
        user.set_password(random_password)
        user.user_type = 'Lab_Sec'
        user.save()

        send_activation_email(user, random_password, self.request)

        return super(LabSecCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Lab Secretary Added successfully")
        return reverse_lazy('dashboard:lab_secretary_details',
                            kwargs={'pk': self.object.pk})


class LabSecListView(DashboardView, ListView):
    model = UserAccount
    template_name = 'dashboard/users/lab_secretaries/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserAccount.objects.filter(user_type='Lab_Sec')
        return context


class LabSecDetailView(DashboardView, DetailView):
    model = UserAccount
    template_name = 'dashboard/users/lab_secretaries/details.html'
    context_object_name = 'user'


class LabSecSuspendView(DashboardView, DetailView):
    model = UserAccount
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'
