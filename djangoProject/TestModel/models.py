from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50,null=True, blank=True)
