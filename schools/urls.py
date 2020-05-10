from django.urls import path
from .views.departments import DepartmentCreateView, DepartmentListView, DepartmentDetailView, \
    DepartmentUpdateView

from .views.schools import SchoolCreateView, SchoolListView, SchoolDetailView, SchoolUpdateView
from .views.labs import LabCreateView, LabDetailView, LabListView, LabUpdateView

app_name = "schools"

urlpatterns = [
    
    path('departments/add/',DepartmentCreateView.as_view(),name='department_add'),
    path('departments/list/',DepartmentListView.as_view(),name='departments_list'),
    path('departments/<int:pk>/details',DepartmentDetailView.as_view(),name='department_details'),
    path('departments/<int:pk>/edit',DepartmentUpdateView.as_view(),name='department_edit'),

    path('schools/add/',SchoolCreateView.as_view(),name='school_add'),
    path('schools/list/',SchoolListView.as_view(),name='schools_list'),
    path('schools/<int:pk>/details',SchoolDetailView.as_view(),name='school_details'),
    path('schools/<int:pk>/edit',SchoolUpdateView.as_view(),name='school_edit'),

    path('labs/add', LabCreateView.as_view(),name='lab_add'),
    path('labs/',LabListView.as_view(),name='labs_list'),
    path('labs/<int:pk>/details', LabDetailView.as_view(),name='lab_details'),
    path('labs/<int:pk>/edit/',LabUpdateView.as_view(),name='lab_edit')
]
