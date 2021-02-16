from django.shortcuts import render


# Create your views here.
from django.http import HttpResponseRedirect
from references.models import Book #импорт класса объектов
from django.urls import reverse
from . import forms
from django.views.generic import DetailView, ListView, DeleteView     #импортируем библиотеки для работы классовым методом


def books_list(request):
    books=Book.objects.all()   #выводим первый экземпляр объектов из класса
    context={"books":books}
    return render(request, template_name="index.html", context=context)

class BooksList(ListView):
    model=Book

def book_detail(request, pk):
    book=Book.objects.get(pk=pk)
    context={"object":book}
    return render(request, template_name="detail.html", context=context)

class BookDetail(DetailView):
    model=Book


def book_delete(request, pk):
    book=Book.objects.get(pk=pk)
    message = f'Book "{ book.name }" has just been deleted!!!'
    book.delete()
    context={"message":message}
    return render(request, template_name="delete.html", context=context)

class BookDelete(DeleteView):
    success_url='/books-cbv/'
    model=Book

def book_create(request):
    context={}
    if request.method == "POST":
        form=forms.BookForm(request.POST)
        if form.is_valid():
            book=form.save()
            return HttpResponseRedirect(reverse('book-detail', kwargs={'pk':book.pk}))
        else:
            context['form']=form
    else:
        context['form']=forms.BookForm()
    return render(request, template_name="create.html", context=context)

def book_update(request, pk):
    context={}
    if request.method == "GET":
        book=Book.objects.get(pk=pk)
        context={'book':book}
    elif request.method == "POST":
        name=request.POST.get('name')
        authors=request.POST.get('authors')
        description=request.POST.get('description')
        #book=Book.objects.create(name=name, authors=authors, description=description)
        book=Book.objects.get(pk=pk)
        book.name=name
        book.authors=authors
        book.description=description
        book.save()     # это тоже важная строка
        return HttpResponseRedirect(reverse('book-detail', kwargs={'pk':book.pk})) #по этой команде происходит отрисовка
    return render(request, template_name="update.html", context=context)
