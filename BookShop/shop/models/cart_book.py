from django.db import models


class CartBook(models.Model):
    cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE)
    book = models.ForeignKey('shop.BookInfo', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
