.. _macros:

Upgrade Macros
==============

.. important::

    When developing Upgrade Macros, they must be tested using a test branch
    (see :ref:`testing`).

To create an upgrade macro, the developer must edit a ``versions.py`` file
which is used to update the various apps in the rose stem suite to accept the
namelist changes. The upgrade macros also form the basis of the ``rose
app-upgrade`` script applied by a user wishing to upgrade from one version of
a model to the next.

The ``versions.py`` file containing upgrade macros can be found in the
following locations:

.. tab-set::

    .. tab-item:: UM

        ``rose-meta/um-atmos/versions.py``

    .. tab-item:: JULES

        ``rose-meta/jules-standalone/versions.py``

    .. tab-item:: LFRic Core + Apps

        ``applications/<APPLICATION>/rose-meta/lfric-<APPLICATION>/versions.py``

        Variations on this theme occur, e.g. LFRic Apps science sections or
        Components in LFRic Core


Within the file a blank upgrade macro will typically look like this:

.. code-block:: python

    class vn130_tXXXX(MacroUpgrade):

        """Upgrade macro for ticket #XXXX by <author>."""

        BEFORE_TAG = "vn13.0"
        AFTER_TAG = "vn13.0_tXXXX"

        def upgrade(self, config, meta_config=None):
            """Upgrade a runtime app configuration."""
            # Input your macro commands here
            return config, self.reports

Note: The BEFORE_TAG should match the AFTER_TAG of the previous macro in the
chain. So if this is not the first macro since the release then the BEFORE_TAG
will be the version number with an added ticket number as well. For example:

.. code-block:: python

      BEFORE_TAG = "vn13.0_t123"


Example of an upgrade macro
---------------------------

Developer Sally Smith wishes to add the logical ``l_bugfix`` to the ``&run_bl``
namelist in the UM. To do this, she replaces the `XXXX` line in the upgrade
macro with her ticket number and adds herself as the author. Within the Python
function ``upgrade``, she adds the appropriate command to include the new
logical. The macro then looks like this:

.. code-block:: python

    class vn130_t1234(MacroUpgrade):

        """Upgrade macro for ticket #1234 by Sally Smith."""

        BEFORE_TAG = "vn13.0"
        AFTER_TAG = "vn13.0_t1234"

        def upgrade(self, config, meta_config=None):
            """Add l_bugfix to namelist run_bl"""
            self.add_setting(config, ["namelist:run_bl", "l_bugfix"], ".true.")
            return config, self.reports

Note that the settings added and their values are Python **strings**. This
command can then be run on a **test** branch (see :ref:`testing`).

.. note::

  Further information about upgrade macros can be found in the `Rose user guide
  <http://metomi.github.io/rose/doc/html/api/rose-upgrader-macros.html>`__.
  This contains information about more complex changes, such as removing
  variables from namelists and changing the value that a particular variable
  takes. A `tutorial
  <http://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/upgrading.html>`__
  is also available.


Upgrade Macros in LFRic
-----------------------

.. warning::

    Namelist files in application example directories are not currently updated
    by the Apply Macros script. This feature is intended to be introduced, but
    for now, developers still need to manually update those files.

The organisation of LFRic metadata is different from other repositories
(UM + Jules) as the metadata is stored with the Science or Application section
it is associated with and is then imported by other apps that require it. This
helps modularise the LFRic code but complicates macro chains.

To solve this, macros in LFRic Apps are applied using a wrapper script which
will read the added macros and combine them into the ``versions.py`` files for
the apps where that metadata is imported. Therefore when adding macros, the
macro should be added in the versions.py file in the same metadata directory
as the metadata change being made. It will then be shared as appropriate by
the ``apply_macros.py`` script.

.. tip::

    The macro will only end up in ``versions.py`` files for metadata that is
    directly imported by a rose-stem app. Therefore if adding to e.g.
    Science/gungho, the macro will be deleted from that file by the script. In
    this case ensure you are ready for the macros to be deleted, e.g. commit
    all changes.

For example, if a change to metadata is made in
``science/gungho/rose-meta/lfric-gungho``, the macro should be added to the
``versions.py`` file in that directory. This will then be copied to other
``versions.py`` files that import gungho metadata, e.g. lfric_atm, transport
etc.

It is expected that all metadata changes in LFRic Core will require change to
the rose-apps in LFRic Apps, but changes to Apps must not affect Core.
Therefore, the apply_macros script requires a working copy of LFRic Apps to
work, but will source it's own copy of Core if required. If your only changes
are to LFRic Core metadata, then you will require a linked LFRic Apps ticket
and test branch, but potentially not a development branch.

.. important::

    Some complex macro commands may be dependent on the order in which they are
    applied. As macros are copied by the wrapper script, the order they are
    applied will always be determined by the reverse metadata import order.
    For example, lfric_atm imports gungho metadata, which itself imports
    components/driver. If all 3 sections have an associated macro, then the
    macro commands would be applied in the order: components/driver, gungho,
    lfric_atm.

.. tip::

    The wrapper script will read the ``dependencies.sh`` file in your LFRic
    Apps working copy and will checkout a temporary copy of the LFRic Core
    source if required. Some Core metadata changes will also modify the Core
    rose apps. In this case make sure to also commit these changes back to the
    core branch.

To add upgrade macros to LFRic the following steps can be followed:

1. In your local LFRic Apps clone update the core source in ``dependencies.sh``
   if you have LFRic Core changes.

2. Add your upgrade macros. These **must** be added to the ``versions.py`` file
   in the same directory as the metadata being changed.

3. Run the Upgrade Macro script in a test branch(see :ref:`testing`). This is
   located in the `SimSys_Scripts github repo
   <https://github.com/MetOffice/SimSys_Scripts>`__ (at meto an up to date
   clone is available in $UMDIR/SimSys_Scripts). The syntax for running is:

.. code-block:: shell

    export CYLC_VERSION=8

    SimSys_Scripts/lfric_macros/apply_macros.py vnX.Y_tZZZZ \
        [--apps=/path/to/apps] [--core=/path/to/core] [--jules=/path/to/jules]

.. important::

    **Test branches must be used for running the Apply Macros script. Do not
    commit the changes made by apply_macros.py to a Dev Branch**

The Apps, Core and Jules options are paths to sources for each of these. Apps
will default to the present location (so it is recommended to launch from an
Apps working copy). Core and Jules will default to reading the
``dependencies.sh`` file in the Apps source if not provided.

The ``vnXX.Y_tTTTT`` option must match the After Tag of your upgrade macro.
When setting this, the version is the last released version of LFRic Apps. If
it's a linked Apps-Core ticket, then set the ticket number as the one where
the most metadata changes are being made.

.. tip::

    The apply_macros script requires python >= 3.9. At the Met Office this can
    be achieved by ``module load scitools``.
