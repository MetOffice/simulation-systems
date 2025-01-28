.. _inputs:

Input Variables, Rose Metadata and Upgrade Macros
=================================================

.. important::

    New UM Ancils must be submitted the the MIAO team for approval. Please follow their process for `Requesting New UM Ancils <https://code.metoffice.gov.uk/trac/ancil/wiki/ANTS/ProjectManagement/updating_UMDIR>`_.

Sometimes the developer needs to alter model namelists and input variables.
A common reason is for the inclusion of a new piece of code which has to be
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

        ``vnXX.Y_<_branch_name>/rose-meta/um-atmos/HEAD/rose-meta.conf``

    .. tab-item:: JULES

        ``vnXX.Y_<_branch_name>/rose-meta/*/*/HEAD/rose-meta.conf``

    .. tab-item:: LFRic

        ``vnXX.Y_<branch_name>/<sub-module>/rose-meta/*/HEAD/rose-meta.conf``

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
  </WorkingPractices/jules_docs>` whenever they add or remove namelist variables.

.. important::
  All changes which alter namelists require an upgrade macro for them to
  work with the model.

Changes to the metadata which don't involve namelist changes may or may not
require an upgrade macro. If you are unsure whether a change needs an
upgrade macro, then run the following command on your branch:

.. code-block::

  rose stem --group=scripts

If all of the tests pass then there is no requirement to add an upgrade macro.
If any of the metadata tests fail, then the developer should add a blank upgrade
macro which contains no upgrade commands but simply points the rose stem suite
to the new metadata. The SSD team are also available to advise on whether an upgrade macro is necessary.

.. tip::

  When editing metadata you should always check that the new metadata appears as expected in the gui, including testing that invalid settings raise appropriate warnings. The command to open the gui is in general:

  .. code-block::

    rose edit -C rose-stem/app/APP-NAME

  For LFRic Apps a few extra changes are required. In your branch (your test branch if you have an upgrade macro):

  .. code-block::

    export ROSE_PYTHONPATH=$PYTHONPATH
    export ROSE_META_PATH=/path/to/valid/core:/path/to/apps/copy
    rose edit -C rose-stem/app/APP-NAME --no-warn version

  This requires an LFRic Core working copy at an appropriate revision to be available. It is also necessary to run from the top level of the Apps working copy to ensure rose metadata paths are valid.

How to add an upgrade macro to your branch
------------------------------------------

Please see :ref:`this page <macros>` for further information.

.. tip::
  When developing a change that updates the input and/or user interface,
  then repeatedly running/reverting the upgrade macro on the dev branch,
  or creating many test branches can be tiresome. Consider working up your
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
