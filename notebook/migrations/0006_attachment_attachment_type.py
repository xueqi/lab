# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_auto_20150211_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='attachment_type',
            field=models.CharField(default=b'unknown', max_length=255),
        ),
    ]
