# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import datetime
import doctest
import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Signalyzer'
author = 'Jochen Gerhaeusser'
copyright = f"2021-{datetime.datetime.utcnow().year}, {author}"
version = '0.3.0'
release = '0.3.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    # "myst_parser",
    "sphinx_copybutton",
    # "sphinx_panels",
    "sphinx_plotly_directive",
]
master_doc = 'index'
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "source_repository": "https://gitlab.com/signalytics/signalyzer/",
    "source_branch": "main",
    "source_directory": "docs/",
    "top_of_page_button": "edit",
    "navigation_with_keys": True,
    "light_css_variables": {
    },
    "dark_css_variables": {
    },
}
html_title = f'{project} {release}'
html_logo = './_static/images/logo.png'
html_favicon = './_static/images/favicon.ico'
html_show_sourcelink = True
html_baseurl = 'https://signalytics.gitlab.io/signalyzer'
show_navbar_depth = 3

# -- Extension configuration -------------------------------------------------

# -- Options for AutoDoc -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autodoc_member_order = 'bysource'
autodoc_inherit_docstrings = False
autodoc_typehints = 'signature'
autodoc_type_aliases = {
    'Number': 'Number',
    'Sample': 'Sample',
    'Samples': 'Samples',
    'Operand': 'Operand',
    'DataFrame': 'DataFrame',
    'Trace': 'Trace'
}
autodoc_typehints_description_target = 'all'
autodoc_typehints_format = 'short'

# -- Options for ExtLinks ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html
extlinks = {
    'issue': (
        'https://gitlab.com/signalytics/signalyzer/-/issues/%s', 'issue ')
}

# -- Options for InterSphinx -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.10', None),
    'plotly': ('https://plotly.com/python-api-reference/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
}

# -- Options for Doctest ------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html#configuration
doctest_default_flags = doctest.ELLIPSIS | \
                        doctest.IGNORE_EXCEPTION_DETAIL | \
                        doctest.NORMALIZE_WHITESPACE
