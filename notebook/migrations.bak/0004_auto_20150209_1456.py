# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_auto_20150209_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteThread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='notedatamodel',
            name='content',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
    ]
