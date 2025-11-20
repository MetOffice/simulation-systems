.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _docs:

Documentation
=============

All projects have their own scientific and technical documentation. Most
notably:

+----------------------------+-----------------------------+
| UM Documentation Papers    |`view UM`_                   |
+----------------------------+-----------------------------+
| JULES User Guide           |`view JULES`_                |
+----------------------------+-----------------------------+
| LFRic Core                 |`view LFRic Core`_           |
+----------------------------+-----------------------------+
| LFRic Apps                 |`view LFRic Apps`_           |
+----------------------------+-----------------------------+

.. _view UM: https://metoffice.github.io/um_doc/
.. _view JULES: https://jules-lsm.github.io/latest/index.html
.. _view LFRic Core: https://metoffice.github.io/lfric_core/
.. _view LFRic Apps: https://metoffice.github.io/lfric_apps/

Increasingly this documentation is stored as restructuredText markdown files
alongside the code. This is then compiled using Sphinx into the webpages above.

.. toctree::
    :maxdepth: 1

    sphinx_docs
    um_docs
    jules_docs


LFRic Apps and Core also use doxygen to document the code and all changes
should include appropriate doxygen changes to go with them. Doxygen guidelines
are available in the `LFRic Core Documentation
<https://metoffice.github.io/lfric_core/how_to_contribute/style_guides/doxygen_style_guide.html>`_.

Small changes and bug fixes rarely need documentation to be updated, but when
new science is added to a project, the documentation must be updated to ensure
that it remains contemporary with the code.

Documentation changes that are held within a repository should be documented
with issues and pull requests, are formally reviewed, and should be included
on the same branch as the code changes. Apply the `Documentation` label to your
pull request.

.. tip::

    Searching the relevant documentation for words related to your change is
    often useful when deciding whether to update the documentation.


