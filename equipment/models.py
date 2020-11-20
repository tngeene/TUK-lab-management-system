from typing import Match
from django.db import models
from schools.models import Lab, Course, School
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .validators import validate_quantities

User = get_user_model()

class CommonInfo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True

class Category(CommonInfo):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Supplier(CommonInfo):
    name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Equipment(CommonInfo):
    name = models.CharField(max_length=254, null=True, blank=True)
    serial_no = models.CharField(max_length=80,null=True,blank=True)
    category = models.ForeignKey(Category,related_name='equipment_category',on_delete=models.PROTECT)
    batch = models.ForeignKey('Batch',on_delete=models.SET_NULL,related_name='equipment_batch',null=True,blank=True)
    lab = models.ForeignKey(Lab,related_name='equipment_lab',on_delete=models.PROTECT)
    storage_unit = models.ForeignKey('StorageUnit',on_delete=models.CASCADE,null=True)
    price = models.FloatField(null=True)
    is_allocated = models.BooleanField(default=False)
    has_exceeded_shelf_life = models.BooleanField(default=False)
    is_damaged = models.BooleanField(default=False)
    is_lost = models.BooleanField(default=False)
    price_to_pay = models.FloatField(null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='equipment_added', null=True)

    def __str__(self):
        return f"{self.serial_no} {self.category} {self.lab} {self.batch}"

class StorageUnit(CommonInfo):
    name = models.CharField(max_length=80,null=True)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE,related_name='storage_unit_lab',null=True)


    def __str__(self):
        return f"Name:{self.name} Lab:{self.lab.name}"

class Batch(CommonInfo):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    serial_no = models.CharField(max_length=45,null=True)
    school= models.ForeignKey(School,on_delete=models.CASCADE,related_name='batch_school',null=True)
    equipment_quantities = models.IntegerField(default=1, verbose_name='Quantities')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='batches', null=True)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

    def __str__(self):
        return f"{self.category} {self.serial_no} {self.equipment_quantities}"

ALLOCATION_USER_CHOICES = (
    ('Student', 'Student'),
    ('Lecturer', 'Lecturer'),
)

class Allocation(CommonInfo):
    allocating_to = models.CharField(max_length=30, choices=ALLOCATION_USER_CHOICES, default='student')
    allocated_to = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True,related_name='equipment_allocated')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True,related_name='allocations')
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,null=True,blank=True,related_name='allocations')
    allocated_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name='equipment_allocations')
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.equipment.serial_no} allocated by {self.allocated_by.get_full_name()}"

    def save(self, *args, **kwargs):
        if self.equipment:
            self.equipment.is_allocated = True

        if self.equipment and self.is_returned:
            self.equipment.is_allocated = False

        # if self.equipment.batch:
        #     if self.quantity < self.equipment.batch.equipment_quantities:
        #         raise ValidationError(f"Amount is higher than available quantities, please allocate a lower quantity.")

        super().save(*args, **kwargs)
