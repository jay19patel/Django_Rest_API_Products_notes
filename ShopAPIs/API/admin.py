from django.contrib import admin
from .models import *

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'id')
    
admin.site.register(Categoty)
admin.site.register(Company)
