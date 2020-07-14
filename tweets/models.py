from django.db import models

# Create your models here.

class Tweet(models.Model):
    content = models.TextField()
    image = models.FileField(upload_to='images/', blank=True, null=True)
    