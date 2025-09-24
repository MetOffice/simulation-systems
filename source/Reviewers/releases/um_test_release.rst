.. _um_test_release:

UM Test Release
===============

.. important::

    When referring to **all** platforms below, this means Azure Spice, EXAB,
    EXCD, EXZ

    Some of the test release only needs to be run on 1 HPC Host Zone - the
    instructions for this assume EXAB, but EXCD can be used instead. Other
    parts of the test release set up files for the main release - this needs
    to be done on both EXAB and EXCD.

Preparing Test Release Branches and Keyword Files
-------------------------------------------------

This will involve switching between your own and the umadmin account on Azure
Spice and EXAB.

* As yourself, create a UM ticket for the test release, marked 'Not for
  Builds'.
* As yourself, create and check out a UM branch at the head of the trunk
  (or whichever revision of the trunk you wish to do a test release with).
* As yourself, create and check out a head of trunk meta branch
  (``fcm:um_meta.x_tr@head``).
* As umadin, setup the ``~/.metomi/fcm/keyword.cfg`` file on Azure Spice to
  specify custom keywords for the UM, JULES, SOCRATES, CASIM, Shumlib, UKCA
  and the mirrors of each of these named after the upcoming version and
  pointing to the current head of trunk revisions of each project. No keywords
  are needed for mule, moci or meta repositories.
* The general format looks like this- substitute model version and revisions

    * Remember to remove any existing hashtags/make sure these lines aren't
      commented out
    * For the test release we also need to set the Jules vn keyword(last line).
      This needs to match the jules version that is passed to
      release_new_version script below.

.. code-block::

    revision[um.x:vn13.5]        = 123059
    revision[jules.x:um13.5]     = 28020
    revision[socrates.x:um13.5]  = 1563
    revision[casim.x:um13.5]     = 10951
    revision[shumlib.x:um13.5]   = 7324
    revision[ukca.x:um13.5]      = 3196

    revision[um.xm:vn13.5]       = 123059
    revision[jules.xm:um13.5]    = 28020
    revision[socrates.xm:um13.5] = 1563
    revision[casim.xm:um13.5]    = 10951
    revision[shumlib.xm:um13.5]  = 7324
    revision[ukca.xm:um13.5]     = 3196

    revision[jules.xm:vn7.5]     = 28020

* As umadmin, scp this file to the EXAB, ``scp ~/.metomi/fcm/keyword.cfg
  login.exab.sc:.metomi/fcm/keyword.cfg``
* As yourself, copy this file into your own homespace ready for testing later,
  ``cp ~umadmin/.metomi/fcm/keyword.cfg ~/.metomi/fcm/keyword.cfg``. Do this
  on Azure Spice and EXAB.
* As yourself, add the following to ``~/.metomi/rose.conf`` on Azure Spice and
  EXAB. This prevents kgo failures due to the new version number when we test
  later. Again, do this on Azure Spice and EXAB.

.. code-block::

    [rose-ana]
    bypass-version-check=.true.


Running the Release Script
--------------------------

As yourself, move into the rose-stem directory in the UM working copy where the
release new version script will be run from. The syntax is,

.. code-block:: shell

    ../admin/rose-stem/release_new_version.py -c <previous version> -n <new version> -j <new *JULES* version>
    eg. ../admin/rose-stem/release_new_version.py -c 13.4 -n 13.5 -j 7.5

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

As yourself, the next step is to move the macros and metadata into the meta
branch. The metadata will have been created already by the release script.
Below shows an example of the commands run to move from 11.4 to 11.5, from the
top directory of the working copy of the UM branch,

.. code-block:: shell

    version="version114_115.py"
    vn="vn11.5"
    path="/path/to/meta/working_copy"

    fcm mv rose-meta/um-atmos/$version $path/um-atmos/$version
    fcm mv rose-meta/um-fcm-make/$version $path/um-fcm-make/$version
    fcm mv rose-meta/um-createbc/$version $path/um-createbc/$version

    fcm mv rose-meta/um-atmos/$vn $path/um-atmos/$vn
    fcm mv rose-meta/um-fcm-make/$vn $path/um-fcm-make/$vn
    fcm mv rose-meta/um-createbc/$vn $path/um-createbc/$vn

Note: there is no need to move um-crmstyle as it only contains HEAD metadata.

