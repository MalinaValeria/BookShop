from django.db import models


class BookAuthor(models.Model):
    book = models.ForeignKey('shop.Book', on_delete=models.CASCADE)
    author = models.ForeignKey('shop.Author', on_delete=models.CASCADE)
