from django.urls import path
from users.views.lab_technicians import LabTechnicianCreateView, LabTechnicianListView, LabTechnicianDetailView
from users.views.lab_sec import LabSecCreateView, LabSecListView, LabSecDetailView

app_name = "users"

urlpatterns = [
    path('lab-technicans/', LabTechnicianListView.as_view(),name='lab_technicians_list'),
    path('lab-technicans/add', LabTechnicianCreateView.as_view(),name='lab_technician_add'),
    path('lab-technicans/<int:pk>/details', LabTechnicianDetailView.as_view(),name='lab_technician_details'),

    path('lab-secretaries/',LabSecListView.as_view(),name='lab_secretaries_list'),
    path('lab-secretaries/add',LabSecCreateView.as_view(),name='lab_secretaries_add'),
    path('lab-secretaries/<int:pk>/details',LabSecDetailView.as_view(),name='lab_secretaries_details'),
]
