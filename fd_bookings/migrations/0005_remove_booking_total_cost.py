# Generated by Django 3.2.23 on 2023-11-12 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fd_bookings', '0004_room_room_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='total_cost',
        ),
    ]