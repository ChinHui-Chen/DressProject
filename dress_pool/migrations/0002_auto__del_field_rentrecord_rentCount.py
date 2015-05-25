# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RentRecord.rentCount'
        db.delete_column(u'dress_pool_rentrecord', 'rentCount')


    def backwards(self, orm):
        # Adding field 'RentRecord.rentCount'
        db.add_column(u'dress_pool_rentrecord', 'rentCount',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


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
            'rentDate': ('django.db.models.fields.DateField', [], {})
        },
        u'dress_pool.skirttype': {
            'Meta': {'object_name': 'SkirtType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skirtTypeName': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dress_pool']