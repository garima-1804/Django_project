from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100,blank=False,null=False)
    description=models.CharField(max_length=150,blank=False,null=False)
    status=models.CharField(max_length=10,blank=False,null=False)
    duedate= models.CharField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.title
    
    