# Generated by Django 4.1.7 on 2023-02-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_employees_delete_newapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Intime',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Outtime',
            field=models.TextField(),
        ),
    ]
