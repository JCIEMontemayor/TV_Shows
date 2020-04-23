from django.db import models

class Shows(models.Model):
    title = models.TextField()
    network = models.TextField()
    release = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# Create your models here.
