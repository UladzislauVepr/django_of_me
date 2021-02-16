"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from references.views import home_page  забираем определение визуальной страницы, "home_page" - это функция, ниже её переаём
from references import views #запись для строки 25, "Внимательно смотрите, что импортируете и как обращаетесь к импортированным объектам и модулям"(с)

urlpatterns = [
    path('admin/', admin.site.urls), #http://127.0.0.1:8000/admin/
    #path('', home_page), #http://127.0.0.1:8000/ --первонвчальная главная страница
    path('books/', views.books_list, name="book-list"), #http://127.0.0.1:8000/books --cтраница c таблицей -- !!!внимательно см путь, его окончание
    path('books-cbv/', views.BooksList.as_view(), name="book-list-cbv"),    #делаем классовым методом
    path('books/<int:pk>/', views.book_detail, name="book-detail"),
    path('books-cbv/<int:pk>/', views.BookDetail.as_view(), name="book-detail-cbv"),     #делаем классовым методом
    path('book-delete/<int:pk>/', views.book_delete, name="book-delete"),   #прописывает удаление столбца
    path('book-delete-cbv/<int:pk>/', views.BookDelete.as_view(), name="book-delete-cbv"),
    path('book-create/', views.book_create, name="book-create"), #
    path('book-update/<int:pk>/', views.book_update, name="book-update")   #прописывает обновление книги
    # URL
    # GET
    # POST 
]
