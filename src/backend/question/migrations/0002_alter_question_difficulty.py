# Generated by Django 4.1.4 on 2024-03-19 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.IntegerField(default=100, help_text='percentage of difficulty'),
        ),
    ]
