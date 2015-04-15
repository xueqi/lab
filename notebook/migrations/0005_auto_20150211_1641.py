# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0004_article_main_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notedatamodel',
            name='thread',
        ),
        migrations.DeleteModel(
            name='NoteDataModel',
        ),
        migrations.DeleteModel(
            name='NoteThread',
        ),
    ]
