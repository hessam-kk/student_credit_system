# Generated by Django 5.1.3 on 2024-12-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_faculty_customuser_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
