# Generated by Django 4.0.6 on 2023-03-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid_sell', '0006_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='latest_bid',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
