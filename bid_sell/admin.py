from django.contrib import admin
from . import models
from django.contrib.admin.sites import site

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','user','name','price','category','latest_bid','last_date','is_active','prod_image')

admin.site.register(models.Products,ProductAdmin)