# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'teams_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('mlb_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('homerun', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hot', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'teams', ['Player'])

        # Adding model 'Team'
        db.create_table(u'teams_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('earnings', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'teams', ['Team'])

        # Adding M2M table for field player on 'Team'
        m2m_table_name = db.shorten_name(u'teams_team_player')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm[u'teams.team'], null=False)),
            ('player', models.ForeignKey(orm[u'teams.player'], null=False))
        ))
        db.create_unique(m2m_table_name, ['team_id', 'player_id'])

        # Adding model 'TeamMonth'
        db.create_table(u'teams_teammonth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['teams.Team'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'teams', ['TeamMonth'])

        # Adding unique constraint on 'TeamMonth', fields ['team', 'key']
        db.create_unique(u'teams_teammonth', ['team_id', 'key'])


    def backwards(self, orm):
        # Removing unique constraint on 'TeamMonth', fields ['team', 'key']
        db.delete_unique(u'teams_teammonth', ['team_id', 'key'])

        # Deleting model 'Player'
        db.delete_table(u'teams_player')

        # Deleting model 'Team'
        db.delete_table(u'teams_team')

        # Removing M2M table for field player on 'Team'
        db.delete_table(db.shorten_name(u'teams_team_player'))

        # Deleting model 'TeamMonth'
        db.delete_table(u'teams_teammonth')


    models = {
        u'teams.player': {
            'Meta': {'object_name': 'Player'},
            'homerun': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hot': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mlb_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'teams.team': {
            'Meta': {'object_name': 'Team'},
            'earnings': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'player': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['teams.Player']", 'symmetrical': 'False'})
        },
        u'teams.teammonth': {
            'Meta': {'unique_together': "(('team', 'key'),)", 'object_name': 'TeamMonth'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['teams.Team']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['teams']