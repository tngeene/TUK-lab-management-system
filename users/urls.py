from django.urls import path

from users.views.admin_actions import suspend_user, unsuspend_user
from users.views.lab_sec import LabSecDashboardView
from users.views.lab_technicians.equipment import (EquipmentCreateView,
                                                   EquipmentDetailView,
                                                   EquipmentListView,
                                                   EquipmentUpdateView,
                                                   StorageUnitDetailView,
                                                   StorageUnitListView)
from users.views.lab_technicians.index import LabTechnicianDashboardView
from users.views.students import StudentorLecturerDashboardView
from users.views.users.allocations import (AllocationDetailView,
                                           AllocationListView)

from .views.lab_technicians.allocations import (AllocateToLecturerView,
                                                AllocateToStudentView,
                                                AllocationCreateView, allocate_equipment)
from .views.lecturers import LecturerDashboardView
from .views.users.base import UserDetailView, UserProfileUpdateView

app_name = "users"

urlpatterns = [
    # lab technician url
    path('lab-technicians-dashboard/', LabTechnicianDashboardView.as_view(),
         name='lab_technicians_dashboard_index'),
    path('equipment/all/', EquipmentListView.as_view(), name="equipment_list"),
    path('equipment/add/', EquipmentCreateView.as_view(), name="equipment_add"),
    path('equipment/<int:pk>/details',
         EquipmentDetailView.as_view(), name="equipment_details"),
    path('equipment/<int:pk>/edit',
         EquipmentUpdateView.as_view(), name="equipment_edit"),
    path('storage-units/', StorageUnitListView.as_view(),
         name="storage_units_list"),
    path('storage-units/<int:pk>/details',
         StorageUnitDetailView.as_view(), name="storage_unit_details"),

    # allocations urls
    path('allocations/new/', AllocationCreateView.as_view(), name="new_allocation"),
    # lab secretary urls
    path('lab-secretaries-dashboard/', LabSecDashboardView.as_view(),
         name='lab_sec_dashboard_index'),

    # student dashboard
    path('student-dashboard/', StudentorLecturerDashboardView.as_view(),
         name="student_dashboard_index"),

    # lecturer
    path('lecturer-dashboard/', LecturerDashboardView.as_view(),
         name="lecturer_dashboard_index"),

    path('users/<int:pk>/suspend_user', suspend_user, name="user_suspend_action"),
    path('admin/admin/users/<int:pk>/unsuspend_user',
         unsuspend_user, name="user_unsuspend_action"),
    path('my-profile/', UserDetailView.as_view(), name="user_profile"),
    path('<int:pk>/profile-update/',
         UserProfileUpdateView.as_view(), name="profile_update"),

    # Allocation urls
    path('allocations/all/', AllocationListView.as_view(), name="allocations_list"),
    path('allocations/<int:pk>/details/',
         AllocationDetailView.as_view(), name="allocation_details"),
    path('allocations/<int:pk>/allocate-to-student/',
         AllocateToStudentView.as_view(), name="allocate_to_student"),
    path('allocations/<int:pk>/allocate-to-lecturer/',
         AllocateToLecturerView.as_view(), name="allocate_to_lecturer"),
    path('allocations/<int:pk>/allocate/<int:user_pk>/',
         allocate_equipment, name="allocate_equipment_action"),
]
