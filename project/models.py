
from django.db import models

class project(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField()
    created_at = models.TimeField(auto_now_add=True)