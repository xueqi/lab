# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_entry_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='uid',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
