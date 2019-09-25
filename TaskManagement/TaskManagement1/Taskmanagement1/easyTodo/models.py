


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)


class Superuser(models.Model):
    Mainuser = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Manager(models.Model):
     Manager = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Employee(models.Model):
     Employee = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Tasks(models.Models):
    Taskname = models.CharField(max_length=30)
    Taskexp = models.CharField(max_length=100)
    Taskdate = models.DateField()


