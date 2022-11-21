from django.db import models

# Create your models here.
class contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Email_name=models.CharField(max_length=100)
    Conatct_Number=models.CharField(max_length=100)
    Address=models.TextField(max_length=100)
    