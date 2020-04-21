import json

from io import StringIO
from lxml import etree
from pelican import signals
from random import sample


def tag_set(articles):
    """Returns a set of Tags from a list of Articles."""
    tags = set()
    for article in articles:
        tags.update(article.tags)
    return tags


def landing_page_images(articles):
    images = []
    for article in articles:
        if hasattr(article, 'images') and article.images:
            content = etree.parse(StringIO('<div id="snippet">{0}</div>'.format(article.content)), etree.HTMLParser())
            original = ''
            translation = ''
            is_greek = False
            for child in content.xpath("//div[@id='snippet']")[0].iterchildren():
                if 'class' in child.attrib:
                    classes = child.attrib['class'].split(' ')
                    if 'original' in classes:
                        original = ''.join(child.itertext())
                        if 'greek' in classes:
                            is_greek = True
                    elif 'translation' in classes:
                        translation = ''.join(child.itertext())
            for image in article.images:
                images.append({'url': article.url,
                               'full': image.full.url,
                               'medium': image.medium.url,
                               'small': image.small.url,
                               'title': article.metadata['title'],
                               'original': original,
                               'isGreek': is_greek,
                               'translation': translation,
                               'alt': '{0}: {1}'.format(image.author, image.title)})
    return images


def install_extra_filters(generator):
    """Install the extra filters."""
    generator.env.filters['tag_set'] = tag_set
    generator.env.filters['landing_page_images'] = landing_page_images


def register():
    """Register the extra filters"""
    signals.generator_init.connect(install_extra_filters)
