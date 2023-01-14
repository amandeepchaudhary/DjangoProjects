from django.db import models

# Create your models here.

class Visitor(models.Model):
    visitor_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.TextField()
    message = models.TextField()