# Generated by Django 3.2.23 on 2023-11-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd_bookings', '0012_alter_room_room_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='room',
            name='category',
        ),
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='Room', max_length=200),
        ),
    ]
