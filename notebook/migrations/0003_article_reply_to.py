# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_remove_article_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='reply_to',
            field=models.ForeignKey(related_name='articles', default=None, blank=True, to='notebook.Article', null=True),
        ),
    ]
