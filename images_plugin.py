'''
##################################################
Pelican plugin to pre-process the images attribute
##################################################
'''
import os
import subprocess

from itertools import chain
from pelican import signals, contents
from pelican.generators import Generator, ArticlesGenerator
from pelican.utils import copy


class StaticImage(object):

    def __init__(self, base_path, filename):
        self.source = os.path.join(base_path, filename)
        self.base = os.path.split(filename)[0]
        self.full = StaticImageVersion(filename, 'full')
        self.medium = StaticImageVersion(filename, 'medium')
        self.small = StaticImageVersion(filename, 'small')
        self.thumbnail = StaticImageVersion(filename, 'thumbnail')


class StaticImageVersion(object):

    def __init__(self, filename, size):
        self.filename = '{0}-{2}{1}'.format(*os.path.splitext(os.path.basename(filename)), size)
        self.url = '/images/{0}-{2}{1}'.format(*os.path.splitext(os.path.basename(filename)), size)


class ImageGenerator(Generator):
    """Generate all static images, automatically generating required sizes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate_context(self):
        self.static_images = {}
        found_files = self.get_files(self.settings['IMAGE_PATHS'],
                                     exclude=self.settings['IMAGE_EXCLUDES'],
                                     extensions=['jpg'])
        for filename in found_files:
            name, extension = os.path.splitext(os.path.basename(filename))
            #self.static_images[name] = {'_source': os.path.join(self.settings['PATH'], filename),
            #                            '_basepath': os.path.split(filename)[0],
            #                            'full': '{0}-full{1}'.format(name, extension),
            #                            'medium': '{0}-medium{1}'.format(name, extension),
            #                            'small': '{0}-small{1}'.format(name, extension),
            #                            'thumbnail': '{0}-thumbnail{1}'.format(name, extension)}
            self.static_images[name] = StaticImage(self.settings['PATH'], filename)
        self._update_context(('static_images',))

    def generate_output(self, writer):
        for image in self.static_images.values():
            pass
            os.makedirs(os.path.join(self.output_path, image.base), exist_ok=True)
            copy(image.source, os.path.join(self.output_path, image.base, image.full.filename))
            subprocess.run(['convert', image.source, '-resize', '1024x1024', os.path.join(self.output_path, image.base, image.medium.filename)])
            subprocess.run(['convert', image.source, '-resize', '640x640', os.path.join(self.output_path, image.base, image.small.filename)])
            subprocess.run(['convert', image.source, '-resize', '240x', os.path.join(self.output_path, image.base, image.thumbnail.filename)])


def preprocess_images(generators):
    """Adds ``order``, ``parents``, and ``children`` attributes to all
    pages.
    """
    article_generator = [g for g in generators if isinstance(g, ArticlesGenerator)][0]
    image_generator = [g for g in generators if isinstance(g, ImageGenerator)][0]
    for article in article_generator.articles:
        if hasattr(article, 'images'):
            article.images = [image_generator.static_images[name] for name in article.images.split(',') if name in image_generator.static_images]
    #        article.images = [{'full': 'images/{0}-full.jpg'.format(name.strip()),
    #                           'medium': 'images/{0}-medium.jpg'.format(name.strip()),
    #                           'small': 'images/{0}-small.jpg'.format(name.strip()),
    #                           'thumbnail': 'images/{0}-thumbnail.jpg'.format(name.strip())} for name in article.images.split(',')]


def get_generator(pelican_object):
    """Return the PersonGenerator to be used to generate the person pages"""
    return ImageGenerator


def add_default_settings(pelican_object):
    """Add the required default settings for the person generation."""
    if 'IMAGE_PATHS' not in pelican_object.settings:
        pelican_object.settings['IMAGE_PATHS'] = []
    if 'IMAGE_EXCLUDES' not in pelican_object.settings:
        pelican_object.settings['IMAGE_EXCLUDES'] = []


def register():
    """Registers the processing callbacks."""
    signals.initialized.connect(add_default_settings)
    signals.get_generators.connect(get_generator)
    signals.all_generators_finalized.connect(preprocess_images)
