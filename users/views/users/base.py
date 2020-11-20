from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, UpdateView, TemplateView
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import get_object_or_404
User = get_user_model()

class BaseUserMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.user_type == 'Student' or user.user_type == 'Lecturer' or user.user_type == 'Lab_Tech':
            return True
        return False


class UserDetailView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'users/profile/details.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context["user"] = User.objects.get(id=user.id)
        return context


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('first_name','last_name','email','phone_number','gender','photo')
    template_name = 'users/profile/edit.html'

    def form_valid(self, form):
            user = form.save(commit=False)
            user.username = user.email.lower()
            user.save()

            return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Your Details have been successfully updated.")
        return reverse_lazy("users:user_profile")
