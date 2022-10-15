from django.db import models

# Create your models here.


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=80)
    stuemail = models.EmailField()
    stuphone = models.BigIntegerField()

    # In django admin the name is written like Student.object
    # So for better naming we apply __str__(self) funtion

    # def __str__(self):
    #     return self.stuname
    # For table form we have to create modeladmin class in admin