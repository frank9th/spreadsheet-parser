# Generated by Django 3.0.7 on 2020-06-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_parser', '0002_excelsavermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='MDA_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='budget',
            name='project_recipient_name',
            field=models.CharField(max_length=120),
        ),
    ]