# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='uid',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
