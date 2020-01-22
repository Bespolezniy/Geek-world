# Generated by Django 3.0.2 on 2020-01-18 13:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200117_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='new',
            options={'ordering': ['-posted'], 'verbose_name': 'new', 'verbose_name_plural': 'news'},
        ),
        migrations.RemoveField(
            model_name='new',
            name='date',
        ),
        migrations.AddField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 18, 16, 48, 16, 15835), verbose_name='Published'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=100, unique_for_date='posted', verbose_name='New title'),
        ),
    ]
