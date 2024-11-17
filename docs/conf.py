# Configuration file for the Sphinx documentation builder.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Textra AI Research'
copyright = '2024, Fatima Zahra Oubella'
author = 'Fatima Zahra Oubella'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# Add these lines to specify the source directory
source_suffix = '.rst'
master_doc = 'index'
# Important: Add this line to point to your source directory
source_dir = 'source'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

templates_path = ['source/_templates']  # Updated path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['source/_static']  # Updated path

# Theme options
html_theme_options = {
    'display_version': True,
    'navigation_depth': 4,
    'collapse_navigation': False,
    'titles_only': False,
}