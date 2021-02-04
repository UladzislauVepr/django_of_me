from django.contrib import admin

# Register your models here.

from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'authors',
        'name',
        'description'
    ]

class CustomersAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'phone',
    ]

 #здесь определяется регистрация инфы инфы в базе данных, см.видео от 29.01/2ч22мин
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Customers, CustomersAdmin)