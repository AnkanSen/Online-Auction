# Generated by Django 4.0.6 on 2023-03-16 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bid_sell', '0005_alter_products_user_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]