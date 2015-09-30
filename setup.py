#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "Django>1.4,<1.7",
    "django-cms>3.0,<3.1",
    "requests>=2.7,<2.8"
]

test_requirements = [
    "Django>1.4,<1.7",
    "django-cms>3.0,<3.1",
    "requests>=2.7,<2.8",
    "django-mptt>=0.6.1,<0.7",
]

setup(
    name='djangocms-youtube-slider',
    version='0.2.0',
    description="django-cms youtube slider build with http://flexslider.woothemes.com/ and good intentions",
    long_description=readme + '\n\n' + history,
    author="Christian Strappazzon",
    author_email='lab@strap.it',
    url='https://github.com/cstrap/djangocms-youtube-slider',
    packages=[
        'djangocms_youtube_slider',
    ],
    package_dir={'djangocms-youtube-slider':
                 'djangocms_youtube_slider'},
    include_package_data=True,
    install_requires=requirements,
    dependency_links=[
        'git+https://github.com/cstrap/django-admin-sortable2.git#egg=django-admin-sortable2'
    ],
    license="MIT",
    zip_safe=False,
    keywords='djangocms-youtube-slider',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
