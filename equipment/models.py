from django.db import models
from schools.models import Lab, Course, School
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .validators import validate_quantities

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Equipment(models.Model):
    serial_no = models.CharField(max_length=80,null=True,blank=True)
    category = models.ForeignKey(Category,related_name='equipment_category',on_delete=models.PROTECT)
    batch = models.ForeignKey('Batch',on_delete=models.SET_NULL,related_name='equipment_batch',null=True,blank=True)
    lab = models.ForeignKey(Lab,related_name='equipment_lab',on_delete=models.PROTECT)
    storage_unit = models.ForeignKey('StorageUnit',on_delete=models.CASCADE,null=True)
    is_allocated = models.BooleanField(default=False)
    is_damaged = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.serial_no} {self.category} {self.lab} {self.batch}"

class StorageUnit(models.Model):
    name = models.CharField(max_length=80,null=True)
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE,related_name='storage_unit_lab',null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"Name:{self.name} Lab:{self.lab.name}"

class Batch(models.Model):
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    serial_no = models.CharField(max_length=45,null=True)
    school= models.ForeignKey(School,on_delete=models.CASCADE,related_name='batch_school',null=True)
    equipment_quantities = models.IntegerField(default=1, verbose_name='Quantities')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name = 'Batch'
        verbose_name_plural = 'Batches'

    def __str__(self):
        return f"{self.category} {self.serial_no} {self.equipment_quantities}"



class Allocation(models.Model):
    student = models.ForeignKey(User, limit_choices_to={'user_type':'Student'},on_delete=models.CASCADE,
        null=True,blank=True,related_name='equipment_allocated')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,blank=True,related_name='allocations')
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,null=True,blank=True,related_name='allocations')
    quantity = models.IntegerField(default=0)
    allocated_by = models.ForeignKey(User, on_delete=models.PROTECT,related_name='equipment_allocations')
    is_returned = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        if self.student:
            return f"{self.student} {self.student.course} {self.allocated_by}"
        else:
            return f"{self.course.name} {self.allocated_by.first_name}"

    def save(self, *args, **kwargs):
        if self.equipment:
            self.equipment.is_allocated = True

        if self.equipment and self.is_returned:
            self.equipment.is_allocated = False

        # if self.equipment.batch:
        #     if self.quantity < self.equipment.batch.equipment_quantities:
        #         raise ValidationError(f"Amount is higher than available quantities, please allocate a lower quantity.")

        super().save(*args, **kwargs)
