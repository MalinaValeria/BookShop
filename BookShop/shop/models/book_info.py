from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from pytils.translit import slugify


class BookInfo(models.Model):
    class AgeLimit(models.IntegerChoices):
        ZERO = 0, '0+'
        SIX = 6, '6+'
        TWELVE = 12, '12+'
        SIXTEEN = 16, '16+'
        EIGHTEEN = 18, '18+'

    class TypeOfCover(models.TextChoices):
        HARD = 'hard', 'Твердый переплёт'
        SOFT = 'soft', 'Мягкий переплёт'
        DUTCH = 'dutch', 'Голланский переплёт'

    book = models.ForeignKey('shop.Book', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Цена')
    publisher = models.ForeignKey('shop.Publisher', on_delete=models.CASCADE)
    publication_year = models.IntegerField(validators=[MaxValueValidator(date.today().year)])
    series = models.ForeignKey('shop.Series', on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.CharField(max_length=17, verbose_name='ISBN')
    page_count = models.IntegerField()
    type_of_cover = models.CharField(max_length=5, choices=TypeOfCover.choices, verbose_name='Тип обложки')
    circulation = models.IntegerField()
    age_limit = models.IntegerField(choices=AgeLimit.choices, verbose_name='Возрастное ограничение')
    image = models.ImageField(upload_to='book_covers', null=True, blank=True)
    description = models.CharField(max_length=1000, verbose_name='Описание')
    slug = models.SlugField(unique=True, max_length=255)

    def __str__(self):
        return f'{self.book.name} ({self.publication_year})'


@receiver(post_save, sender=BookInfo)
def create_slug(instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.book.name + '-' + str(instance.id))
        instance.save()

