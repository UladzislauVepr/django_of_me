from django.contrib import admin

# Register your models here.

from . import models

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'authors',
        'name',
        'description',
        'created',
        'updated'
    ]

class CustomersAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'phone',
    ]

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'authors']

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'series']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'genre']

class PublishhouseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'publishhouse']


 #здесь определяется регистрация инфы инфы в базе данных, см.видео от 29.01/2ч22мин
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Customers, CustomersAdmin)
admin.site.register(models.Authors, AuthorsAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publishhouse, PublishhouseAdmin)