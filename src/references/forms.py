from django import forms
from . import models



class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=('name', 'authors', 'description')   #здесь прописываются поля, которые мы хотим видель из файла models


    def clean(self):                    #здксь можно реализовывать любую логичу питона
        cleaned_data=super().clean()    # как, например, проверка запрещенный авторов в этом случае
        authors=cleaned_data.get('authors')

        if authors == "Лукашенко":
            self.add_error('authors','This authors is forbiden!!!')
        return cleaned_data
