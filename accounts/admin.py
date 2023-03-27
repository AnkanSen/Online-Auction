from django.contrib import admin
from . import models
from django.contrib.admin.sites import site

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','user','balance')

admin.site.register(models.Profile,ProfileAdmin)