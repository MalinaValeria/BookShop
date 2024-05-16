from django.db import models


class OrderStatus(models.TextChoices):
    CREATED = 'created', 'Создан'
    PROCESSING = 'processing', 'В обработке'
    DELIVERY = 'delivery', 'Доставляется'
    DELIVERED = 'delivered', 'Доставлен'
    CANCELLED = 'cancelled', 'Отменен'


class Order(models.Model):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    status = models.BooleanField(default=OrderStatus.CREATED, choices=OrderStatus.choices, verbose_name='Статус')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    books = models.ManyToManyField('shop.BookInfo', through='shop.OrderBook', verbose_name='Книги', related_name='orders')