# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'YoutubeVideoContainer'
        db.create_table(u'cmsplugin_youtubevideocontainer', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'djangocms_youtube_slider', ['YoutubeVideoContainer'])

        # Adding model 'YoutubeVideoSlide'
        db.create_table(u'cmsplugin_youtubevideoslide', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('slider', self.gf('django.db.models.fields.related.ForeignKey')(related_name='slides', to=orm['djangocms_youtube_slider.YoutubeVideoContainer'])),
            ('video_link', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'djangocms_youtube_slider', ['YoutubeVideoSlide'])

    def backwards(self, orm):
        # Deleting model 'YoutubeVideoContainer'
        db.delete_table(u'cmsplugin_youtubevideocontainer')

        # Deleting model 'YoutubeVideoSlide'
        db.delete_table(u'cmsplugin_youtubevideoslide')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'djangocms_youtube_slider.youtubevideocontainer': {
            'Meta': {'object_name': 'YoutubeVideoContainer', 'db_table': "u'cmsplugin_youtubevideocontainer'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'djangocms_youtube_slider.youtubevideoslide': {
            'Meta': {'object_name': 'YoutubeVideoSlide', 'db_table': "u'cmsplugin_youtubevideoslide'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['djangocms_youtube_slider.YoutubeVideoContainer']"}),
            'video_link': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['djangocms_youtube_slider']