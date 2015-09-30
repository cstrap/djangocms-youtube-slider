# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.test import TestCase

from djangocms_youtube_slider.models import YoutubeVideoSlide


class YoutubeVideoSlideTest(TestCase):
    def test_video_id_empty(self):
        obj = YoutubeVideoSlide()

        self.assertIsNone(obj.video_id())

    def test_video_id_not_empty(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/watch?v=WlBiLNN1NhQ"

        self.assertEquals(u"WlBiLNN1NhQ", obj.video_id())

    def test_video_thumb_empty(self):
        obj = YoutubeVideoSlide()

        self.assertIsNone(obj.video_thumb())

    def test_video_thumb_correct_link(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/watch?v=WlBiLNN1NhQ"

        self.assertEquals(u"http://img.youtube.com/vi/WlBiLNN1NhQ/default.jpg", obj.video_thumb())

    def test_video_thumb_correct_link_long_querystring(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/watch?v=igMekDOVZk0&index=2&list=PL13631684C30573D5"

        self.assertEquals(u"http://img.youtube.com/vi/igMekDOVZk0/default.jpg", obj.video_thumb())

    def test_video_thumb_incorrect(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/watch?V=2K8_jgiNqUc"

        self.assertEquals(u"http://img.youtube.com/vi/X/default.jpg", obj.video_thumb())

    def test_video_thumb_param(self):
        obj = YoutubeVideoSlide()

        self.assertEquals(u"http://img.youtube.com/vi/2K8_jgiNqUc/default.jpg", obj.video_thumb(u"2K8_jgiNqUc"))

    def test_link_is_not_playlist(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/watch?V=2K8_jgiNqUc"

        self.assertFalse(obj.is_playlist)

    def test_link_is_playlist(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/playlist?list=PL3EThPF3sbJppGg2o65CjpeCkJ7Y2UvKn"

        self.assertTrue(obj.is_playlist)

    def test_link_is_not_playlist_malformed_url(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://ysutube.com"

        self.assertFalse(obj.is_playlist)

    def test_link_is_not_playlist_empty_url(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u""

        self.assertFalse(obj.is_playlist)

    def test_link_playlist_not_playlist_link(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/watch?V=2K8_jgiNqUc"

        self.assertEquals("", obj.playlist_link)

    def test_link_playlist_gdata(self):
        obj = YoutubeVideoSlide()
        obj.video_link = u"https://www.youtube.com/playlist?list=PL3EThPF3sbJppGg2o65CjpeCkJ7Y2UvKn"

        self.assertEquals("https://gdata.youtube.com/feeds/api/playlists/PL3EThPF3sbJppGg2o65CjpeCkJ7Y2UvKn",
                          obj.playlist_link)
