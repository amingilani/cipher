# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CIPHER'
copyright = '2024, CIPHER Contributors'
author = 'CIPHER Contributors'
release = '0.1.0'

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
]

# Language settings
language = 'en'
locale_dirs = ['locale/']
gettext_compact = False

# HTML output settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = '_static/cipher_logo.png'
html_theme_options = {
    'logo_only': True,
    'display_version': True,
    'navigation_depth': 4,
}

# PDF output settings
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
}

# Add any paths that contain templates here
templates_path = ['_templates']

# Source suffix
source_suffix = '.rst'

# The master toctree document
master_doc = 'index' 
