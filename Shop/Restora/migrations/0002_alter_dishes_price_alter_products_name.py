# Generated by Django 4.2.4 on 2023-11-04 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restora', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость'),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]