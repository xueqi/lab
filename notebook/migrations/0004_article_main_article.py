# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_article_reply_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_article',
            field=models.BooleanField(default=True),
        ),
    ]
