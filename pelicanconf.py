#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mark Hall'
SITENAME = 'Steinreich'
SITEURL = ''

# Content path configuration
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['texts']
IMAGE_PATHS = ['images']
STATIC_PATHS = []

# Theme configuration
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'de'
THEME = './theme'

# No feeds or external links required
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

PLUGIN_PATHS = ['./']
PLUGINS = [
    'images_plugin',
    'extra_filters',
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DEVELOPMENT = True

# Theme Groupings
MUSEUM_EGYPT = [
    'den-steinen-auf-der-spur',
    'steinhart-und-steinalt',
    'zuruck-in-die-steinzeit',
    'stein-und-brot',
    'die-kraft-der-steine',
    'jenseits-des-menschlichen-masses',
    'und-das-wort-ward-stein',
    'zu-stein-geworden-aus-stein-geboren',
]
MUSEUM_ANTIQUITIES = [
    'der-weg-der-steine',
    'mensch-formt-stein-stein-formt-mensch',
    'bilder-aus-stein',
    'mord-und-steinschlag',
    'im-schutz-der-steine',
    'grabstein-und-steingrab',
    'das-mass-der-steine',
    'un-verganglichkeit',
]
