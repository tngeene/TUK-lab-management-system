from allauth.account.views import LoginView
from django.views.generic import TemplateView,UpdateView
from django.contrib.auth import logout,login
from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth import authenticate
from django.urls import reverse_lazy

class IndexTemplateView(TemplateView):
    template_name = 'account/login.html'

def logout_user(request):
    logout(request)
    return redirect('index')

# handle redirect based on user role
def login_redirect(request):
    if request.user.user_type == 'Student':
        return redirect('users:student_dashboard_index')
    elif request.user.user_type == 'Lab_Tech':
        return redirect('users:lab_technicians_dashboard_index')
    elif request.user.user_type == 'Lab_Sec':
        return redirect('users:lab_sec_dashboard_index')
    elif request.user.is_staff:
        return redirect('dashboard:index')


class LoginUserView(LoginView):

    def get_success_url(self):
        return reverse_lazy('login_redirect')

def register_redirect(request):
    if request.user.user_type == 'Student':
        return redirect('users:student_dashboard_index')
    elif request.user.user_type == 'Lab_Tech':
        return redirect('users:lab_technician_dashboard_index')
    elif request.user.user_type == 'Lab_Sec':
        return redirect('users:lab_sec_dashboard')
    elif request.user.is_staff and request.user.user_type == 'Staff':
        return redirect('dashboard:index')


class RegisterUserView(UpdateView):
    def get_success_url(self):
        return reverse_lazy('register_redirect')