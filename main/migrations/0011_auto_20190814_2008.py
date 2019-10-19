# Generated by Django 2.2.4 on 2019-08-14 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190813_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_thumbnail',
            field=models.CharField(default='/materials/images/<django.db.models.fields.CharField>', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 14, 20, 8, 55, 176308), verbose_name='date published'),
        ),
    ]