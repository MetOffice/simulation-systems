.. _jules_docs:

The JULES User Guide
====================

The JULES User Guide is built using the :ref:`Sphinx Documentation Generator
<sphinx>`. The source files for the JULES documentation are contained
in the `JULES GitHub repository`_, with the plain text files contained in the
`source`_ directory.

.. _JULES GitHub repository: https://github.com/jules-lsm/jules-lsm.github.io
.. _source: https://github.com/jules-lsm/jules-lsm.github.io/tree/master/user_guide/doc/source

The JULES User Guide uses some custom extensions to reStructuredText to allow
it to represent Fortran namelists more effectively - these are discussed in
more detail below.


reStructuredText Extension for Fortran Namelists
------------------------------------------------

The JULES User Guide uses a custom extension to reStructuredText to allow a
more natural expression of Fortran namelists
(see `user_guide/doc/sphinxext/sphinx_nml_domain.py`_ if you are interested in
the implementation).

.. _user_guide/doc/sphinxext/sphinx_nml_domain.py: https://github.com/jules-lsm/jules-lsm.github.io/blob/master/user_guide/doc/sphinxext/sphinx_nml_domain.py

Documenting namelists
---------------------

To begin documenting a namelist, the directive

.. code-block:: text

    .. nml:namelist:: <NAMELIST_NAME>

is used. By convention, namelist names are ``UPPER_CASE``, while namelist
member names are ``lower_case``.

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
used. The description of the namelist member can contain any valid
reStructuredText markup, as long as it is indented correctly.

The final directive used to document namelists is:

.. code-block:: text

    .. nml:group:: <Text describing the group>

        .. nml:member:: <member1>
            <Description of member1>

        .. nml:member:: <member2>
            <Description of member2>

``nml:group`` is used to group logically related members within a namelist. Any
number of members can be contained within it, but they must be indented. Any
un-indented members end the group.

For an example of how ``nml:group`` might be used, see the documentation of
``JULES_INPUT_GRID`` in `model_grid.nml`_. To see how the nml:group directive
is rendered, see `JULES_INPUT_GRID namelist members`_.

.. _model_grid.nml: https://jules-lsm.github.io/latest/namelists/model_grid.nml.html
.. _JULES_INPUT_GRID namelist members: https://jules-lsm.github.io/latest/namelists/model_grid.nml.html#jules-input-grid-namelist-members

Note - If you are adding a completely new namelist then the namelist name also
needs to be added to the contents page in source/namelists/contents.rst in
order for it to be included in the build.


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

So to link to the member ``l_aggregate`` of namelist ``JULES_SURFACE``, we
would use the following:

.. code-block:: text

    This is some text, with a link to :nml:mem:`JULES_SURFACE::l_aggregate`
    embedded.

The cross-references are rendered as hyperlinks in the HTML version, and link
to different parts of the document in the PDF version.


Checking for broken hyperlinks
-------------------------------

One can test whether there are broken hyperlinks in the user guide by running

.. code-block:: shell

    make linkcheck
