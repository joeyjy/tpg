# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('start_time', models.DateTimeField(verbose_name='Start Time')),
                ('expired_time', models.DateTimeField(verbose_name='Expired Time')),
            ],
            options={
                'verbose_name': 'Package',
            },
        ),
    ]
