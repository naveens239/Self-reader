# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passage_name', models.CharField(unique=True, max_length=50)),
                ('passage', models.TextField()),
                ('words', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(unique=True, max_length=150)),
                ('time_per_word', models.TextField()),
                ('passage_read', models.ForeignKey(to='pacereader.Passage')),
            ],
        ),
    ]
