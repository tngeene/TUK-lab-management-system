from django.urls import path

from users.views.admin_actions import suspend_user, unsuspend_user
from users.views.lab_sec import LabSecDashboardView
from users.views.lab_technicians import  LabTechnicianDashboardView
from users.views.students import  StudentDashboardView

app_name = "users"

urlpatterns = [
    # lab technician url
    path('lab-technicians-dashboard/', LabTechnicianDashboardView.as_view(),name='lab_technicians_dashboard_index'),

    # lab secretary urls
    path('lab-secretaries-dashboard/', LabSecDashboardView.as_view(), name='lab_sec_dashboard_index'),

    # student dashboard
    path('student-dashboard/', StudentDashboardView.as_view(),name="student_dashboard_index"),

    path('users/<int:pk>/suspend_user', suspend_user,name="user_suspend_action"),
    path('admin/admin/users/<int:pk>/unsuspend_user', unsuspend_user,name="user_unsuspend_action")
]
