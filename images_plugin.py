'''
##################################################
Pelican plugin to pre-process the images attribute
##################################################
'''
import os
import subprocess

from itertools import chain
from pelican import signals, contents
from pelican.generators import Generator
from pelican.utils import copy


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
            self.static_images[name] = {'_source': os.path.join(self.settings['PATH'], filename),
                                        '_basepath': os.path.split(filename)[0],
                                        'full': '{0}-full{1}'.format(name, extension),
                                        'medium': '{0}-medium{1}'.format(name, extension),
                                        'small': '{0}-small{1}'.format(name, extension),
                                        'thumbnail': '{0}-thumbnail{1}'.format(name, extension)}
        self._update_context(('static_images',))

    def generate_output(self, writer):
        for image in self.static_images.values():
            os.makedirs(os.path.join(self.output_path, image['_basepath']), exist_ok=True)
            copy(image['_source'], os.path.join(self.output_path, image['_basepath'], image['full']))
            subprocess.run(['convert', image['_source'], '-resize', '1024x1024', os.path.join(self.output_path, image['_basepath'], image['medium'])])
            subprocess.run(['convert', image['_source'], '-resize', '640x640', os.path.join(self.output_path, image['_basepath'], image['small'])])
            subprocess.run(['convert', image['_source'], '-resize', '240x', os.path.join(self.output_path, image['_basepath'], image['thumbnail'])])


def preprocess_images(generator):
    """Adds ``order``, ``parents``, and ``children`` attributes to all
    pages.
    """
    for article in generator.articles:
        if hasattr(article, 'images'):
            article.images = [{'full': 'images/{0}-full.jpg'.format(name.strip()),
                               'medium': 'images/{0}-medium.jpg'.format(name.strip()),
                               'small': 'images/{0}-small.jpg'.format(name.strip()),
                               'thumbnail': 'images/{0}-thumbnail.jpg'.format(name.strip())} for name in article.images.split(',')]


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
    signals.article_generator_finalized.connect(preprocess_images)
