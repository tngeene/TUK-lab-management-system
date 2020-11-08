from core.utils import generate_random_string
from dashboard.views.dashboard import DashboardView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from users.models import UserAccount


class LabSecCreateView(DashboardView, CreateView):
        model = UserAccount
        fields = ('first_name','last_name','email','phone_number','gender','staff_id')
        template_name = 'dashboard/users/lab_secretaries/add.html'

        def form_valid(self, form):
            random_password = generate_random_string()
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(random_password)
            user.user_type = 'Lab_Sec'
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

            return super(LabSecCreateView, self).form_valid(form)

        def get_success_url(self):
                return reverse_lazy('dashboard:index')

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

    def get_success_url(self):
        return reverse_lazy('users:lab_secretaries_details', kwargs={'pk': self.object.pk})


