.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _um_test_release:

UM Test Release
===============

.. important::

    When referring to **all** platforms below, this means Azure Spice, EXAB,
    EXCD, EXZ

    Some of the test release only needs to be run on 1 HPC Host Zone - the
    instructions for this assume EXAB, but EXCD can be used instead. Other
    parts of the test release set up files for the main release - this needs
    to be done on both EXAB EXCD and EXZ.

Preparing Test Release Branches and Keyword Files
-------------------------------------------------

.. note::

    These steps require switching between your own account and the ``umadmin``
    account on Azure Spice and EXAB/CD.

1. **Create a tracking issue**:   Using your own account,
   `open a new UM Issue <https://github.com/MetOffice/um/issues/new>`_
   to track the test release.

2. **Sync your forks**:   Ensure you have :ref:`forks <forking>` of both the
   ``um`` and ``um_meta`` repositories, and :ref:`update <syncing_fork>`
   the ``main`` branch in each to match the upstream repository.

3. **Create your working branches**: In a local clone of each fork,
   :ref:`create a new branch <create_branch>` off ``main``. Link both branches
   to your UM Issue.

4. **Update dependencies.yaml**: In your new ``um`` branch,
   open ``dependencies.yaml`` and make the following changes so testing uses the
   latest repository heads:

   - Point ``um_meta`` to your new ``um_meta`` branch.
   - Point all other entries to ``main``.

5. **Configure Rose to bypass version checks**: Using your own account on both
   Azure Spice and EXAB/CD, add the following lines to ``~/.metomi/rose.conf``
   to prevent KGO failures from the new version number during testing:

   .. code-block:: ini

      [rose-ana]
      bypass-version-check=.true.


Running the Release Script
--------------------------

Move into the rose-stem directory in the UM clone. This is where the release
new version script will be run from. The syntax is,

.. code-block:: shell

    ../admin/rose-stem/release_new_version.py -c <previous version> -n <new version> -j <new *JULES* version> --test
    eg. ../admin/rose-stem/release_new_version.py -c 13.4 -n 13.5 -j 7.5 --test

.. note::

    Adding ``--test`` will prevent the script from updating the Jules version
    in the metadata which is needed as the new Jules tag will not yet exist.

* Open a new terminal and inspect that the version number update macro added by
  the script is correct, and that the tXXXX template macro has been deleted
  appropriately.

  * This has caused problems before see `this edge case
    <https://code.metoffice.gov.uk/trac/um/wiki/ticket/2437/SciTechReview>`.
    The upgrade macro should fail to execute if the macro chain is
    incorrect, as it won't be able to upgrade an app to the new version -
    this is likely this edge case.

* As there is no kgo installed for the new version revert the changes to
  ``rose-stem/site/meto/variables_*.cylc`` as well as the ``BASE`` variable at
  the bottom of ``rose-stem/site/meto/variables.cylc``.

Copying the metadata and upgrade macros to the um_meta branch
-------------------------------------------------------------

The next step is to move the macros and metadata into the meta branch. The
metadata will have been created already by the release script. For each of the
``um-atmos``, ``um-fcm-make`` and ``um-createbc`` metadata sections, move the
new ``vnX.Y`` directory into the ``um_meta`` clone, eg.

.. code-block:: shell

    mv rose-meta/um-atmos/vnX.Y /path/to/meta_clone/um-atmos/
    cd /path/to/meta_clone
    git add um-atmos/vnX.Y

Note, there is no need to move um-crmstyle as it only contains HEAD metadata.

In the ``um_meta`` clone, manually add a line to each of the
``um-atmos/versions.py``, ``um-fcm-make/versions.py`` and
``um-createbc/versions.py`` files to import the newly copied ``versionXX_XY.py``
file (see the existing line).

Commit the changes to both the UM and Meta branches.


Installing Ctldata, Utilities and Prebuilds
-------------------------------------------

.. note::

   Run all steps in this section as the ``umadmin`` user. Log in with your own
   account first, then switch users by running ``sudo -iu umadmin``.

Copy your local ``um`` and ``um_meta`` repository clones into the ``umadmin``
workspace (preferably in ``~umadmin/umX.Y_test_release``).

First check that the upgrade has gone successfully and the new install will
appear in the correct place. Do this by running,

.. code-block:: shell

    cylc vip -z g=install -S CENTRAL_INSTALL=false -S USE_EXAB=true -n umX.Y_test_release ./rose-stem

and check that ``cylc_run/<working_copy_name>/runN/share/vnX.Y`` exists and is
the new version number. If that has worked, change the ``CENTRALL_INSTALL`` flag
to true and rerun,

.. code-block:: shell

    cylc vip -z g=install -S CENTRAL_INSTALL=true -S USE_EXAB=true -n umX.Y_test_release ./rose-stem

Navigate to the input data directory on azure spice
(``$UMDIR/standard_jobs/inputs``) and run the following command which copies
the old directory to the new one, and then creates a new symlink. Replace 11.5
and 11.6 with the correct version numbers,

.. code-block:: shell

    mv vn11.5 vn11.6 && ln -s vn11.6 vn11.5

Repeat this step on **all of** EXAB, EXCD and EXZ.


Test the Branch
---------------

These steps are done as yourself. In your UM branch clone ensure the meta branch
is set in the ``dependencies.yaml`` file and then run the entire test suite,

.. code-block:: shell

    cylc vip -z g=all -S USE_EXAB=true -n umX.Y_test_release ./rose-stem

Before continuing the next step you should make sure the suite has run as
expected. All tests should pass apart from any tasks that output netcdf
(these have _nc in the tasks name) and the SCM tasks. Both of these encode the
UM version and use a direct comparison, it is not as simple to exclude UM
version from the comparison as we did with tests that use mule-cumf.

.. tip::

  Check the test results using the Cylc Tui or GUI or by running something like

  .. code-block::

    find ~cylc-run/<suite name>/runN/log/job -path "*rose_ana*" -type f \
        -name job.status \
        | xargs grep -l CYLC_JOB_EXIT=ERR \
        | grep -vE "(scm|netcdf)


Test on Monsoon
---------------

It's also sensible to check now that nothing has broken on Monsoon. Do this by
cloning the UM main and meta branches and run the test suite as you did in the
previous section except for the group which should now be ``ex1a``.

.. note::

    At the time of writing, the solution for extracting from GitHub on monsoon
    is unknown


Reset Keywords and Remove Prebuilds (Important!)
------------------------------------------------

As both yourself and umadmin,

* Remove or comment out the ``bypass-version-check`` in
  ``~/.metomi/rose.conf``

  * Make sure to do this on **all** platforms (inlcuding Monsoon)
  * Not doing so can result in some weird behaviour down the line

* As umadmin, remove the installed release, by deleting the ``$UMDIR/vnX.Y``
  directory

The test release is now done!
