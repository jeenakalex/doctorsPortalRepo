from django.db import models

# Create your models here.
class TblUser(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='',null=False)
    age = models.IntegerField(default='',null=False)
    email = models.CharField(max_length=100,default='',null=False)
    mobile = models.IntegerField(default='',null=False)
    password = models.CharField(max_length=100,default='',null=False)
    dattimeCreated = models.DateTimeField()
    intLastAction =  models.IntegerField(default='',null=False)

class TblPatientDetails(models.Model):
    patientId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='',null=False)
    age = models.IntegerField(default='',null=False)
    mobile = models.IntegerField(default='',null=False)
    place = models.CharField(max_length=100,default='',null=False)
    intCreatedUserId =  models.IntegerField(default='',null=False)
    dattimeCreated = models.DateTimeField()
    intLastAction =  models.IntegerField(default='',null=False)    