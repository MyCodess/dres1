# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

project = 'Sphinx-Extensions-eg1'
copyright = '2023, au1'
author = 'au1'

# #----------- Allg-prj: --------------------------------
# #--!! adding prj-src-code-path to the sys.path , so can be found/loaded in rst-sphinx-docs :
srcRoot = os.path.abspath('../src/')
sys.path.append(srcRoot)
# #--
# #--  include_patterns = [
# #--      '**', ##--all files in the source directory and subdirectories, recursively
# #--      '../stage1/',
# #--      ]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
primary_domain = 'py'

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    ]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# #--1org:  html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
