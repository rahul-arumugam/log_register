# Generated by Django 4.1.7 on 2023-02-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_alter_employees_intime_alter_employees_outtime'),
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