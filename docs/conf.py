# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../popsycle/'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../SPISEA/spisea/'))
sys.path.insert(0, os.path.abspath('../SPISEA/'))
sys.path.insert(0, os.path.abspath('../BAGLE_Microlensing/src/'))
os.environ["PYSYN_CDBS"] = "../cbds"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PopSyCLE'
copyright = '2023, Casey Lam, Jessica Lu, Michael Medford, Natasha Abrams, Sam Rose'
author = 'Casey Lam, Jessica Lu, Michael Medford, Natasha Abrams, Sam Rose'
release = '2.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax', 'numpydoc', 'sphinx_rtd_theme'] #'sphinx.ext.napoleon'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'deprecated']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
