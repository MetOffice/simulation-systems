.. _inputs:

Input Variables, Rose Metadata and Upgrade Macros
=================================================

.. important::

    New UM Ancils must be submitted to the MIAO team for approval. Please
    follow their process for `Requesting New UM Ancils
    <https://code.metoffice.gov.uk/trac/ancil/wiki/ANTS/ProjectManagement/updating_UMDIR>`__.

Sometimes the developer needs to alter model namelists and input variables. A
common reason is for the inclusion of a new piece of code which has to be
turned off by default.

If a developer changes the namelist inputs they are also expected to alter the
following areas of the code:

* The inclusion of appropriate defensive checks.
* Changes to Rose metadata.
* Upgrade macros.

Defensive checks abort the model run if the user sets variables outside of
their expected range or a combination of variables that will lead to an error.
Most namelist modules contain a subroutine which performs this checking and
which can be modified.

The project metadata can be found in the following locations:

.. tab-set::

    .. tab-item:: UM

        ``<branch_name>/rose-meta/um-atmos/HEAD/rose-meta.conf``

    .. tab-item:: JULES

        ``<branch_name>/rose-meta/*/*/HEAD/rose-meta.conf``

    .. tab-item:: LFRic

        ``<branch_name>/<sub-module>/rose-meta/*/HEAD/rose-meta.conf``

In addition to the above locations, the rose metadata is centrally mirrored on
Met Office systems. This means that metadata that has been committed to the
trunk can be accessed without a working copy. This may be of use when
upgrading scientific suites between versions.

All new namelist variables need a new entry so that the metadata loads into the
Rose GUI for users to switch it on. Additionally, sometimes the metadata needs
to be modified without changing a namelist variable. Guidance for updating the
metadata :ref:`is available <metadata_guidance>`.

..
  Could do with thinking about how the JULES metadata could be included in this
  document in the future, rather than the JULES wiki page
  (https://code.metoffice.gov.uk/trac/jules/wiki/WorkingPractices#NamelistsUpgradeMacrosMetadata)

.. note::

    JULES developers also need to :doc:`update the JULES documentation
    <jules_docs>` whenever they add or remove namelist variables.

.. important::

    All changes which alter namelists require an upgrade macro for them to work
    with the model.

Changes to the metadata which don't involve namelist changes may or may not
require an upgrade macro. If you are unsure whether a change needs an upgrade
macro, then run the following command on your branch:

.. code-block:: shell

  rose stem --group=scripts

If all of the tests pass then there is no requirement to add an upgrade macro.
If any of the metadata tests fail, then the developer should add a blank
upgrade macro which contains no upgrade commands but simply points the rose
stem suite to the new metadata. The SSD team are also available to advise on
whether an upgrade macro is necessary.

.. tip::

  When editing metadata you should always check that the new metadata appears
  as expected in the GUI, including testing that invalid settings raise
  appropriate warnings. The command to open the GUI is in general:

  .. code-block:: shell

    rose edit -C rose-stem/app/APP-NAME

  For LFRic Apps a few extra changes are required. In your branch (your test
  branch if you have an upgrade macro):

  .. code-block:: shell

    cd rose-meta
    rose edit -C rose-stem/app/APP-NAME --no-warn version

  If you have a linked LFRic Core or Jules ticket with metadata changes, you
  can load their metadata by adding ``-M /path/to/working_copy/rose-meta`` to
  the ``rose-edit`` command.


Adding a new LFRic Metadata Section
-----------------------------------

Due to the way lfric metadata is shared, if a new LFRic metadata section is
added, then a few new files are added. A new LFRic metadata section here is
defined as a new directory within an existing or new ``rose-meta`` directory.
Adding a new metadata section requires:

* ``rose-meta/META-NAME/HEAD/rose-meta.conf``
* ``rose-meta/META-NAME/vnX.Y/rose-meta.conf`` (where ``X.Y`` is the most
  recent released version)
* ``rose-meta/META-NAME/versions.py``
* A symlink from the top-level rose-meta directory to the new directory
  (see existing ones for examples)

The ``vnX.Y`` and ``HEAD`` metadata should be identical for this initial
ticket, other than any import statements, which should point at vnX.Y or HEAD
respectively. Other ``vnX.Y`` and ``versionAB_CD.py`` files shouldn't be
modified or added (these are a snapshot of the metadata at a release).

If a new rose-stem app using the new metadata is also being added, then
a "blank" upgrade macro will also need to be added with a ``BEFORE_TAG=vnX.Y``
and a standard ``AFTER_TAG=vnX.Y_tTTTT``. This upgrade macro will allow the
new app to be updated to the Head metadata when the branch is merged to trunk.
The ``rose-app.conf`` for this app will require a metadata import line of
format, ``meta=META-NAME/vnX.Y``.


How to add an upgrade macro to your branch
------------------------------------------

Please see :ref:`this page <macros>` for further information.

.. tip::

    When developing a change that updates the input and/or user interface, then
    repeatedly running/reverting the upgrade macro on the dev branch, or
    creating many test branches can be tiresome. Consider working up your
    change with the new options hard-coded in until such time as you are ready
    to connect up to the input for real.

.. important::

    If your development includes an upgrade macro, you **must** add the
    ``macro`` keyword to your ticket.

    **Do not** apply the upgrade macro to your dev branch prior to the review
    process. Instead you must create a test branch. See :ref:`testing`.

.. toctree::
    :hidden:

    metadata_guidance
    macros
