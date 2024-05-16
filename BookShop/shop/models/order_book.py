from django.db import models


class OrderBook(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    book = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=0, max_digits=6)
