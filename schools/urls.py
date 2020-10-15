from django.urls import path
from .views.departments import DepartmentCreateView, DepartmentListView, DepartmentDetailView, \
    DepartmentUpdateView

from .views.schools import SchoolCreateView, SchoolListView, SchoolDetailView, SchoolUpdateView
from .views.labs import LabCreateView, LabDetailView, LabListView, LabUpdateView, SchoolAssignView, \
    school_assign_view, school_unassign_view
from .views.courses import CourseCreateView, CourseListView, CourseDetailView, CourseUpdateView

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
    path('labs/<int:pk>/edit/',LabUpdateView.as_view(),name='lab_edit'),
    path('labs/<int:pk>/assign', SchoolAssignView.as_view(), name='lab_assign_school'),
    path('labs/<int:pk>/assign/<int:school_pk>/', school_assign_view, name='school_assign_action'),
    path('labs/<int:pk>/unassign/<int:school_pk>/', school_unassign_view, name='school_unassign_action'),

    path('courses/',CourseListView.as_view(),name='course_list'),
    path('courses/add/',CourseCreateView.as_view(),name='course_add'),
    path('courses/<int:pk>/details/',CourseDetailView.as_view(),name='course_details'),
    path('courses/<int:pk>/edit/',CourseUpdateView.as_view(),name='course_edit'),
]
