#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Balázs Bujna'
SITENAME = 'DTC Jamstack POC'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TYPOGRIFY = True

THEME = "themes/mnmlist"

# I'm told I need this to make extensions work

# I've manually put include.py from the markdown-include extension
# inside both C:\\Program Files\\Python37 and C:\\Program Files\\Python37\\lib\\site-packages
# and imported MarkdownInclude from there
# and it works, too
# but markdown.extensions.markdowninclude isn't recognized
# and there's gotta be a better way
# from include import MarkdownInclude

# this is what the extension's readme says
import markdown
from markdown_include.include import MarkdownInclude

MARKDOWN = {
    'extensions' : [MarkdownInclude()],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

STATIC_PATHS = ['img']