from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название книги')
    authors = models.ManyToManyField('shop.Author', through='shop.BookAuthor', related_name='books', verbose_name='Авторы книги')
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.authors.all()} {self.name}'
