# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('content', models.TextField(default=b'', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('uid', models.CharField(max_length=64)),
                ('article', models.ForeignKey(related_name='attachments', to='notebook.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('description', models.TextField(default=b'', null=True, blank=True)),
                ('parent', models.ForeignKey(related_name='sub_forums', default=None, blank=True, to='notebook.Forum', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ForumGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ForumUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('password', models.Field(max_length=255)),
                ('group', models.ForeignKey(related_name='users', to='notebook.ForumGroup')),
            ],
        ),
        migrations.CreateModel(
            name='NoteDataModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('content', models.TextField(default=b'', null=True, blank=True)),
                ('delete_marker', models.BooleanField(default=False)),
                ('content_type', models.CharField(default=b'MA', max_length=2, choices=[(b'MA', b'MAIN'), (b'RE', b'REPLY')])),
            ],
        ),
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
        migrations.AddField(
            model_name='notedatamodel',
            name='thread',
            field=models.ForeignKey(related_name='datas', to='notebook.NoteThread'),
        ),
        migrations.AddField(
            model_name='article',
            name='forum',
            field=models.ForeignKey(related_name='articles', to='notebook.Forum'),
        ),
        migrations.AddField(
            model_name='article',
            name='reply_to',
            field=models.ForeignKey(related_name='articles', default=None, blank=True, to='notebook.Article', null=True),
        ),
    ]
