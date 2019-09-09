'''
##################################################
Pelican plugin to pre-process the images attribute
##################################################
'''
import os

from itertools import chain
from pelican import signals, contents


def preprocess_images(generator):
    """Adds ``order``, ``parents``, and ``children`` attributes to all
    pages.
    """
    for article in generator.articles:
        if hasattr(article, 'images'):
            article.images = [img.split(',') for img in article.images.split(';')]


def register():
    """Registers the processing callbacks."""
    signals.article_generator_finalized.connect(preprocess_images)
