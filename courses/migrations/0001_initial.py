# Generated by Django 5.1.3 on 2024-12-28 11:44

import courses.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name_fa', models.CharField(max_length=255, verbose_name='Course Name (Persian)')),
                ('course_name_en', models.CharField(max_length=255, verbose_name='Course Name (English)')),
                ('faculty', models.CharField(max_length=255, verbose_name='Faculty')),
                ('first_day_of_week', models.PositiveSmallIntegerField(help_text='0: Sunday, 6: Saturday', verbose_name='First Day of Week')),
                ('first_day_time', models.CharField(help_text='Format: HH:MM (24-hour format)', max_length=5, validators=[courses.models.validate_time_format], verbose_name='First Day Time')),
                ('first_day_duration', models.PositiveIntegerField(verbose_name='First Day Duration (hours)')),
                ('second_day_of_week', models.PositiveSmallIntegerField(help_text='0: Sunday, 6: Saturday', verbose_name='Second Day of Week')),
                ('second_day_time', models.CharField(help_text='Format: HH:MM (24-hour format)', max_length=5, validators=[courses.models.validate_time_format], verbose_name='Second Day Time')),
                ('second_day_duration', models.PositiveIntegerField(verbose_name='Second Day Duration (hours)')),
                ('exam_date', models.DateField(verbose_name='Exam Date')),
                ('exam_start_time', models.CharField(help_text='Format: HH:MM (24-hour format)', max_length=5, validators=[courses.models.validate_time_format], verbose_name='Exam Start Time')),
                ('exam_duration', models.PositiveIntegerField(verbose_name='Exam Duration (hours)')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='professors.professor')),
            ],
        ),
    ]
