# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('mlb_id', models.IntegerField(null=True)),
                ('homerun', models.IntegerField(default=0)),
                ('hot', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('earnings', models.IntegerField(default=0)),
                ('player', models.ManyToManyField(to='teams.Player')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMonth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=255, choices=[(b'April', b'April'), (b'May', b'May'), (b'June', b'June'), (b'July', b'July'), (b'August', b'August'), (b'September', b'September'), (b'October', b'October')])),
                ('value', models.IntegerField(default=0)),
                ('team', models.ForeignKey(to='teams.Team')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='teammonth',
            unique_together=set([('team', 'key')]),
        ),
    ]
