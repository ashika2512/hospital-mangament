from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    desc=models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    
    illness=models.CharField(max_length=20)
    issue=models.TextField(max_length=100)
    doctor_name=models.CharField(max_length=20)

    def __int__(self):
        return self.illness    
