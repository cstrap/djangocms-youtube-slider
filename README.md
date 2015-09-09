# djangocms-youtube-slider
django-cms youtube slider built with http://flexslider.woothemes.com/ and good intentions

It works on my envs and for my purposes... but... feel free to fork and send pull requests!

## Installation

```bash
$ python setup.py install
```

Add the ```djangocms_youtube_slider``` to your ```INSTALLED_APPS```

```python
INSTALLED_APPS = (
    # ...
    'djangocms_youtube_slider',
    # ...
```

If you are using South for database migrations, please ensure you have installed at least version 1.0, or it won't be
able to find the migrations (stored under south_migrations).

Configure how to use the ```YoutubeSliderPlugin``` with django-cms.
