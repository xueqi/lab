# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('box', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.CharField(max_length=10)),
                ('name', models.CharField(default=b'', max_length=255)),
                ('row', models.IntegerField(default=0)),
                ('col', models.IntegerField(default=0)),
                ('entry_type', models.CharField(default=b'DNA', max_length=256)),
                ('box', models.ForeignKey(to='box.Box')),
            ],
        ),
    ]
