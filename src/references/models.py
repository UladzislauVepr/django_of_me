from django.db import models

# Create your models here.

class Authors(models.Model):               #формируем модель для базы данных
    authors = models.CharField(
        verbose_name="autors of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="autors of book",
        default='---')
    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.authors}"

class Series(models.Model):
    series= models.CharField(
        verbose_name="series of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="series of book",
        default='---')
    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.series}"

class Genre(models.Model):
    genre= models.CharField(
        verbose_name="genre of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="genre of book",
        default='---')
    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.genre}"

class Publishhouse(models.Model):
    publishhouse= models.CharField(
        verbose_name="publishing house of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="publishing house of book",
        default='---')
    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.publishhouse}"

class Book(models.Model):               #формируем модель для базы данных
    #id/pk -- create autimatically
    authors = models.ForeignKey(
        'references.Authors',
        verbose_name="autors of book",
        help_text="autors of book",
        on_delete=models.PROTECT)
    name = models.CharField(
        verbose_name="name of book",
        max_length=100,
        null=False,
        blank=False)
    description = models.TextField(
        verbose_name="book's description",
        null=True,
        blank=True)
    cover_photo= models.ImageField(
        verbose_name="cover's book foto",
        help_text="book's foto",
        default='---'        )
    price= models.DecimalField(
        verbose_name="cost of book",
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="cost of book",
        default='---')
    series= models.ForeignKey(
        'references.Series',
        on_delete=models.PROTECT,
        verbose_name="series of book")
    genre= models.CharField(
        verbose_name="genre of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="genre of book",
        default='---')
    yearpublishing= models.DecimalField(
        verbose_name="year of book relise",
        max_digits=4,
        decimal_places=0,
        null=True,
        blank=True,
        help_text="year of book relise",
        default='---')
    quantitypage= models.DecimalField(
        verbose_name="quantity pages",
        max_digits=4,
        decimal_places=0,
        null=True,
        blank=True,
        help_text="quantity pages",
        default='---')
    binding= models.CharField(
        verbose_name="binding (cover) of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="binding (cover) of book",
        default='---')
    sizeform= models.CharField(
        verbose_name="size (format) of book",
        max_length=2,
        null=True,
        blank=True,
        help_text="size (format) of book",
        default='---')
    isbn= models.CharField(
        verbose_name="ISBN of book",
        max_length=16,
        null=True,
        blank=True,
        help_text="ISBN of book",
        default='---')
    weightofcopy= models.DecimalField(
        verbose_name="weight of book copy",
        max_digits=5,
        decimal_places=0,
        null=True,
        blank=True,
        help_text="weight of book copy",
        default='---')
    ageslimit= models.DecimalField(
        verbose_name="limit of readers age",
        max_digits=2,
        decimal_places=0,
        null=True,
        blank=True,
        help_text="limit of readers age",
        default='---')
    publishhouse= models.CharField(
        verbose_name="publishing house of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="publishing house of book",
        default='---')
    qyantitystock= models.DecimalField(
        verbose_name="quantity of books copy in stock",
        max_digits=4,
        decimal_places=0,
        null=True,
        blank=True,
        help_text="quantity of books copy in stock",
        default='---')
    stateofactivity= models.CharField(
        verbose_name="state of activity",
        max_length=10,
        null=True,
        blank=True,
        help_text="state of activity",
        default='---')
    rating= models.CharField(
        verbose_name="autors of book",
        max_length=50,
        null=True,
        blank=True,
        help_text="autors of book",
        default='---')
    created = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        verbose_name="data of record creating",
        help_text="data of record creating")
    updated= models.DateTimeField(
        auto_now_add=False,
        auto_now=True,
        verbose_name="data of record updating",
        help_text="data of record updating")
    def __str__(self):  #здесь определяется порядок вывода  инфы, можно брать из других моделей, см.видео от 29.01/2ч17мин
        return f"{self.authors} {self.name} {self.description} {self.created} {self.updated}"



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
       
 
