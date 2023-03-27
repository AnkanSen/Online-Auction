from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Products(models.Model):
    id=models.AutoField(primary_key=True,null=False,blank=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    price=models.IntegerField(blank=False,null=False)
    category=models.CharField(max_length=250,null=False,blank=False)
    latest_bid=models.CharField(max_length=250,null=True,blank=True)
    last_date=models.DateField(auto_now_add=False,auto_now=False,null=False,blank=False)
    is_active=models.BooleanField(default=True,null=False,blank=True)
    prod_image=models.ImageField(null=True,blank=True,upload_to="images/")
