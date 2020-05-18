from django.db import models
from schools.models import Lab
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    in_stock = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.name

    # def calculate_in_stock(self):
    #     in_stock = self._equipment.allocated_to.count()

class Equipment(models.Model):
    serial_no = models.CharField(max_length=80)
    allocated_to = models.ForeignKey('Allocation',related_name='equipment_allocation',on_delete=models.SET_NULL,
    null=True,blank=True)
    category = models.ForeignKey(Category,related_name='equipment_category',on_delete=models.PROTECT)
    lab = models.ForeignKey(Lab,related_name='equipment_lab',on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.serial_no} {self.category} {self.lab} {self.allocated_to}"


class Batch(models.Model):
    equipment = models.ForeignKey(Equipment,on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

class Allocation(models.Model):
    user = models.ForeignKey(User,limit_choices_to={'user_type':'Student'},on_delete=models.PROTECT,
        null=True)
    batch = models.ForeignKey(Batch,null=True,on_delete=models.PROTECT)
    allocated_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='equipment_allocated_by')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)