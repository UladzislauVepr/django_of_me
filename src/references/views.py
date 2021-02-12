from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from references.models import Book #импорт класса объекто


def books_list(request):
    books=Book.objects.all()   #выводим первый экземпляр объектов из класса
    #exz='The first from our books is: \"{book.name}\",<br> with number  <{book.pk}>.'
    #    Wich was created by {book.authors} and<br>
    #    this book has the following content:<br>
    #    {book.description}"""
    #return HttpResponse(exz)
    #return HttpResponse(f'The first from our books is:<br> "{book.name}",<br> with number  <{book.pk}>,<br>Wich was created by {book.authors} and<br>this book has the following content:<br>{book.description}')
    context={"books":books}
    return render(request, template_name="index.html", context=context)

def book_detail(request, pk):
    book=Book.objects.get(pk=pk)
    context={"object":book}
    return render(request, template_name="detail.html", context=context)

def book_delete(request, pk):
    book=Book.objects.get(pk=pk)
    message = f'Book "{ book.name }" has just been deleted!!!'
    book.delete()
    context={"message":message}
    return render(request, template_name="delete.html", context=context)
