# Generated by Django 2.1.4 on 2019-04-18 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190418_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 14, 50, 6, 596533, tzinfo=utc)),
        ),
    ]
