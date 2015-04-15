# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_auto_20150209_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='notedatamodel',
            name='thread',
            field=models.ForeignKey(default=1, to='notebook.NoteThread'),
            preserve_default=False,
        ),
    ]
