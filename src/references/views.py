from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from references.models import Book #импорт класса объекто


def home_page(request):
    book=Book.objects.first()   #выводим первый экземпляр объектов из класса
    #exz='The first from our books is: \"{book.name}\",<br> with number  <{book.pk}>.'
    #    Wich was created by {book.authors} and<br>
    #    this book has the following content:<br>
    #    {book.description}"""
    #return HttpResponse(exz)
    #return HttpResponse(f'The first from our books is:<br> "{book.name}",<br> with number  <{book.pk}>,<br>Wich was created by {book.authors} and<br>this book has the following content:<br>{book.description}')
    context={"book":book}
    return render(request, template_name="index.html", context=context)