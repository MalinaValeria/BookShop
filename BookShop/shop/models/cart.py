from django.db import models


class Cart(models.Model):
    user = models.OneToOneField('account.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    books = models.ManyToManyField('shop.BookInfo', through='shop.CartBook', verbose_name='Книги', related_name='cart')
