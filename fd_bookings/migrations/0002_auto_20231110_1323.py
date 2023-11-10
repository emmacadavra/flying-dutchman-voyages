# Generated by Django 3.2.23 on 2023-11-10 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fd_bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('CAP', 'CAPTAIN QUARTERS'), ('OCB', 'OFFICER CABIN'), ('CRW', 'CREW BUNKS')], max_length=3)),
                ('number', models.IntegerField()),
                ('beds', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='fd_bookings.room'),
        ),
    ]
