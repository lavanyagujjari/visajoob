from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers

# Create your models here.

class UserProfileInfo(AbstractUser):
    id = models.CharField(max_length=10, null = False,primary_key=True)
    username = models.CharField(max_length=20, null = True)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    mobileno = models.CharField(max_length=10)
    userflag = models.CharField(max_length=2)
    admin_status = models.CharField(max_length=2)
    is_staff = models.CharField(max_length=2)
    class Meta:
         db_table = "user"
	#user = models.OneToOneField(User,on_delete=models.CASCADE)
	#portfolio_site = models.URLField(blank=True)
	#profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

class login_det(models.Model):
    dept_name = models.CharField(max_length=20, null = True)
    dept_code = models.CharField(max_length=25)
    mobile = models.CharField(max_length=25)
    class Meta:
         db_table = "DEPARTMENT_M"

class data_form(models.Model):
    name = models.CharField(max_length=20, null = False)
    Mobile = models.CharField(max_length=25, null = False)
    area = models.CharField(max_length=25, null = False)
    class Meta:
         db_table = "mobile_reg"
         managed = False

#def __str__(self):
#  return self.user.username

class rest_form(models.Model):
    #id=models.CharField(max_length=20, null = false)
    name = models.CharField(max_length=20, null = False)
    mobile = models.CharField(max_length=25, null = False)
    area = models.CharField(max_length=25, null = False)
    class Meta:
         db_table = "mobile_reg"
         ordering = ['-id']
         managed = False