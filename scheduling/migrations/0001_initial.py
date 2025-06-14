# Generated by Django 5.0.6 on 2025-06-10 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fitness_class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the current sesssion', max_length=200)),
                ('datetime', models.DateTimeField()),
                ('total_available_slots', models.PositiveIntegerField()),
                ('fitness_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_classes', to='fitness_class.fitnessclass')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classes', to='fitness_class.instructor')),
            ],
            options={
                'ordering': ['datetime'],
                'unique_together': {('instructor', 'datetime')},
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('scheduled_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='scheduling.scheduledclass')),
            ],
            options={
                'ordering': ['booking_time'],
                'unique_together': {('scheduled_class', 'email')},
            },
        ),
    ]
