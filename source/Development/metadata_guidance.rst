.. _metadata_guidance:

..
  This section will need some thought and revisiting after CA2 is completed.

.. important::

    Do **not** edit the existing ``vnX.Y`` metadata directories or the upgrade
    python files (e.g. ``versionab_cd.py``) as these are a snapshot of the
    metadata at release. Only the ``HEAD`` and ``versions.py`` files should be
    modified.

Some basic guidance on Rose metadata
====================================

It is important that the appearance of inputs across the GUI panels conform to
the same standards. This ensures that users of each model become familiar with
how the panels work and are present with a consistent set of information, such
as follows:

.. code-block::

   [namelist:<namelist>=<variable>]
   description=<what is the variable for?>
   help=<detailed information about the variable>
   sort-key=<XY>
   url=<http://jules-lsm.github.io/latest/namelists/<namelist>.nml.html#<NAMELIST>::<item>>
   etc

where JULES namelist items should only contain the ``url=`` field and not the
``help=`` field regardless of the repository they reside in. Each input is
presented in the GUI as:

.. code-block::

    variable name
    short description of the variable name

Either the help text is displayed or web help opened when one clicks the
variable name. If both fields exist the Web help is opened preferentially. If
a ``url=`` is present the ``help=`` field should be removed to avoid
duplication.

.. _shared-namelists:

Shared namelists
----------------

Shared namelist items, or items which exist in more than one repository, should
have identical metadata regardless of the repository where they reside
(e.g. JULES items in the UM metadata). The only caveats are where a
``trigger`` or a ``fail-if`` reference a namelist item from the parent model
(e.g. UM).

Shared JULES metadata is in the process of being migrated to
`rose-meta/jules-shared
<https://code.metoffice.gov.uk/trac/jules/browser/main/trunk/rose-meta/jules-shared>`__,
which resides in the JULES repository. The sub-directories are imported
by **rose-meta/um-atmos** and **rose-meta/jules-standalone** and is manually
synced with a copy in LFRic. Please see `Sharing JULES metadata
<https://code.metoffice.gov.uk/trac/jules/wiki/SharingJULESmetadata>`__ for
more details including what should be in `jules-shared
<https://code.metoffice.gov.uk/trac/jules/wiki/SharingJULESmetadata#Whatsinjules-shared>`__
and in `jules-standalone, jules-lfric or um-atmos
<https://code.metoffice.gov.uk/trac/jules/wiki/SharingJULESmetadata#Whatsinjules-standalonejules-lfricorum-atmos>`__.
When developing shared JULES metadata, you will need :ref:`linked tickets
<multirepo>`. The metadata migration is currently dictated by LFRic porting of
science, although the ultimate aim is to have a single source of truth.

Please see the :ref:`rose config-edit example<metadata_changes>` for an
illustration of how to pick up **jules-shared** changes from a JULES working
copy.

..
    We need to check if this is all still the case with cylc 8.

The following sections provide some general guidance as to how to structure
your metadata.

..
    This is largely based on how the UM does everything, so should be revisited
    after the CA2 activity is finished. The following sections have been

Number of panels
----------------

If you have a particularly long namelist, consider dividing up the number of
panels to ensure that the user doesn't have to deal with a particularly long
panel with lots of switches. However, switches which relate to each other
should always be on the same panel.


Sort Keys and triggers
----------------------

Please use sort-keys to order the appearance of items in your panels, otherwise
they will appear in alphabetical order. This means that sometimes items that
are triggered on and off will appear far away from the item that triggered
them.

Please provide triggers for all variables where possible. It is much better and
cleaner to only see inputs that need to be set rather than everything.

.. tip::

    The GUI provides an option to un-hide triggered variables if one wants to
    see them all.

Please set ``compulsory=true`` for items and use triggers for when it is not
required. The settings of all variables will then be present, in all apps to
aid configuration management. When a variable is triggered off, it will be
commented out in the apps e.g. ``!!variable``.

..
    I think from memory that JULES doesn't do the compulsory=true, which is
    something for CA2 to look at.

.. important::

    If any variable (new or existing) has received a new compulsory=true
    setting please use an upgrade macro to add that variable to apps with a
    valid value.

.. note::

    While it is possible to trigger a variable based on ``AND`` logic
    (e.g. where some condition on ``variable1`` and another condition on
    ``variable2`` trigger ``variable3``), cumbersome triggering of this nature
    is best avoided.

    It is not possible to trigger a variable based on ``OR`` logic.

.. _metadata_changes:

Viewing metadata changes as you go along
-----------------------------------------

One can easily review their metadata changes with the rose config editor,
opening up an example app file. For example:

.. code-block:: shell

    cd <branch path>/rose-stem/app/um_n48_eg
    rose config-edit -M <branch path>/rose-meta/

If making **jules-shared** changes, when reviewing these changes from a
different parent repository, you will first need to set the ``ROSE_META_PATH``
system variable:

.. code-block:: shell

   export ROSE_META_PATH=<JULES branch path>/rose-meta/

or add the path instead as a colon separated list:

.. code-block:: shell

   rose config-edit -M <branch path>/rose-meta/:<JULES branch path>/rose-meta/

then once the app opens click on the LHS appname to display the app meta panel.
Update this to HEAD rather than the version number and apply.

Please note that if you have used an upgrade macro on the app then the meta
line at the top of the app file will have changed
(e.g. meta=um-atmos/vn11.0_t46). Since no metadata exists at this version rose
edit will produce an error saying that it cannot find it, instead it will use
the metadata in e.g. um-atmos/HEAD. Please click OK and continue.

Your updates should now appear.

Ensuring metadata changes are valid
-----------------------------------

Developments to the metadata can be checked for errors by running `rose
metadata-check
<https://metomi.github.io/rose/doc/html/api/command-reference.html#rose-metadata-check>`__

.. code-block:: shell

   rose metadata-check -C /path/to/rose-meta/<config>/HEAD

where the ``-C`` option can be omitted if inside the directory containing the
metadata file.

.. note::

   If there are **jules-shared** changes then these need to be added to the
   metadata path even in the JULES repository. As the metadata checker does
   not have the ``-M`` option, this has to be done using the `ROSE_META_PATH`
   environment variable as in the :ref:`previous example<metadata_changes>`.

   If the metadata checker returns "not a configuration metadata directory"
   then this may indicate that the wrong path has been set.
