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

# -- Project information -----------------------------------------------------

project = 'Simulation Systems'
copyright = 'Met Office 2025'
author = 'Simulation Systems and Deployment Team'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_sitemap'
]

language = "en"

# Added to use dropdowns with command: pip install sphinx-design
extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinxcontrib.rsvgconverter',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_static_path = ["_static"]
html_css_files = ["custom.css"]
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "footer_start": ["crown-copyright", "sphinx-version"],
    "navigation_with_keys": False,
    "show_toc_level": 2,
    "show_prev_next": True,
    "navbar_align": "content",
    "logo": {
        "text": "Simulation Systems",
        "image_light": "_static/MO_SQUARE_black_mono_for_light_backg_RBG.png",
        "image_dark": "_static/MO_SQUARE_for_dark_backg_RBG.png",
    },
    "icon_links": [
        {
            "name": "GitHub Discussions",
            "url": "https://github.com/MetOffice/simulation-systems/discussions",
            "icon": "far fa-comments",
        },
    ],
}

html_context = {
    "default_mode": "auto",
}
# Hide the link which shows the rst markup
html_show_sourcelink = False

# -- Options for linkcheck builder -------------------------------------------
linkcheck_anchors = False
linkcheck_ignore = [
    r'.*\.py$',  # Ignores URLs ending with .py
    r'https://github.com/MetOffice/um*',
]
