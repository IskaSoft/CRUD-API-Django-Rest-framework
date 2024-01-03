from django.db import models

# Create your models here.
class Task(models.Model):
    fullname = models.CharField(max_length=255, null=False, blank=False)
    lastname = models.CharField(max_length=255,null=False,blank=False)
    price = models.IntegerField()

    def __str__(self):
        return self.fullname
    
