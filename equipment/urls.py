from django.urls import path
from .views.categories import CategoryCreateView, CategoryDetailView, CategoryListView, CategoryUpdateView
from .views.batches import BatchCreateView, BatchListView, BatchDetailView, BatchUpdateView
from .views.equipment import EquipmentCreateView, EquipmentDetailView, EquipmentListView, EquipmentUpdateView, \
    mark_as_damaged, mark_as_working
from .views.storage_units import StorageUnitCreateView, StorageUnitListView, StorageUnitDetailView, \
        StorageUnitUpdateView

app_name = "equipment"


urlpatterns = [
    # equipment category urls
    path('categories/',CategoryListView.as_view(),name="categories_list"),
    path('categories/add',CategoryCreateView.as_view(),name="category_add"),
    path('categories/<int:pk>/details',CategoryDetailView.as_view(),name="category_details"),
    path('categories/<int:pk>/edit',CategoryUpdateView.as_view(),name="category_edit"),

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
    path('equipment/<int:pk>/mark-as-damaged',mark_as_damaged,name="equipment_damaged_action"),
    path('equipment/<int:pk>/mark-as-working',mark_as_working,name="equipment_working_action"),

    # storage units
    path('storage-units/',StorageUnitListView.as_view(),name="storage_units_list"),
    path('storage-units/add',StorageUnitCreateView.as_view(),name="storage_unit_add"),
    path('storage-units/<int:pk>/details',StorageUnitDetailView.as_view(),name="storage_unit_details"),
    path('storage-units/<int:pk>/edit',StorageUnitUpdateView.as_view(),name="storage_unit_edit"),
]
