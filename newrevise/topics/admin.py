from django.contrib import admin
from topics.models import dataModels

# Register your models here.
@admin.register(dataModels)
class dataAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']