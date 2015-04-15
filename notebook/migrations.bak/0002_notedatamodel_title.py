# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notedatamodel',
            name='title',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
