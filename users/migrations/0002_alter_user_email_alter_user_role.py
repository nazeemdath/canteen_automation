# Generated by Django 5.1.5 on 2025-02-13 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('faculty', 'Faculty'), ('admin', 'Admin')], max_length=50),
        ),
    ]
