# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_notedatamodel_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='notedatamodel',
            name='delete_marker',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notedatamodel',
            name='thread',
            field=models.ForeignKey(related_name='datas', to='notebook.NoteThread'),
        ),
    ]
