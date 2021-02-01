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

    def __str__(self):
        return self.authors
        return self.name
        return self.description


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
    def __str__(self):
        return self.name
        return self.phone
 
