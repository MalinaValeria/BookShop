from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название книги')
    authors = models.ManyToManyField('shop.Author', related_name='books', through='BookAuthor', verbose_name='Авторы')
    category = models.ForeignKey('shop.Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.authors.all()} {self.name}'
