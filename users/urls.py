from django.urls import path
from users.views.staff import StaffCreateView, StaffDetailView, StaffDetailView, StaffListView, StaffSuspendView
from users.views.lab_technicians import LabTechnicianCreateView, LabTechnicianListView, LabTechnicianDetailView, \
    LabTechnicianSuspendView
from users.views.lab_sec import LabSecCreateView, LabSecListView, LabSecDetailView, LabSecSuspendView
from users.views.admin_actions import suspend_user, unsuspend_user


app_name = "users"

urlpatterns = [
    path('lab-technicans/', LabTechnicianListView.as_view(),name='lab_technicians_list'),
    path('lab-technicans/add', LabTechnicianCreateView.as_view(),name='lab_technician_add'),
    path('lab-technicans/<int:pk>/details', LabTechnicianDetailView.as_view(),name='lab_technician_details'),
    path('lab-technicans/<int:pk>/suspend', LabTechnicianSuspendView.as_view(),name='lab_technician_confirm_suspension'),

    path('lab-secretaries/',LabSecListView.as_view(),name='lab_secretaries_list'),
    path('lab-secretaries/add',LabSecCreateView.as_view(),name='lab_secretaries_add'),
    path('lab-secretaries/<int:pk>/details',LabSecDetailView.as_view(),name='lab_secretaries_details'),
    path('lab-/<int:pk>/suspend', LabSecSuspendView.as_view(),name='lab_secretary_confirm_suspension'),

    path('staff/',StaffListView.as_view(),name='staff_list'),
    path('staff/add',StaffCreateView.as_view(),name='staff_add'),
    path('staff/<int:pk>/details',StaffDetailView.as_view(),name='staff_details'),
    path('staff/<int:pk>/suspend',StaffSuspendView.as_view(),name='staff_confirm_suspension'),

    path('users/<int:pk>/suspend_user', suspend_user,name="user_suspend_action"),
    path('users/<int:pk>/unsuspend_user', unsuspend_user,name="user_unsuspend_action")
]
