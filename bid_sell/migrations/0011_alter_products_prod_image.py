# Generated by Django 4.0.6 on 2023-03-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_sell', '0010_products_prod_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prod_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]