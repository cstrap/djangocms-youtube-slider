#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="djangocms_youtube_slider",
    version="0.1.2",
    url='https://github.com/cstrap/djangocms_youtube_slider',
    license='MIT',
    description="django-cms plugin - Youtube Slider",
    long_description=open('README.rst').read(),
    author='Christian Strappazzon',
    author_email='lab@strap.it',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        "Django<1.6",
        "django-cms<2.5",
        "requests<2.6"
    ],
    dependency_links=[
        'git+https://github.com/cstrap/django-admin-sortable2.git#egg=django-admin-sortable2'
    ],
    include_package_data=True,
    zip_safe=False,
)