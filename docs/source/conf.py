# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'CIPHER'
copyright = '2024, CIPHER Contributors'
author = 'CIPHER Contributors'
release = '0.1.0'

# The master toctree document
master_doc = 'index'
root_doc = 'index' 

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
html_theme_options = {
    'navigation_depth': 4,
    'titles_only': True,
    'sticky_navigation': True,
    'collapse_navigation': False,
    'includehidden': False,
}

html_context = {
    'display_github': True,
    'github_user': 'amingilani',
    'github_repo': 'cipher',
    'github_version': 'master/docs/source/',
}

# PDF output settings
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
}

# Single bilingual PDF configuration
latex_documents = [
    (master_doc, 'CIPHER.tex', 'CIPHER Documentation / Documentation CIPHER',
     'CIPHER Contributors / Contributeurs CIPHER', 'manual', False),
]

# Source suffix
source_suffix = {'.rst': 'restructuredtext'}
templates_path = ['_templates']
