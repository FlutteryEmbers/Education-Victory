# Generated by Django 4.1.4 on 2023-10-16 06:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_user_is_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.BigIntegerField(default=0)),
                ('qtype', models.CharField(blank=True, max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('origin_link', models.URLField(blank=True, help_text='URL for origin post', max_length=1000)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='questionsubmission',
            name='content',
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='completeness',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='qtype',
            field=models.CharField(default='coding', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionsubmission',
            name='question_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
