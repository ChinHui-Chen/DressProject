# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SkirtType'
        db.create_table(u'dress_pool_skirttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skirtTypeName', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dress_pool', ['SkirtType'])

        # Adding model 'DressType'
        db.create_table(u'dress_pool_dresstype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dressTypeName', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dress_pool', ['DressType'])

        # Adding model 'Purpose'
        db.create_table(u'dress_pool_purpose', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('purposeName', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dress_pool', ['Purpose'])

        # Adding model 'Dress'
        db.create_table(u'dress_pool_dress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skirtType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dress_pool.SkirtType'])),
            ('dressType', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dress_pool.DressType'])),
            ('purpose', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dress_pool.Purpose'])),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('amount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rent', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('additional', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dress_pool', ['Dress'])

        # Adding model 'RentRecord'
        db.create_table(u'dress_pool_rentrecord', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dress', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dress_pool.Dress'])),
            ('rentCount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rentDate', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'dress_pool', ['RentRecord'])


    def backwards(self, orm):
        # Deleting model 'SkirtType'
        db.delete_table(u'dress_pool_skirttype')

        # Deleting model 'DressType'
        db.delete_table(u'dress_pool_dresstype')

        # Deleting model 'Purpose'
        db.delete_table(u'dress_pool_purpose')

        # Deleting model 'Dress'
        db.delete_table(u'dress_pool_dress')

        # Deleting model 'RentRecord'
        db.delete_table(u'dress_pool_rentrecord')


    models = {
        u'dress_pool.dress': {
            'Meta': {'object_name': 'Dress'},
            'additional': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'amount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'dressType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dress_pool.DressType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'purpose': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dress_pool.Purpose']"}),
            'rent': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'skirtType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dress_pool.SkirtType']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'dress_pool.dresstype': {
            'Meta': {'object_name': 'DressType'},
            'dressTypeName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'dress_pool.purpose': {
            'Meta': {'object_name': 'Purpose'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purposeName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'dress_pool.rentrecord': {
            'Meta': {'object_name': 'RentRecord'},
            'dress': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dress_pool.Dress']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rentCount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rentDate': ('django.db.models.fields.DateField', [], {})
        },
        u'dress_pool.skirttype': {
            'Meta': {'object_name': 'SkirtType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skirtTypeName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dress_pool']