# -*- coding: utf-8 -*-
"""Sphinx documentation """

# -- Path setup --------------------------------------------------------------

import os
from os.path import abspath, dirname
import sys

# -- Project information -----------------------------------------------------

project = "DRM integration"
copyright = "Accelize"
author = "jeydoux@accelize.com"
version = "v1.3"
release = "v1.3"


# -- General configuration ---------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon',
              'sphinx.ext.coverage', 'sphinx.ext.viewcode', 
              'sphinx.ext.autosectionlabel']

source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.settings']
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_favicon = '_static/favicon.ico'

html_context = {
    'css_files': ['_static/accelize.css', '_static/custom.css'],  # Overwrite them style
    'display_github': False, # Add 'Edit on Github' link instead of 'View page source'
    'last_updated': True,
    'commit': False
}

html_logo = '_static/logo.png'

html_show_sourcelink = False

html_show_sphinx = False

templates_path = ['_templates']


# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = '%sdoc' % project

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {}
latex_documents = [(
    master_doc, '%s.tex' % project, '%s Documentation' % project, author,
    'manual')]

latex_logo = '_static/logo.png'

# -- Options for manual page output ------------------------------------------

man_pages = [(
    master_doc, "my_name", '%s Documentation' % project,
    [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

texinfo_documents = [(
    master_doc, project, '%s Documentation' % project, author, project,
    "my_description", 'Miscellaneous')]


#https://stackoverflow.com/questions/36019670/removing-the-edit-on-github-link-when-using-read-the-docs-sphinx-with-readthed
def setup(app):
    app.add_stylesheet('custom.css')
