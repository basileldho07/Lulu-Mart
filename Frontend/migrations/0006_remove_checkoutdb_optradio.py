# Generated by Django 4.2.6 on 2024-01-03 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Frontend', '0005_checkoutdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutdb',
            name='optradio',
        ),
    ]