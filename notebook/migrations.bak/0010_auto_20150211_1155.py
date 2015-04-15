# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0009_forumgroup_forumuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumuser',
            name='password',
            field=models.Field(default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='article',
            old_name='parent',
            new_name='reply_to',
        ),
    ]
