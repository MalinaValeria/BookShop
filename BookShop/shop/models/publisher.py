from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название издательства')

    def __str__(self):
        return self.name