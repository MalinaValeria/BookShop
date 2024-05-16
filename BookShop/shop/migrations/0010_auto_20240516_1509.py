# Generated by Django 3.2 on 2024-05-16 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_auto_20240516_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CartBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bookinfo')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(related_name='cart', through='shop.CartBook', to='shop.BookInfo', verbose_name='Книги'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
