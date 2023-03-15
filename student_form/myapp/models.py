from django.db import models

# Create your models here.

GENDER_CHOICES=(
    ('select','Select'),
    ('male', 'Male'),
    ('Female', 'Female')            
)


class Form(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    gender=models.CharField(max_length=7, choices=GENDER_CHOICES, default='select')
    college=models.CharField(max_length=250)
    email=models.EmailField()
    phone=models.BigIntegerField()

