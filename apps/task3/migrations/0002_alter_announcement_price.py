# Generated by Django 4.2 on 2023-04-11 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]