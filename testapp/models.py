from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class fir(models.Model):
    subject=models.CharField(max_length=100)
    fir = models.TextField()
    File_Date = models.DateTimeField(default=datetime.now())
class prisoner(models.Model):
    address=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    prisoner_aadhar_no=models.BigIntegerField(primary_key=True)
    crime=models.CharField(max_length=100)
    punishment=models.CharField(max_length=100)
    date_of_entry=models.DateTimeField(default=datetime.now())
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name+':'+str(self.prisoner_aadhar_no)
class visitor(models.Model):
    name=models.CharField(max_length=50)
    visitor_aadhar_no=models.BigIntegerField(primary_key=True)
    prisoner_aadhar_no=models.ForeignKey(prisoner,on_delete=models.CASCADE)
    date_of_visit=models.DateTimeField(default=datetime.now())
    image=models.ImageField(upload_to='images/')
class allvisitors(models.Model):
    name=models.CharField(max_length=50)
    visitor_aadhar_no=models.BigIntegerField(primary_key=True)
    prisoner_aadhar_no=models.BigIntegerField()
    date_of_visit=models.DateTimeField(default=datetime.now())
    image=models.ImageField(upload_to='images/')

class guard(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    duty_hours=models.IntegerField()
    guard_aadhar_no=models.BigIntegerField(primary_key=True)
    alloted_to=models.ForeignKey(prisoner,on_delete=models.SET_NULL,null=True)
    shift=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
