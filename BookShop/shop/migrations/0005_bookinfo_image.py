# Generated by Django 3.2 on 2024-04-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_bookinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers'),
        ),
    ]
