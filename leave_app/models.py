from operator import mod
from django.db import models
from admins.models import Accounts
# Create your models here.

class Employe(models.Model):
    designation = models.CharField(max_length = 25)
    user = models.ForeignKey(Accounts, on_delete = models.CASCADE)


class LeaveApplication(models.Model):
    Employe = models.ForeignKey(Employe, on_delete = models.CASCADE)
    leave_starting_date = models.DateTimeField()
    leave_ending_date = models.DateTimeField()
    leave_applying_date = models.DateTimeField(auto_now_add=True)