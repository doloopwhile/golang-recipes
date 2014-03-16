#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
PLUGIN_PATH = os.path.expanduser('~/pelican-plugins')
PLUGINS = ["read_more_link"]
AUTHOR = 'OMOTO Kenji'
SITENAME = 'Golang Recipes'
SITEURL = 'http://localhost:8000/'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.expanduser('~/pelican-themes/simple-bootstrap')

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

GITHUB_URL = 'https://github.com/doloopwhile/golang-recipes'

DISQUS_SITENAME = 'golangrecipes'


# This settings indicates that you want to create summary at a certain length
SUMMARY_MAX_LENGTH = 50

# This indicates what goes inside the read more link
# READ_MORE_LINK = None (ex: '<span>continue</span>')
READ_MORE_LINK = '<span>continue</span>'

# This is the format of the read more link
READ_MORE_LINK_FORMAT = '<p><a class="read-more" href="/{url}">{text}</a></p>'

READ_MORE_COMMENT = 'continue'
