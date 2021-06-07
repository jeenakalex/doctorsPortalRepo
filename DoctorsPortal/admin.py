from django.contrib import admin
from django.db import models

# Register your models here.
from .models import TblUser,TblPatientDetails

admin.site.register(TblUser)
admin.site.register(TblPatientDetails)