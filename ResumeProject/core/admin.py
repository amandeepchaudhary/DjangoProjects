from django.contrib import admin
from core.models import Visitor
# Register your models here.

@admin.register(Visitor)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'visitor_name', 'email', 'subject', 'message']