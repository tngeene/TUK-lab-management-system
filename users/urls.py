from django.urls import path
from users.views.lab_technicians import LabTechnicianCreateView, LabTechnicianListView
from users.views.lab_sec import LabSecCreateView, LabSecListView

app_name = "users"

urlpatterns = [
    path('lab-technicans/', LabTechnicianListView.as_view(),name='lab_technicians_list'),
    path('lab-technicans/add', LabTechnicianCreateView.as_view(),name='lab_technician_add'),

    path('lab-secretaries/',LabSecListView.as_view(),name='lab_secretaries_list'),
    path('lab-secretaries/add',LabSecCreateView.as_view(),name='lab_secretaries_add'),
]
