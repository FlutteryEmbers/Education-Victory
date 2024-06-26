# Generated by Django 4.1.4 on 2024-04-03 03:25

import common.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_user_tag_alter_userability_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=1)),
                ('problem_id', models.IntegerField(default=1)),
                ('question_id', models.IntegerField(default=1)),
                ('content', models.JSONField(default=common.models.get_default_json)),
                ('is_correct', models.BooleanField(default=False)),
                ('time_spent', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
