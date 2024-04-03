from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
