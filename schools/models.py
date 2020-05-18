from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class School(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.department}"

class Lab(models.Model):
    name = models.CharField(max_length=255)
    school = models.ManyToManyField(School)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.school}"

class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    school = models.ForeignKey(School,on_delete=models.PROTECT)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name