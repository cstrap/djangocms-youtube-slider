# -*- coding: utf-8 -*-
from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                           'NAME': 'database'
                       }
                   },
                   ROOT_URLCONF='djangocms_youtube_slider.urls',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'adminsortable2',
                                   'mptt',
                                   'cms',
                                   'djangocms_youtube_slider',),
                   TEMPLATE_CONTEXT_PROCESSORS=(
                       'django.contrib.auth.context_processors.auth',
                       'django.core.context_processors.debug',
                       'django.core.context_processors.i18n',
                       'django.core.context_processors.media',
                       'django.core.context_processors.static',
                       'django.core.context_processors.request',
                       'django.contrib.messages.context_processors.messages',
                       'cms.context_processors.cms_settings',
                       'sekizai.context_processors.sekizai',
                   ))
