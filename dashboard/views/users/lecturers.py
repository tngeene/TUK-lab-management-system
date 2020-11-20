from core.utils import generate_random_string
from dashboard.utils import send_activation_email
from dashboard.views.dashboard import DashboardView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from equipment.models import Allocation

from users.models import UserAccount


class LecturerCreateView(DashboardView, CreateView):
    model = UserAccount
    fields = ('first_name', 'last_name', 'email',
              'phone_number', 'gender', 'departmemt', 'staff_id')
    template_name = 'dashboard/users/lecturers/add.html'

    def form_valid(self, form):
        random_password = generate_random_string()
        user = form.save(commit=False)
        user.username = user.email
        user.set_password(random_password)
        user.user_type = 'Lecturer'
        user.save()

        send_activation_email(user, random_password, self.request)

        return super(LecturerCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Lecturer successfully Added")
        return reverse_lazy('dashboard:lecturer_details', kwargs={'pk': self.object.pk})


class LecturerListView(DashboardView, ListView):
    model = UserAccount
    template_name = 'dashboard/users/lecturers/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserAccount.objects.filter(user_type='Lecturer')
        return context


class LecturerDetailView(DashboardView, DetailView):
    model = UserAccount
    template_name = 'dashboard/users/lecturers/details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        lecturer = self.object.id
        context = super().get_context_data(**kwargs)
        context["equipment_allocations"] = Allocation.objects.filter(
            allocated_to=lecturer)
        return context


class LecturerSuspendView(DashboardView, DetailView):
    model = UserAccount
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'
