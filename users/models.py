from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _
from schools.models import Course

class UserAccountManager(UserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, email, password, **extra_fields)

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff status.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must have is_superuser status')

        return self._create_user(email, email, password, **extra_fields)

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
MEMBERSHIP_CHOICES = (
    ('Lab_Tech', 'Lab Technician'),
    ('Lab_Sec', 'Lab Secretary'),
    ('Student', 'Student'),
)

YEAR_OF_STUDY_CHOICES = (
    ('Select One', 'Select One'),
    ('1st Year', 'First Year'),
    ('2nd Year', 'Second Year'),
    ('3rd Year', 'Third Year'),
    ('4th Year', 'Fourth Year'),
    ('5th Year', 'Fifth Year'),
    ('6th Year', 'Sixth Year'),
)
class UserAccount(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='media/profiles', null=True)
    phone_number = models.CharField(max_length=50)
    user_type = models.CharField(max_length=30,choices=MEMBERSHIP_CHOICES,default='Lab_Tech')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    course = models.ForeignKey(Course,on_delete=models.PROTECT,null=True,blank=True)
    year_of_study = models.CharField(max_length=30, choices=YEAR_OF_STUDY_CHOICES,default="Select One",blank=True,null=True)
    staff_id = models.CharField(max_length=50, null=True,blank=True)
    registration_no = models.CharField(max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number',]

    objects = UserAccountManager()

    def __str_(self):
        return f'{self.first_name} {self.last_name} {self.phone_number}'


