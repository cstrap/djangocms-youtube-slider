# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_auto_20150907_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideoContainer',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='YoutubeVideoSlide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('video_link', models.CharField(max_length=200)),
                ('order', models.PositiveIntegerField(default=1)),
                ('slider', models.ForeignKey(related_name='slides', verbose_name='Slider', to='djangocms_youtube_slider.YoutubeVideoContainer')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=('cms.cmsplugin',),
        ),
    ]
