# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0006_attachment_attachment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attachment',
            name='attachment_type',
        ),
    ]
