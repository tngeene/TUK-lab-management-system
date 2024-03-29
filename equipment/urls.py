from django.urls import path

from .views.allocations import (AllocateToLecturerView, AllocateToStudentView,
                                AllocationCreateView, AllocationDetailView,
                                AllocationListView, AllocationUpdateView,
                                allocate_equipment, allocation_mark_as_damaged,
                                allocation_mark_as_fixed,
                                allocation_mark_as_lost,
                                allocation_mark_as_replaced, mark_as_returned,
                                unallocate_equipment)
from .views.batches import (BatchCreateView, BatchDetailView, BatchListView,
                            BatchUpdateView)
from .views.categories import (CategoryCreateView, CategoryDeleteView,
                               CategoryDetailView, CategoryListView,
                               CategoryUpdateView)
from .views.equipment import (EquipmentCreateView, EquipmentDeleteView,
                              EquipmentDetailView, EquipmentListView,
                              EquipmentUpdateView, mark_as_damaged,
                              mark_as_found, mark_as_lost, mark_as_out_service,
                              mark_as_working)
from .views.storage_units import (StorageUnitCreateView, StorageUnitDetailView,
                                  StorageUnitListView, StorageUnitUpdateView)
from .views.suppliers import (SupplierCreateView, SupplierDetailView,
                              SupplierListView, SupplierUpdateView)

app_name = "equipment"


urlpatterns = [
    # equipment category urls
    path('categories/',CategoryListView.as_view(),name="categories_list"),
    path('categories/add',CategoryCreateView.as_view(),name="category_add"),
    path('categories/<int:pk>/details',CategoryDetailView.as_view(),name="category_details"),
    path('categories/<int:pk>/edit',CategoryUpdateView.as_view(),name="category_edit"),
    path('categories/<int:pk>/delete',CategoryDeleteView.as_view(),name="category_delete"),

    # equipment batches urls
    path('batches/',BatchListView.as_view(),name="batch_list"),
    path('batches/add',BatchCreateView.as_view(),name="batch_add"),
    path('batches/<int:pk>/details',BatchDetailView.as_view(),name="batch_details"),
    path('batches/<int:pk>/edit',BatchUpdateView.as_view(),name="batch_edit"),

    #  equipment urls
    path('equipment/',EquipmentListView.as_view(),name="equipment_list"),
    path('equipment/add',EquipmentCreateView.as_view(),name="equipment_add"),
    path('equipment/<int:pk>/details',EquipmentDetailView.as_view(),name="equipment_details"),
    path('equipment/<int:pk>/edit',EquipmentUpdateView.as_view(),name="equipment_edit"),
    path('equipment/<int:pk>/delete',EquipmentDeleteView.as_view(),name="equipment_delete"),
    path('equipment/<int:pk>/mark-as-damaged/',mark_as_damaged,name="equipment_damaged_action"),
    path('equipment/<int:pk>/mark-as-working/',mark_as_working,name="equipment_working_action"),
    path('equipment/<int:pk>/mark-as-out-of-service/',mark_as_out_service,name="equipment_out_of_service_action"),
    path('equipment/<int:pk>/mark-as-lost/',mark_as_lost,name="equipment_lost_action"),
    path('equipment/<int:pk>/mark-as-found/',mark_as_found,name="equipment_found_action"),

    # supplier urls
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/add/', SupplierCreateView.as_view(), name='supplier_add'),
    path('suppliers/<int:pk>/details/', SupplierDetailView.as_view(), name='supplier_details'),
    path('suppliers/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_edit'),

    # storage units
    path('storage-units/',StorageUnitListView.as_view(),name="storage_units_list"),
    path('storage-units/add',StorageUnitCreateView.as_view(),name="storage_unit_add"),
    path('storage-units/<int:pk>/details',StorageUnitDetailView.as_view(),name="storage_unit_details"),
    path('storage-units/<int:pk>/edit',StorageUnitUpdateView.as_view(),name="storage_unit_edit"),

    # allocations
    path('allocations/',AllocationListView.as_view(),name="all_allocations"),
    path('allocations/new/',AllocationCreateView.as_view(),name="new_allocation"),
    path('allocations/<int:pk>/details/',AllocationDetailView.as_view(),name="allocation_details"),
    path('allocations/<int:pk>/edit',AllocationUpdateView.as_view(),name="allocation_edit"),
    path('allocations/<int:pk>/mark-as-returned/', mark_as_returned, name="allocation_return_action"),
    path('allocations/<int:pk>/mark-as-damaged/', allocation_mark_as_damaged, name="allocation_damaged_action"),
    path('allocations/<int:pk>/mark-as-fixed/', allocation_mark_as_fixed, name="allocation_fixed_action"),
    path('allocations/<int:pk>/mark-as-lost/', allocation_mark_as_lost, name="allocation_lost_action"),
    path('allocations/<int:pk>/mark-as-replaced/', allocation_mark_as_replaced, name="allocation_replaced_action"),
    path('allocations/<int:pk>/allocate-to-student/', AllocateToStudentView.as_view(), name="allocate_to_student"),
    path('allocations/<int:pk>/allocate-to-lecturer/', AllocateToLecturerView.as_view(), name="allocate_to_lecturer"),
    path('allocations/<int:pk>/allocate/<int:user_pk>/', allocate_equipment, name="allocate_equipment_action"),
    path('allocations/<int:pk>/unallocate/<int:user_pk>/', unallocate_equipment, name="unallocate_equipment_action"),
]
