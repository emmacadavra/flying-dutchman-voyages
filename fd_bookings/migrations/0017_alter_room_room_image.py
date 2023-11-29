# Generated by Django 3.2.23 on 2023-11-29 15:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fd_bookings', '0016_alter_room_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
