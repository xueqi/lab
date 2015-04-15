# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0002_auto_20150114_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='cols',
            field=models.IntegerField(default=9),
        ),
        migrations.AddField(
            model_name='box',
            name='rows',
            field=models.IntegerField(default=9),
        ),
    ]
