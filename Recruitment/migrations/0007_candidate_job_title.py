# Generated by Django 3.0.8 on 2020-09-03 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruitment', '0006_auto_20200903_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='job_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
