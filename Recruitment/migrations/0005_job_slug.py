# Generated by Django 3.0.8 on 2020-09-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment', '0004_auto_20200901_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, help_text='A short description of the Job', max_length=100, null=True, unique=True),
        ),
    ]
