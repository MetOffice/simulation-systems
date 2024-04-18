# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import datetime

# -- Project information -----------------------------------------------------

project = 'Simulation Systems'
copyright = f'2023 - {datetime.datetime.now().year},  Met Office'
author = 'Simulation Systems and Deployment Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_sitemap'
]

# Added to use dropdowns with command: pip install sphinx-design
extensions = ['sphinx_design']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_title = 'Simulation Systems'

# See https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/configuring.html#configure-the-search-bar-position
html_sidebars = {
    "**": [
        "search-field",
        "sidebar-nav-bs",
        "sidebar-ethical-ads",
    ]
}

html_theme_options = {
    "footer_start": ["copyright", "sphinx-version"],
    "navigation_depth": 3,
    "navigation_with_keys": False,
    "show_toc_level": 2,
    "show_prev_next": True,
    "navbar_align": "content",
    # removes the search box from the top bar
    "navbar_persistent": [],
    # TODO: review if 6 links is too crowded.
    "header_links_before_dropdown": 6,
}

# Hide the link which shows the rst markup
html_show_sourcelink = False
