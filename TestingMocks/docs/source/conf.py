# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.insert(0, os.path.abspath('../../testing-mock-api/app'))

# -- Project information -----------------------------------------------------
project = 'TestingMocks'
copyright = '2025, Egor Kuznetsov, Igor Akimov'
author = 'Egor Kuznetsov, Igor Akimov'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',         # Generate documentation from docstrings
    'sphinx.ext.napoleon',        # Support Google and NumPy style docstrings
    'sphinx.ext.todo',            # Support "todo" directives
    'sphinx.ext.viewcode',        # Add links to source code
    'sphinx.ext.intersphinx',     # Link to other Sphinx documentation
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']  # Exclude build directory

language = 'en'  # English language

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Read the Docs theme
html_static_path = ['_static']

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'requests': ('https://requests.readthedocs.io/en/latest/', None),
}

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True  # Show todo notes

# -- Options for Napoleon extension ------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- General information about the project.
master_doc = 'index'
