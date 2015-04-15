# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0006_auto_20150209_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='notedatamodel',
            name='content_type',
            field=models.CharField(default=b'MA', max_length=2, choices=[(b'MA', b'MAIN'), (b'RE', b'REPLY')]),
        ),
    ]
