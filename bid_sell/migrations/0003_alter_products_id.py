# Generated by Django 4.0.6 on 2023-03-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_sell', '0002_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
