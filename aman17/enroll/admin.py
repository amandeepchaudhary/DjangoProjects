from django.contrib import admin
from enroll.models import Student

# Register your models here.


# Using Decorator
@admin.register(Student)
# For table form we have to make a modeladmin class here
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuid', 'stuname', 'stuemail', 'stuphone')


# admin.site.register(Student, StudentAdmin)