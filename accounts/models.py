from django.db import models

# Create your models here.

class logn(models.Model):
    user_name=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    def __str__(self):
        return self.user_name

        
class regs(models.Model):
    user_name=models.CharField(max_length=150)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=150)
    def __str__(self):
        return self.user_name

