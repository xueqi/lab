# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_notedatamodel_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notedatamodel',
            old_name='create_date',
            new_name='update_time',
        ),
        migrations.RemoveField(
            model_name='notedatamodel',
            name='update_date',
        ),
        migrations.AddField(
            model_name='notedatamodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 9, 19, 36, 7, 638834, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
