from django.views.generic import DetailView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy

from ..models import UserAccount

# logic for suspending users and redirection based on user type
def suspend_user(request, pk):
    user = get_object_or_404(UserAccount, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if(user.user_type == 'Lab_Tech'):
        return redirect("users:lab_technician_details", pk=pk)
    elif(user.user_type == 'Lab_Sec'):
        return redirect("users:lab_secretaries_details", pk=pk)
    elif(user.user_type == 'Staff'):
        return redirect("users:staff_details", pk=pk)
    elif(user.user_type == 'Student'):
        return redirect("users:student_details", pk=pk)

# logic for unsuspending users and redirection
def unsuspend_user(request,pk):
    user = get_object_or_404(UserAccount, pk=pk)
    user.is_active = True
    user.save()

    if(user.user_type == 'Lab_Tech'):
        return redirect("users:lab_technician_details", pk=pk)
    elif(user.user_type == 'Lab_Sec'):
        return redirect("users:lab_secretaries_details", pk=pk)
    elif(user.user_type == 'Staff'):
        return redirect("users:staff_details", pk=pk)
    elif(user.user_type == 'Student'):
        return redirect("users:student_details", pk=pk)

