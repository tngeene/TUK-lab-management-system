from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView

from ..models import UserAccount


# logic for suspending users and redirection based on user type
def suspend_user(request, pk):
    user = get_object_or_404(UserAccount, pk=pk)
    user.is_active = not user.is_active
    user.save()

    if(user.user_type == 'Lab_Tech'):
        messages.success(request,"User suspended")
        return redirect("dashboard:lab_technician_details", pk=pk)
    elif(user.user_type == 'Lab_Sec'):
        messages.success(request,"User suspended")
        return redirect("dashboard:lab_secretaries_details", pk=pk)
    elif(user.user_type == 'Staff'):
        messages.success(request,"User suspended")
        return redirect("dashboard:staff_details", pk=pk)
    elif(user.user_type == 'Student'):
        messages.success(request,"User suspended")
        return redirect("dashboard:student_details", pk=pk)
    elif(user.user_type == 'Lecturer'):
        messages.success(request,"User suspended")
        return redirect("dashboard:lecturer_details", pk=pk)

# logic for unsuspending users and redirection
def unsuspend_user(request,pk):
    user = get_object_or_404(UserAccount, pk=pk)
    user.is_active = True
    user.save()

    if(user.user_type == 'Lab_Tech'):
        messages.success(request,"User activated")
        return redirect("dashboard:lab_technician_details", pk=pk)
    elif(user.user_type == 'Lab_Sec'):
        messages.success(request,"User activated")
        return redirect("dashboard:lab_secretaries_details", pk=pk)
    elif(user.user_type == 'Staff'):
        messages.success(request,"User activated")
        return redirect("dashboard:staff_details", pk=pk)
    elif(user.user_type == 'Student'):
        messages.success(request,"User activated")
        return redirect("dashboard:student_details", pk=pk)
    elif(user.user_type == 'Lecturer'):
        messages.success(request,"User activated")
        return redirect("dashboard:lecturer_details", pk=pk)
