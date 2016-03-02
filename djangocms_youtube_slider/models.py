# -*- coding: utf-8 -*-
from __future__ import absolute_import

import urlparse

from django.db import models
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin

YOUTUBE_RSS_PLAYLIST_V3 = u"https://www.youtube.com/feeds/videos.xml?playlist_id={}"


class YoutubeVideoContainer(CMSPlugin):
    description = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Description"))

    def copy_relations(self, old_instance):
        for slide in old_instance.slides.all():
            slide.id = slide.pk = None
            slide.slider = self
            slide.save(force_insert=True)

    def __unicode__(self):
        return u"{} ({} video)".format(self.description, self.slides.count())

    class Meta:
        db_table = 'cmsplugin_youtubevideocontainer'


class YoutubeVideoSlide(CMSPlugin):
    slider = models.ForeignKey(YoutubeVideoContainer, related_name='slides', verbose_name=_("Slider"))
    video_link = models.CharField(max_length=200, null=False, blank=False)
    order = models.PositiveIntegerField(default=1)

    def video_id(self, video_url=None):
        """
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        """
        # http://stackoverflow.com/questions/4356538/how-can-i-extract-video-id-from-youtubes-link-in-python
        video_url = self.video_link if video_url is None else video_url
        if video_url:
            query = urlparse.urlparse(video_url)
            if query.hostname == 'youtu.be':
                return query.path[1:]
            if query.hostname in ('www.youtube.com', 'youtube.com'):
                if query.path == '/watch':
                    p = urlparse.parse_qs(query.query)
                    return p.get('v', 'X')[0]
                if query.path[:7] == '/embed/':
                    return query.path.split('/')[2]
                if query.path[:3] == '/v/':
                    return query.path.split('/')[2]
        return None

    def video_thumb(self, video_id=None):
        video_id = self.video_id() if video_id is None else video_id
        if video_id:
            return u"http://img.youtube.com/vi/{}/default.jpg".format(video_id)

    @property
    def is_playlist(self):
        if urlparse.urlparse(self.video_link).path == '/playlist':
            return True
        return False

    @property
    def playlist_link(self):
        if self.is_playlist:
            return YOUTUBE_RSS_PLAYLIST_V3.format(
                urlparse.parse_qs(urlparse.urlparse(self.video_link).query).get('list', 'X')[0]
            )
        return ""

    def save(self, no_signals=False, *args, **kwargs):
        if not self.id:
            self.order = (YoutubeVideoSlide.objects.all().aggregate(Max('order')).get('order__max') or 1) + 1
        super(YoutubeVideoSlide, self).save(no_signals, *args, **kwargs)

    def __unicode__(self):
        return u"Video/Playlist {}".format(self.pk)

    class Meta:
        ordering = ('order',)
        db_table = 'cmsplugin_youtubevideoslide'

