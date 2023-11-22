.. _jules_docs:

Building and editing the JULES User Guide
=========================================
The JULES User Guide is built using the Sphinx Documentation Generator. The
documentation is written in plain text files using a markup language called
reStructuredText. The source files for the JULES documentation are contained in
the `JULES GitHub repository`_. The plain text files are contained in the `source`_
directory and have the extension ``.rst``. Sphinx can take these plain text
files and generate both HTML and PDF documentation from them (complete with
cross-referencing links, etc.). Since reStructuredText is a plain text format,
your favourite text editor is all you need to edit the JULES documentation.

.. _JULES GitHub repository: https://github.com/jules-lsm/jules-lsm.github.io
.. _source: https://github.com/jules-lsm/jules-lsm.github.io/tree/master/user_guide/doc/source

The JULES User Guide uses some custom extensions to reStructuredText to allow it
to represent Fortran namelists more effectively - these are discussed in more
detail below. Other than that, the `Sphinx documentation`_ is an excellent resource.

.. _Sphinx documentation: https://www.sphinx-doc.org/en/master/

Checking out a copy of the JULES documentation
----------------------------------------------
First time developers will need to clone the git repository before starting work:

.. code-block:: text

    cd <path_to_where_you_want_to_clone_to>
    git clone git@github.com:jules-lsm/jules-lsm.github.io.git
    cd jules-lsm.github.io.git

Create and checkout a new feature branch:

.. code-block:: text

    git checkout -b <feature_branch_name>

Share the feature branch to GitHub:

.. code-block:: text

    git push --set-upstream origin <feature_branch_name>

If new files have been created, use the ``git add <file_name>`` command, then
ensure the new files (including the Sphinx sources) are tracked:

.. code-block:: text

    git add <new_file>

Commit all staged changes:

.. code-block:: text

    git commit -m "<descriptive_commit_message>"

Share the changes to GitHub:

.. code-block:: text

    git push

Create a pull request
---------------------

Create either a PR or, if the changes aren't quite ready for review, a draft
PR, see `GitHub - Creating a pull request`_

.. _GitHub - Creating a pull request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

Building the JULES User Guide
-----------------------------
For first time users, please create the production environment to build the
documentation. From the top level of the repository run:

.. code-block:: text

    conda env create -f environment.yml

Activate the environment:

.. code-block:: text

    conda activate jules-user-guide

Move to the correct directory:

.. code-block:: text

    cd <path_to>/jules-user-guide-test/doc

Run ``make`` to build the documentation:

To build and view the HTML documentation:

.. code-block:: text

    make html
    firefox build/html/index.html

To build and view the PDF documentation:

.. code-block:: text

    make latexpdf
    evince build/latex/JULES_User_Guide.pdf

reStructuredText Extension for Fortran Namelists
------------------------------------------------
The JULES User Guide uses a custom extension to reStructuredText to allow a more
natural expression of Fortran namelists (see `user_guide/doc/sphinxext/sphinx_nml_domain.py`_
if you are interested in the implementation).

.. _user_guide/doc/sphinxext/sphinx_nml_domain.py: https://github.com/jules-lsm/jules-lsm.github.io/blob/master/user_guide/doc/sphinxext/sphinx_nml_domain.py

Documenting namelists
---------------------

To begin documenting a namelist, the directive

.. code-block:: text

    .. nml:namelist:: <NAMELIST_NAME>

is used. By convention, namelist names are UPPER_CASE, while namelist member
names are ``lower_case``.

The ``nml:namelist`` directive does not output anything, but indicates that all
subsequently declared members belong to the namelist (up until the next
occurrence of ``nml:namelist``).

Once a namelist has been declared, the members of that namelist are documented
using the directive

.. code-block:: text

    .. nml:member:: <member_name>

      :type: [e.g. real, integer, logical]
      :permitted: [Permitted values, e.g. > 0, 1-5]
      :default: [Default value]

      First paragraph describing this namelist member.

      Second paragraph describing this namelist member.

      ...

The white-space (indentation and blank lines) is very important here. The
``:permitted:`` annotation is optional, and can be omitted if any value is
acceptable. If the member has no default value, ``:default: None`` should be
used. The description of the namelist member can contain any valid reStructuredText
markup, as long as it is indented correctly.

The final directive used to document namelists is:

.. code-block:: text

    .. nml:group:: <Text describing the group>

        .. nml:member:: <member1>
            <Description of member1>

        .. nml:member:: <member2>
            <Description of member2>

``nml:group`` is used to group logically related members within a namelist.
Any number of members can be contained within it, but they must be indented.
Any un-indented members end the group.

For an example of how ``nml:group`` might be used, see the documentation of
``JULES_INPUT_GRID`` in `model_grid.nml`_. To see how the nml:group directive
is rendered, see JULES_INPUT_GRID namelist members.

.. _model_grid.nml: https://jules-lsm.github.io/latest/namelists/model_grid.nml.html

Note - If you are adding a completely new namelist then the namelist name also
needs to be added to the contents page in source/namelists/contents.rst in order
for it to be included in the build.

Cross-referencing namelists and namelist members
------------------------------------------------
The custom reStructuredText extension for Fortran namelists also provides
facilities for easily cross-referencing namelists and namelist members from
anywhere in the User Guide.

To insert a cross-reference to a namelist anywhere in the documentation, use
the following within any normal piece of text:

.. code-block:: text

    :nml:lst:`<NAMELIST_NAME>`

Similarly, to cross-reference a namelist member:

.. code-block:: text

    :nml:mem:`<NAMELIST_NAME>::<member_name>`

So to link to the member ``l_aggregate`` of namelist ``JULES_SURFACE``, we would
use the following:

.. code-block:: text

    This is some text, with a link to :nml:mem:`JULES_SURFACE::l_aggregate` embedded.

The cross-references are rendered as hyperlinks in the HTML version, and link
to different parts of the document in the PDF version.

Checking for broken hyperlinks
-------------------------------
One can test whether there are broken hyperlinks in the user guide by running

.. code-block:: text

    make linkcheck