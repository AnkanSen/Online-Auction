from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    balance=models.CharField(max_length=200,null=True,blank=True)
    id=models.AutoField(primary_key=True,null=False,blank=False)