from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.contrib import messages
from users.models import UserAccount
from dashboard.views import DashboardView
from django.urls import reverse_lazy
from core.utils import generate_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class StaffCreateView(DashboardView, CreateView):
        model = UserAccount
        fields = ('first_name','last_name','email','phone_number','gender','staff_id')
        template_name = 'dashboard/users/Staff/add.html'

        def form_valid(self, form):
            random_password = generate_random_string()
            user = form.save(commit=False)
            user.username = user.email
            user.set_password(random_password)
            user.user_type = 'Staff'
            user.is_staff = True
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

            return super(StaffCreateView, self).form_valid(form)

        def get_success_url(self):
            messages.success(self.request,"Admin added successfully")
            return reverse_lazy('users:staff_details', kwargs ={'pk': self.object.id})

class StaffListView(DashboardView, ListView):
        model = UserAccount
        template_name = 'dashboard/users/Staff/list.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["users"] = UserAccount.objects.filter(user_type='Staff')
            return context

class StaffDetailView(DashboardView, DetailView):
    model = UserAccount
    template_name = 'dashboard/users/Staff/details.html'
    context_object_name = 'user'

class StaffSuspendView(DashboardView, DetailView):
    model = UserAccount
    context_object_name = 'user'
    template_name = 'dashboard/users/confirm-suspension.html'

    def get_success_url(self):
        return reverse_lazy('users:staff_details', kwargs={'pk': self.object.pk})