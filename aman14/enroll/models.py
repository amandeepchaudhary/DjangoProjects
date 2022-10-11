from django.db import models

# Create your models here.
class students(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=90)
    stuclass = models.IntegerField()
    stumail = models.EmailField(default='Email is not given')
    stuphone = models.BigIntegerField()