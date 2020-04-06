import json

from pelican import signals


def tag_set(articles):
    """Returns a set of Tags from a list of Articles."""
    tags = set()
    for article in articles:
        tags.update(article.tags)
    return tags


def install_extra_filters(generator):
    """Install the extra filters."""
    generator.env.filters['tag_set'] = tag_set


def register():
    """Register the extra filters"""
    signals.generator_init.connect(install_extra_filters)
