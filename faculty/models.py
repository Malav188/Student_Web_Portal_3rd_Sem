from django.core.exceptions import ValidationError
from django.db import models
# from Student_app.models import *
from user.models import Faculty
# Create your models here.

class Faculty_Records(models.Model):
    fac_id = models.AutoField(primary_key=True,unique=True)
    email = models.EmailField(default='Enter your email here',unique=True,null=False,blank=False)
    user = models.OneToOneField(Faculty, on_delete=models.CASCADE,null=True,blank=True)
    fac_name = models.CharField(max_length=25)
    def __str__(self):
        return self.fac_name












