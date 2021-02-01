from django.contrib import admin

# Register your models here.

from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk'
        'authors'
        'name'
        'description'
    ]

class CustomersAdmin(admin.ModelAdmin):
    list_display = [
        'pk'
        'name'
        'phone'
    ]

admin.site.register(models.Book)

admin.site.register(models.Customers)