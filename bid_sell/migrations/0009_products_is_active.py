# Generated by Django 4.0.6 on 2023-03-18 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_sell', '0008_products_last_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]