from django.urls import path

from dashboard.views.dashboard import DashboardTemplateView

from .views.users.lab_secretaries import (LabSecCreateView, LabSecDetailView,
                                          LabSecListView, LabSecSuspendView)
from .views.users.lab_technicians import (LabTechnicianCreateView,
                                          LabTechnicianDetailView,
                                          LabTechnicianListView,
                                          LabTechnicianSuspendView)
from .views.users.staff import (StaffCreateView, StaffDetailView,
                                StaffListView, StaffSuspendView)
from .views.users.students import (StudentCreateView, StudentDetailView,
                                   StudentListView, StudentSuspendView)

app_name = "dashboard"

urlpatterns = [
    path('', DashboardTemplateView.as_view(), name='index'),

    # students urls
    path('admin/students/',StudentListView.as_view(),name='students_list'),
    path('admin/students/add',StudentCreateView.as_view(),name='student_add'),
    path('admin/students/<int:pk>/details',StudentDetailView.as_view(),name='student_details'),
    path('admin/students/<int:pk>/suspend',StudentSuspendView.as_view(),name='student_confirm_suspension'),

    # staff urls
    path('admin/staff/',StaffListView.as_view(),name='staff_list'),
    path('admin/staff/add',StaffCreateView.as_view(),name='staff_add'),
    path('admin/staff/<int:pk>/details',StaffDetailView.as_view(),name='staff_details'),
    path('admin/staff/<int:pk>/suspend',StaffSuspendView.as_view(),name='staff_confirm_suspension'),

    # lab technician urls
    path('admin/lab-technicans/', LabTechnicianListView.as_view(),name='lab_technicians_list'),
    path('admin/lab-technicans/add', LabTechnicianCreateView.as_view(),name='lab_technician_add'),
    path('admin/lab-technicans/<int:pk>/details', LabTechnicianDetailView.as_view(),name='lab_technician_details'),
    path('admin/lab-technicans/<int:pk>/suspend', LabTechnicianSuspendView.as_view(),name='lab_technician_confirm_suspension'),

    # lab secretaries
    path('admin/lab-secretaries/',LabSecListView.as_view(),name='lab_secretaries_list'),
    path('admin/lab-secretaries/add',LabSecCreateView.as_view(),name='lab_secretaries_add'),
    path('admin/lab-secretaries/<int:pk>/details',LabSecDetailView.as_view(),name='lab_secretaries_details'),
    path('admin/lab-/<int:pk>/suspend', LabSecSuspendView.as_view(),name='lab_secretary_confirm_suspension'),
]
