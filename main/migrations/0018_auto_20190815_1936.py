# Generated by Django 2.2.4 on 2019-08-15 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190815_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 19, 36, 53, 685145), verbose_name='date published'),
        ),
    ]
