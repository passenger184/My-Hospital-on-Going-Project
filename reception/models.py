from django.db import models

# Create your models here.


class Patient(models.Model):
    GENDER = (
        ('Male', 'male'), 
        ('Female', 'female'),
    )
    
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    contact_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=200, choices=GENDER)
    blood_group = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    any_major_disease = models.CharField(max_length=200, null=True)
    
    
    def __str__(self):
        return self.name