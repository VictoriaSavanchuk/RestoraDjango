# Generated by Django 4.2.4 on 2023-11-04 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=None, max_length=15, unique=True, validators=[django.core.validators.RegexValidator(regex='^(\\+375|80)-(29|25|44|33)-(\\d{3})(\\d{2})(\\d{2})$')], verbose_name='Телефон'),
        ),
    ]
