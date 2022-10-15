from django.db import models

# Create your models here.


class Student(models.Model):
    sturoll = models.IntegerField()
    stufname = models.CharField(max_length=70)
    stulname = models.CharField(max_length=70)
    stuemail = models.EmailField()
    stuphone = models.BigIntegerField()

    def __str__(self):  # used to find which persons data is there as a heading
        return self.stufname  # used to better readability
    
    def __str__(self):  # used to find which persons data is there as a heading
        return str(self.sturoll)  # used to better readability
        # in integer we have to convert the numeric in string
