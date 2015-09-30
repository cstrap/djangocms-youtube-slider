# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys
from collections import namedtuple
from io import BytesIO
import xml.etree.cElementTree as ET

import requests
from django.contrib.admin import StackedInline
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from adminsortable2.admin import SortableInlineAdminMixin

from .models import YoutubeVideoContainer, YoutubeVideoSlide


class YoutubeSlideInline(SortableInlineAdminMixin, StackedInline):
    model = YoutubeVideoSlide
    fk_name = 'slider'
    extra = 1
    ordering = ('order',)


class YoutubeSliderPlugin(CMSPluginBase):
    admin_preview = False
    inlines = [YoutubeSlideInline, ]
    model = YoutubeVideoContainer
    name = "Youtube Video Slider"
    render_template = "cms/plugin/youtube_slider.html"

    def render(self, context, instance, placeholder):

        context = super(YoutubeSliderPlugin, self).render(context, instance, placeholder)

        slides = []
        YoutubeVideo = namedtuple('YoutubeVideo', 'pos, video_id, video_thumb')
        pos = (i for i in xrange(0, sys.maxsize))

        for slide in instance.slides.all().order_by('order'):
            if slide.is_playlist:
                response = requests.get(slide.playlist_link)
                if response.status_code == 200:
                    xml = BytesIO(response.content)
                    xml.flush()
                    xml.seek(0)
                    for entry in ET.parse(xml).getroot().findall(u"{http://www.w3.org/2005/Atom}entry"):
                        video_id = slide.video_id(
                            entry.findall(u"{http://www.w3.org/2005/Atom}link")[0].attrib.get('href', 'X'))
                        slides.append(YoutubeVideo(pos.next(), video_id, slide.video_thumb(video_id)))
            else:
                slides.append(YoutubeVideo(pos.next(), slide.video_id, slide.video_thumb))

        context.update({
            'slides': slides,
            'description': instance.description.strip()
        })

        return context


plugin_pool.register_plugin(YoutubeSliderPlugin)