Manually add a line to each of the ``um-atmos/versions.py``,
``um-fcm-make/versions.py`` and ``um-createbc/versions.py`` files in the meta
branch to import the newly copied ``versionXX_XY.py`` file.

Commit the changes to both the UM and Meta branches.


Installing Ctldata, Utilities and Prebuilds
-------------------------------------------

These steps are all done as umadmin

Check out the UM trunk into a working copy. umadmin can only check out from the
mirror - if immediately following the previous steps, ensure the mirror has
updated.

.. code-block:: shell

    fcm co fcm:um.xm_tr@vnX.Y umX.Y_install
    cd umX.Y_install

First check that the upgrade has gone successfully and the new install will
appear in the correct place. Do this by running,

.. code-block:: shell

    rose stem --group=install rose-stem -S CENTRAL_INSTALL=false \
        -S PREBUILDS=false -S USE_EXAB=true
    cylc play <name-of-suite>

and check that ``~umadmin/cylc_run/<working_copy_name>/runN/share/vnX.Y``
exists and is the new version number. If that has worked, change the
CENTRALL_INSTALL flag to true and rerun,

.. code-block:: shell

    rose stem --group=install rose-stem -S CENTRAL_INSTALL=true \
        -S PREBUILDS=false -S USE_EXAB=true
    cylc play <name-of-suite>

Now install the prebuilds by running,

.. code-block:: shell

    rose stem --group=prebuilds -S MAKE_PREBUILDS=true \
        --workflow-name=vnX.Y_prebuilds --no-run-name

.. tip::

    In the main release, we use cylc7 for the prebuild install as the Cylc8
    rose-stem is missing a feature. As we are going to be removing these
    prebuilds shortly, the default Cylc8 is fine for the test release.

Navigate to the input data directory on azure spice
(``$UMDIR/standard_jobs/inputs``) and run the following command which copies
the old directory to the new one, and then creates a new symlink. Replace 11.5
and 11.6 with the correct version numbers,

.. code-block:: shell

    mv vn11.5 vn11.6 && ln -s vn11.6 vn11.5

Repeat this step on **all of** EXAB, EXCD and EXZ.


Test the Branch
---------------

These steps are done as yourself. In your UM branch working copy, ensure the
``PREBUILDS`` variable in ``rose-stem/site/meto/variables.cylc`` is set to
true so we test the new prebuilds. Then run the entire test suite,

.. code-block:: shell

    rose stem --group=all --source=. --source=/path/to/meta/working/copy
    cylc play <name-of-suite>

Before continuing the next step you should make sure the suite has run as
expected. All tests should pass apart from any tasks that output netcdf
(these have _nc in the tasks name) and the SCM tasks. Both of these encode the
UM version and use a direct comparison, it is not as simple to exclude UM
version from the comparison as we did with tests that use mule-cumf.

.. tip::

    Check the test results by running something like

    .. code-block::

        find ~cylc-run/<suite name>/runN/log/job -path "*rose_ana*" -type f \
            -name job.status \
            | xargs grep -l CYLC_JOB_EXIT=ERR \
            | grep -vE "(scm|netcdf)


Test on Monsoon
---------------

It's also sensible to check now that nothing has broken on Monsoon. Do this by
copying your keyword settings across to your account on there. Then check out
the UM main and meta branches and run the test suite as you in the previous
section except for the group which should now be ``ex1a``.


Reset Keywords and Remove Prebuilds (Important!)
------------------------------------------------

As both yourself and umadmin,

* Remove or comment out the custom keyword revisions from
  ``~/.metomi/fcm/keywords.cfg``
* Remove or comment out the ``bypass-version-check`` in
  ``~/.metomi/rose.conf``

    * Make sure to do this on **all** platforms (inlcuding Monsoon)
    * Not doing so can result in some weird behaviour down the line

* As umadmin, remove the installed release and prebuilds. Doing this now saves
  significant time during the actual release. These steps should only need
  doing on Azure Spice and EXAB.

    * Delete the ``$UMDIR/vnX.Y`` directory
    * On Azure Spice, run ``cylc clean --timeout=5000 vnX.Y_prebuilds``. Once
      this has finished, check the cylc-run directory that the suite has been
      removed. Do this on all of $HOME, $DATADIR, $SCRATCH on both Azure Spice
      and EXAB.

The test release is now done!
