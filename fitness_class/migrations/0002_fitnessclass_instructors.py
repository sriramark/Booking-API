# Generated by Django 5.0.6 on 2025-06-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_class', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessclass',
            name='instructors',
            field=models.ManyToManyField(help_text='Instructors who can teach this class', related_name='fitness_classes', to='fitness_class.instructor'),
        ),
    ]
