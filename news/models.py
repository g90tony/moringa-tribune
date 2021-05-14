from django.db import models
from django.db.models.base import Model

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name']
        
