.. _macros:

Upgrade Macros
==============

To create an upgrade macro, the developer must edit a ``versions.py`` file which is used
to update the various apps in the rose stem suite to accept the namelist changes. The upgrade
macros also form the basis of the ``rose app-upgrade`` script applied by a user wishing to
upgrade from one version of a model to the next.

The  ``versions.py`` file containing upgrade macros can be found in the following locations:

+------------------+----------------------------------------------+
| Project          | Location                                     |
+==================+==============================================+
| UM               |  ``rose-meta/um-atmos/versions.py``          |
+------------------+----------------------------------------------+
| JULES            |  ``rose-meta/jules-standalone/versions.py``  |
+------------------+----------------------------------------------+
| UKCA / CASIM /   | Upgrade macros not currently used by these   |
|                  |                                              |
| LFRic / SOCRATES | projects.                                    |
+------------------+----------------------------------------------+

Within the file a blank upgrade macro will typically look like this:

.. code-block::

  class vn130_tXXXX(MacroUpgrade):

      """Upgrade macro for ticket #XXXX by <author>."""

      BEFORE_TAG = "vn13.0"
      AFTER_TAG = "vn13.0_tXXXX"

      def upgrade(self, config, meta_config=None):
          """Upgrade a runtime app configuration."""
          # Input your macro commands here
          return config, self.reports


Example of an upgrade macro
---------------------------

Developer Sally Smith wishes to add the logical ``l_bugfix`` to the
``&run_bl`` namelist in the UM. To do this, she replaces the `XXXX`
line in the upgrade macro with her ticket number and adds herself
as the author. Within the Python function ``upgrade``, she adds the
appropriate command to include the new logical. The macro then looks
like this:

.. code-block::

  class vn130_t1234(MacroUpgrade):

      """Upgrade macro for ticket #1234 by Sally Smith."""

      BEFORE_TAG = "vn13.0"
      AFTER_TAG = "vn13.0_t1234"

      def upgrade(self, config, meta_config=None):
          """Add l_bugfix to namelist run_bl"""
          self.add_setting(config, ["namelist:run_bl", "l_bugfix"], ".true.")
          return config, self.reports

Note that the settings added and their values are Python **strings**.
This command can then be run on a **test** branch (see :ref:`testing`).

.. note::

  Further information about upgrade macros can be found in the
  `Rose user guide <http://metomi.github.io/rose/doc/html/api/rose-upgrader-macros.html>`_.
  This contains information about more complex changes, such as removing variables from
  namelists and changing the value that a particular variable takes.
  A `tutorial <http://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/upgrading.html>`_
  is also available.
