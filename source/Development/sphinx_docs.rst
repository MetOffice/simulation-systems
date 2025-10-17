.. _sphinx:

Sphinx Documentation
====================
The documentation is written in plain text files using a markup language called
reStructuredText. The text files have the extension ``.rst``. Sphinx can
take these text files and generate both HTML and PDF documentation from them
(complete with cross-referencing links, etc.). Since reStructuredText is a
plain text format, your favourite text editor is all you need to edit the
documentation.

.. tip::
    The `Sphinx documentation <https://www.sphinx-doc.org/en/master/>`_ is an
    useful resource.


Building the documentation
--------------------------

Please create the production environment to build the
documentation (first time users only), and then activate it.

.. tab-set::

    .. tab-item:: JULES

        From the top level of the repository:

        .. code-block:: shell

            conda env create -f environment.yml

        Activate the environment:

        .. code-block:: shell

            conda activate jules-user-guide

    .. tab-item:: LFRic Apps and Core

        On the Met Office Azure Spice machine the main LFRic module environment
        contains all the required packages to build the documentation. Ensure
        this is loaded.

        Note there is a `style guide included in the LFRic Core documentation
        <https://metoffice.github.io/lfric_core/how_to_contribute/style_guides
        /documentation_style_guide.html>`_ that should be followed for both
        these repositories.

    .. tab-item:: Working Practices

        From the top level of the repository:

        .. code-block:: shell

            conda env create -f env.yml

        Activate the environment:

        .. code-block:: shell

            conda activate sphinx_doc_env

Move to the documentation directory and run ``make`` to build the documentation:

To build and view the HTML documentation:

.. code-block:: shell

    make [clean] html
    firefox build/html/index.html

To build and view the PDF documentation:

.. code-block:: shell

    make latexpdf
    evince build/latex/JULES_User_Guide.pdf
