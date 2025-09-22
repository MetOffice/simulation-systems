.. _jules_release:

Jules Release
=============

Create a ticket and Create Branches
-----------------------------------

To document the process create a ticket and put a link to it on the release
curation ticket. You may wish to include links to the UM branch and a wiki
page for the reviews.

.. code-block::

    Documents the 'Build and install the Jules release'

    NOTES: Any changes required that are not a direct instruction from this
    section of the guide.

    '''Branch :''' [log:main/branches/dev/branch_path_n_name dev/branch_path_n_name]
    '''[wiki:ticket/ticket_no/CodeSystemReview Code/System Review]'''


Create and check out a head of trunk Jules branch. Then update the ticket
description.

.. code-block:: shell

    fcm bc -k ticket_no vn5.9_jules_release fcm:jules.x_tr
    fcm co fcm:jules.x_br/dev/username/r12345_vn5.9_jules_release


Metadata Changes
----------------

* First, change the user guide URLs in the ``HEAD`` metadata for
  ``jules-fcm-make`` and ``jules-standalone`` from "latest". This is done
  automatically by running the ``create_jules_version_metadata.py`` script
  from the ``rose-stem`` directory.

    .. code-block:: shell

        cd rose-stem
        ./bin/create_jules_version_metadata.py 5.8 5.9

* Run ``rose config-dump`` to ensure that the metadata files are in the common
  format (do this from the top-level of the working copy)
* Copy ``rose-meta/jules-standalone/versions.py`` to an appropriately named
  file, e.g. for the JULES vn5.9 release, the file is called
  ``rose-meta/jules-standalone/version58_59.py``.

  .. code-block:: shell

    fcm cp rose-meta/jules-standalone/versions.py rose-meta/jules-standalone/version58_59.py

* Edit ``rose-meta/jules-standalone/versions.py`` to:

    * Remove the upgrade macros
    * Import the macros from the newly created file, e.g.

    .. code-block:: python

        ...
        from .versionUU_YY import *
        ...

        class vnYY_txxxx(MacroUpgrade):

            """Upgrade macro from JULES by Author"""

            BEFORE_TAG = "vnY.Y"
            AFTER_TAG = "vnY.Y_txxxx"

            def upgrade(self, config, meta_config=None):
                """Upgrade a JULES runtime app configuration."""

                # Add settings
                return config, self.reports

* Edit ``rose-meta/jules-standalone/version<from>_<to>.py`` such that,

    * Imports of other macros are removed
    * Add a new blank upgrade macro that bumps the version to the release
      version,

    .. code-block:: python

        class vn58_vn59(MacroUpgrade):
            """Version bump macro"""

            BEFORE_TAG = "vn5.8_txxx"
            AFTER_TAG = "vn5.9"

            def upgrade(self, config, meta_config=None):
                # Nothing to do
                return config, self.reports

  * Add a similar version bump macro to
    ``rose-meta/jules-fcm-make/versions.py``.

* Check that the list of options on line 96 in
  ``rose-meta/jules-fcm-make/HEAD/rose-meta.conf`` includes all the ones
  listed in directory ``etc/fcm-make/platform/`` (ignoring custom.cfg,
  envars.cfg and load_settings.cfg).
* Commit the metadata changes


Rose Stem Updates
-----------------

* Update the ``VN`` variable in ``rose-stem/rose-suite.conf``.
* Upgrade the rose-stem apps as normal, using the upgrade macro added earlier,
  e.g.

    .. code-block:: shell

        ./bin/upgrade_jules_test_apps vn5.9

* Update ``KGO_VERSION`` in ``rose-stem/include/variables.rc`` to the release
  version, making a note of original version number.
* Login as julesadmin and create new KGO directories for the release by copying
  the old kgo to a new directory named ``vnX.Y``. See `the kgo install
  instructions <https://code.metoffice.gov.uk/trac/jules/wiki/KGOInstall>`_
  for paths to the kgo install.

    .. code-block:: shell

        xsudo -i -u julesadmin

        # Azure Spice
        PREVIOUS=vn5.8_txxx
        RELEASE=vn5.9
        cd <KGO_DIR>
        cp -r ./$PREVIOUS ./$RELEASE

        # EXAB
        # From your desktop
        ssh -Y login.exab.sc
        PREVIOUS=vn5.8_txxx
        RELEASE=vn5.9
        cd <KGO_DIR>
        cp -r ./$PREVIOUS ./$RELEASE

        # From EXAB, rsync to EXCD & EXZ:
        rsync -avz <KGO_DIR>/$RELEASE login.excd.sc:<KGO_DIR>
        rsync -avz <KGO_DIR>/$RELEASE login.exz:<KGO_DIR_EXZ>
        exit
        exit

* Commit the rose-stem changes and then run the Jules and UM rose-stem suites
  to ensure nothing has broken.


Code Review and Commit
----------------------

Pass the Jules ticket along for code review and commit. Once done, :ref:`Tag
<reference-tagging>` the trunk with the new version number (a ``umX.Y`` tag
can also be added if the UM release number is known).


Release Notes
-------------

These are done with a PR in `this github repo
<https://github.com/jules-lsm/jules-lsm.github.io>`__

Often the release notes will have been prepared beforehand and have their own
ticket. In this case it makes more sense for you to review and commit that
branch. See below for the relevant steps and the how to commit page for
instructions.

The user guide contains release notes for each JULES version which should
detail any major commits.

#. Create a new file at ``user_guide/doc/source/release_notes/JULESX-X.rst``,
   probably by copying from a previous release
#. Go through the trunk commits since the last release and decide whether the
   change is worth noting
#. Use the ticket details to describe the change
#. For some large commits, it is worth contacting the original author for a few
   sentences
#. Add the new file to the contents, at the top -
   ``user_guide/doc/source/release_notes/contents.rst``
#. Update the version number in ``docs/user_guide/source/conf.py`` and check
   the copyright variable is correct.

To build the docs, move into the ``user_guide/doc`` directory. At meto,
``module load scitools`` will also need to have been run.

.. code-block:: shell

    # For html pages
    make html
    firefox build/html/index.html

    # For latex pdfs
    make latexpdf
    gio open build/latex/JULES_User_Guide.pdf


Publicise the Release
---------------------

Update the wiki:

* Update the table on the front page of this wiki to note the release.
* Create a new standard jobs page for the upcoming release cycle - compare the
  list of apps in the table to that in the rose-stem/apps directory.
* Mark the wiki milestone for the release as completed (this should give the
  option to move open tickets to a different milestone)

Notify the JULES community:

* Post a message to the JULES Users mailing list:

    * JULES-USERS@MAILLISTS.READING.AC.UK
    * JULES@MAILLISTS.READING.AC.UK

* Post a message to the simulation-systems GitHub Discussions board
