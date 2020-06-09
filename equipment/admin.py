from django.contrib import admin
from .models import Category, Equipment, Batch, Allocation, StorageUnit
# Register your models here.
admin.site.register(Category)
admin.site.register(Equipment)
admin.site.register(Batch)
admin.site.register(Allocation)
admin.site.register(StorageUnit)