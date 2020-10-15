from django.urls import path

from users.views.admin_actions import suspend_user, unsuspend_user
from users.views.lab_sec import (LabSecCreateView, LabSecDashboardView,
                                 LabSecDetailView, LabSecListView,
                                 LabSecSuspendView)
from users.views.lab_technicians import (LabTechnicianCreateView,
                                         LabTechnicianDashboardView,
                                         LabTechnicianDetailView,
                                         LabTechnicianListView,
                                         LabTechnicianSuspendView)
from users.views.staff import (
    StaffCreateView, StaffDetailView, StaffListView, StaffSuspendView)
from users.views.students import (StudentCreateView, StudentDashboardView,
                                  StudentDetailView, StudentListView,
                                  StudentSuspendView)

app_name = "users"

urlpatterns = [
    # lab technician url
    path('admin/lab-technicans/', LabTechnicianListView.as_view(),name='lab_technicians_list'),
    path('admin/lab-technicans/add', LabTechnicianCreateView.as_view(),name='lab_technician_add'),
    path('admin/lab-technicans/<int:pk>/details', LabTechnicianDetailView.as_view(),name='lab_technician_details'),
    path('admin/lab-technicans/<int:pk>/suspend', LabTechnicianSuspendView.as_view(),name='lab_technician_confirm_suspension'),

    path('lab-technicians-dashboard/', LabTechnicianDashboardView.as_view(),name='lab_technicians_dashboard_index'),

    # lab secretary urls
    path('admin/lab-secretaries/',LabSecListView.as_view(),name='lab_secretaries_list'),
    path('admin/lab-secretaries/add',LabSecCreateView.as_view(),name='lab_secretaries_add'),
    path('admin/lab-secretaries/<int:pk>/details',LabSecDetailView.as_view(),name='lab_secretaries_details'),
    path('admin/lab-/<int:pk>/suspend', LabSecSuspendView.as_view(),name='lab_secretary_confirm_suspension'),

    path('lab-secretaries-dashboard/', LabSecDashboardView.as_view(), name='lab_sec_dashboard_index'),

    # staff urls
    path('admin/staff/',StaffListView.as_view(),name='staff_list'),
    path('admin/staff/add',StaffCreateView.as_view(),name='staff_add'),
    path('admin/staff/<int:pk>/details',StaffDetailView.as_view(),name='staff_details'),
    path('admin/staff/<int:pk>/suspend',StaffSuspendView.as_view(),name='staff_confirm_suspension'),

    path('admin/students/',StudentListView.as_view(),name='students_list'),
    path('admin/students/add',StudentCreateView.as_view(),name='student_add'),
    path('admin/students/<int:pk>/details',StudentDetailView.as_view(),name='student_details'),
    path('admin/students/<int:pk>/suspend',StudentSuspendView.as_view(),name='student_confirm_suspension'),

    # student dashboard
    path('student-dashboard/', StudentDashboardView.as_view(),name="student_dashboard_index"),

    path('users/<int:pk>/suspend_user', suspend_user,name="user_suspend_action"),
    path('admin/admin/users/<int:pk>/unsuspend_user', unsuspend_user,name="user_unsuspend_action")
]
