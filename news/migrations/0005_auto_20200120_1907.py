# Generated by Django 3.0.2 on 2020-01-20 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200118_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 20, 19, 7, 51, 445720), verbose_name='Published'),
        ),
    ]
