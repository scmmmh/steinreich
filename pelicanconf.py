#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mark Hall'
SITENAME = 'Steinreich'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

THEME = './theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

# Social widget
SOCIAL = []

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./']
PLUGINS = [
    'images_plugin',
    'extra_filters',
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
