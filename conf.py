# -*- coding: utf-8 -*-
import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.imgmath', 'sphinx.ext.ifconfig', 'sensio.sphinx.configurationblock']
source_suffix = '.rst'
master_doc = 'index'
project = 'Open Loyalty'
copyright = u'2011-2018, Divante Ltd'
version = ''
release = ''
exclude_patterns = ['_includes/*.rst']
html_theme = 'ol_rtd_theme'
html_theme_path = ["_themes"]
htmlhelp_basename = 'Openloyaltydocs'
man_pages = [
    ('index', 'open-loyalty', u'Open Loyalty Documentation',
     [u'Divante Ltd'], 1)
]
sys.path.append(os.path.abspath('_exts'))
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
rst_epilog = """
"""
