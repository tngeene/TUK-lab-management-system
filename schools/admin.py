from django.contrib import admin
from .models import Department, School, Lab
# Register your models here.
admin.site.register(Department)
admin.site.register(School)
admin.site.register(Lab)