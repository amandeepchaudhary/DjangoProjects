from django.db import models

# Create your models here.
class Students(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=100)
    stumail = models.EmailField(max_length=100)
    stupass = models.CharField(max_length=100)
    stuclass = models.IntegerField()
    stuPhone = models.BigIntegerField()
    comment = models.CharField(max_length=40, default='NO Comments')