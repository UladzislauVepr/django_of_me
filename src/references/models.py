from django.db import models

# Create your models here.

class Book(models.Model):
    #id/pk -- create autimatically
    authors = models.CharField(
        verbose_name="autors of book",
        max_length=100,
        null=True,
        blank=True)
    name = models.CharField(
        verbose_name="name of book",
        max_length=100,
        null=False,
        blank=False)
    description = models.TextField(
        verbose_name="book's description",
        null=True,
        blank=True)
    #cover_photo
    #price
    #series
    #genre
    #year_of_publishing

    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.authors} {self.name} {self.description}"


class Customers(models.Model):
    name = models.CharField(
        verbose_name="name of customer",
        max_length=25,
        null=True,
        blank=True)
    phone = models.CharField(
        verbose_name="phone of customer",
        max_length=11,
        null=True,
        blank=True)
    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.name} {self.phone}"
       
 
