# Generated by Django 2.1.4 on 2019-04-18 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190418_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 14, 55, 31, 116439, tzinfo=utc)),
        ),
    ]