# Generated by Django 4.0.6 on 2023-03-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_sell', '0009_products_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prod_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
