# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='description',
            field=models.TextField(max_length=256, null=True, blank=True),
        ),
    ]
