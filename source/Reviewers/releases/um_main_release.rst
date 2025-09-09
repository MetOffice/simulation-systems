.. _um_main_release:

UM Main Release
===============

Create a ticket and Create Branches
-----------------------------------

To document the process create a ticket and put a link to it on the release
curation ticket. You may wish to include links to the UM and UM metadata
branches required and a wiki page for the reviews.

.. code-block::

    Documents the 'Build and install the <main/test> UM release'

    NOTES: Any changes required that are not a direct instruction from this section of the guide.

    '''Branch :''' [log:main/branches/dev/branch_path_n_name dev/branch_path_n_name]
    '''Meta Branch :''' [log:meta/branches/dev/branch_path_n_name dev/branch_path_n_name]
    '''[wiki:ticket/ticket_no/CodeSystemReview Code/System Review]'''


Create and check out both a head of trunk UM branch and a head of trunk UM meta
branch. Then update the ticket description.

.. code-block:: shell

    fcm bc -k ticket_no vn11.5_um_release fcm:um.x_tr
    fcm co fcm:um.x_br/dev/username/r12345_vn11.5_um_release
    fcm bc -k ticket_no vn11.5_meta_release fcm:um_meta.x_tr
    fcm co fcm:um_meta.x_br/dev/username/r12345_vn11.5_meta_release


Tagging Feeder Trunks
---------------------

* :ref:`Tag <reference-tagging>` the head of the feeder repositories with
   keywords for the new UM version if they do not already exist.

* ``fcm:casim.x``
* ``fcm:jules.x``
* ``fcm:shumlib.x``
* ``fcm:socrates.x``
* ``fcm:ukca.x``

Send an email to all repository owners to let them know that the the head of
the trunk has been tagged.

.. note::

    Jules should already have been done by the Jules release, but this is worth
    checking.


Apply Code Styling
------------------

* Switch to the UM branch
* Set ``export RUNFULL=1`` then run ./admin/code_styling/apply_styling
* If any files have changed, check nothing has gone wrong with a quick compile
  ``rose stem --group=fcm_make_ex1a_gnu_um_rigorous_omp``
* Commit any changes


Checking Metadata and Rose Apps
-------------------------------

The JULES release must be completed first and all jules-shared metadata changes
from the JULES repository must be centrally installed before progressing.

* First switch to the UM branch.
* Check that the metadata meets the Rose standards: run ``rose config-dump -C
  rose-meta``. Do this before running release_new_version, so that any
  metadata errors are fixed before the new vnX.Y metadata directories are
  created, otherwise you'll have to check both vnX.Y and HEAD.

    * Run ``fcm diff`` on HEAD. Are the changes sensible? They often just
      involve moving sections of meta-data to be in the correct alphabetical
      order. However, `UM:#1824
      <https://code.metoffice.gov.uk/trac/um/ticket/1824>`__ added comments
      for some additional triggers ([43853]) to circumvent a bug in Rose.
      Running config-dump will move the location of these comments to the
      bottom of the that item's metadata. Check for any moved references
      to "issue 2107" (there should be 4 of them) and put them back in the
      right places by hand, by referring to an unaltered copy of the trunk.

* Check rose-stem meets the Rose standards: run ``rose config-dump -C
  rose-stem/app``. The version upgrade macro should have reformatted all the
  atmos and fcm-make apps, so they should be correct. Are there any other
  changes (e.g. to rose-ana apps)? Are they understood? Commit them to the
  branch or discuss with the team as appropriate.
* Commit all changes before moving onto the next section


Running the Release Script
--------------------------

Move into the rose-stem directory in the UM working copy where the release new
version script will be run from. The syntax is,

.. code-block:: shell

    ../admin/rose-stem/release_new_version.py -c <previous version> -n <new version> -j <new *JULES* version>
    eg. ../admin/rose-stem/release_new_version.py -c 13.4 -n 13.5 -j 7.5

* Open a new terminal and inspect that the version number update macro added by
  the script is correct, and that the tXXXX template macro has been deleted
  appropriately.

    * This has caused problems before see `this edge case
      <https://code.metoffice.gov.uk/trac/um/wiki/ticket/2437/SciTechReview>`_.
      The upgrade macro should fail to execute if the macro chain is
      incorrect, as it won't be able to upgrade an app to the new version -
      this is likely this edge case.


Copying the metadata and upgrade macros to the um_meta branch
-------------------------------------------------------------

The next step is to move the macros and metadata into the meta branch. The
metadata will have been created already by the release script. Below shows an
example of the commands run to move from 11.4 to 11.5, from the top directory
of the working copy of the UM branch,

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
branch to import the newly copied versionXX_XY.py file.

Commit the changes to both the UM and Meta branches.


Final Checks
------------

**UM AUX Changes**

If there are changes to the AUX trunk in this release, are we picking up the
head of the AUX trunk (fcm:um_aux)? A new keyword will need to be created and
copied into the rose-stem/rose-suite.conf file.

.. code-block:: shell

    fcm co -q -N fcm:um_aux.x aux
    fcm log -l1 fcm:um_aux.x/trunk
    cd aux
    fcm pe fcm:revision .
    fcm commit

.. warning::

    Updating ``HOST_SOURCE_UM_AUX`` with the new keyword is NOT done
    automatically by release_new_version.py as it doesn't need to be done
    every release

**Other Points**

* Make sure the prebuilds are set to ``true`` in the
  ``site/meto/variables.cylc`` by checking the line, ``{% do SITE_VARS.update(
  {"PREBUILDS" : true}) %}``
* Check rose-stem/rose-suite.conf?

    * Are the UM, JULES, SOCRATES, CASIM and UKCA versions correct? These
      should be the keywords setup earlier.
    * Is housekeeping ``true``?
    * Are the KGO versions correct in the ``variables.cylc`` file for each
      site?
    * Does the minimum version of Rose/Cylc need to be increased? (Do any
      rose-ana changes require new functionality?)
    * Do any of the apps or parts of the suites reference ``$UMDIR`` - they
      shouldn't (the correct thing to do is to reference
      ``$UM_INSTALL_DIR``).

* ``grep`` for any instances of the old version keyword(s). Fix as required and
  add any corrections to the instructions on this page too.

Commit any changes resulting from these final checks.


Preparing to Test
-----------------

.. important::

    When referring to **all** platforms below, this means Azure Spice, EXAB, EXCD, EXZ


* Check that a ``$UMDIR/standard_jobs/inputs/vnX.Y`` input data directory
  exists in UMDIR on **all** platforms - this should have been done as part of
  the test release.

    * If not, rename the inputs directory ``$UMDIR/standard_jobs/inputs/vnX.Y``
      to the new version number and be sure to symlink the previous version to
      it. Do this all on one line to minimise any glitches during the rename.
      This needs to be repeated on all platforms. i.e. to update from vn11.5
      to vn11.6 one would run, ``mv vn11.5 vn11.6; ln -s vn11.6 vn11.5``.

* Local keywords for the UM should be put in your ``~/.metomi/fcm/keyword.cfg``
  file on **all** platforms (don't forget to remove them afterwards). The tag
  should correspond to the version you are releasing and the version number
  should be the revision of the trunk from which you branched. For example:

  .. code-block::

    revision[um.x:vn10.0]                    = 112
    revision[um.xm:vn10.0]                   = 112

* For the rose_ana tasks to pass new KGO also needs to be generated for the new
  version, since you are about to run the ``all`` group test anyway you should
  use this opportunity to produce a new set of KGO.

    * KGO is installed using the scripts in SimSys_Scripts. In order for the
      script to work you must first change the KGO directories in the
      ``variables.cylc`` and platform-specific ``variables_PLATFORM.cylc``
      files back to whichever versions were present before the
      ``release_new_version.py`` script was run - you can do this with a
      simple copy from the head of the trunk. Be careful to ensure this is
      only changing the KGO versions for each variable as expected. **DO NOT
      COMMIT this change - you will be reverting it later**.

    .. code-block:: shell

        fcm export --force fcm:um.x_tr/rose-stem/site/meto/variables.cylc \
            rose-stem/site/meto/

        fcm export --force fcm:um.x_tr/rose-stem/site/meto/ \
            variables_azspice.cylc rose-stem/site/meto/

        fcm export --force \
            fcm:um.x_tr/rose-stem/site/meto/variables_ex1a.cylc \z
            rose-stem/site/meto/

    * Current KGO files will have the older UM version in the fixed length
      header and lookups. In order for the rose-ana tasks that use mule-cumf
      to not give false rose-ana failures we must temporarily ignore the model
      version. There is some logic in the UM rose stem suite to enable this.
      Open your ``~/.metomi/rose.conf`` file, on **all** platforms, and add
      the following lines to the rose-ana section, making sure that
      bypass-version-check is true:

    .. code-block::

        [rose-ana]
        bypass-version-check=.true.


Testing and KGO Generation
--------------------------

As yourself, and in the working copy of the UM branch run rose stem, be sure
not to forget the source argument to the UM metadata branch,

.. code-block:: shell

    rose stem --task=all -S PREBUILDS=false -S HOUSEKEEPING=false \
        -S USE_EXAB=true --source=. --source=/path/to/metadata/working_copy

    cylc play <name-of-suite>

Before continuing the next step you should make sure the suite has run as
expected. All tests should pass apart from any tasks that output netcdf
(these have _nc in the tasks name) and the SCM tasks. Both of these encode the
UM version and use a direct comparison, it is not as simple to exclude UM
version from the comparison as we did with tests that use mule-cumf.

.. tip::

    Check the test results by running something like

    .. code-block:: shell

        find ~cylc-run/<suite name>/runN/log/job -path "*rose_ana*" -type f \
            -name job.status \
            | xargs grep -l CYLC_JOB_EXIT=ERR \
            | grep -vE "(scm|netcdf)"

The ``meto_update_kgo.sh`` script is stored in SimSys_Scripts. As yourself,
navigate to ``$UMDIR/SimSys_Scripts/kgo_updates`` directory and run
``./meto_update_kgo.sh --new-release`` and follow its instructions.

* First it will ask for all platforms run on, ``azspice ex1a``
* It will ask which Host Zone the tests ran on - we specified EXAB so choose
  that (Host Zone 1).
* You will need to supply the username and suitename of the suite you ran
  above. This will need to include the ``runX`` directory.
* The version number should be the new version.
* The ticket number won't be used but can be entered as the ticket associated
  with the release.
* When asked how the new kgo directory should be named overwrite the default
  with the name ``vnX.Y`` where this is the new version number.
* It will show you the settings to double check before you continue.

    * Pay particular attention to the preview of the list of commands the
      script will present you with to ensure it has accounted for all expected
      KGO files.

* The script will install the new kgo on every platform in order azspice->ex1a.
  Once these are finished installing it will rsync to the EXCD and EXZ. To
  install the entire kgo database will take some time.

Once you believe you have installed the KGO you should fcm revert the changes
you made to the variables*.cylc files to reset the KGO variables, ``fcm revert
rose-stem/site/meto/variables*``

The test suite should now be rerun to confirm the kgo has been installed
properly. As we can't restart Cylc8 rose-stem suites, the entire thing needs
to be rerun. We're just checking that the kgo has been installed, so it's
probably unnecessary to wait for the entire thing - instead just ensure a
reasonable range of rose-ana tasks have passed.

.. tip::

    Has the ability to reload the test suite been enabled yet? If so ``cylc
    vr`` can likely be used to restart the original suite. These instructions
    also need updating!


Review and Commit
-----------------

Ensure all changes are committed to both branches and then pass along for a
review to someone in the team.

Notes for Reviewer:

* In ``rose-stem/site/meto/variables``, ensure the ``PREBUILDS`` variable near
  the top is set to true.
* Once happy, commit both the meta and main branches, and return the ticket to
  the developer.

Now :ref:`tag <reference-tagging>` the trunk with the ``vnX.Y = RRR`` tag.

**Now make sure to revert changes to ``~/.metomi/fcm/keyword.cfg`` on all
platforms**


Install the Release
-------------------

The main installation of ctldata, utilities and prebuilds can now take place.
This all takes place as the ``umadmin`` account so log in to that now.

Delete any remaining temporary vnX.Y keywords for umadmin/umtest, on **all**
platforms. Check all keyword.cfg files, and do both accounts now. They could
be left over from the earlier test build, even if you didn't set them.

Check out the UM trunk into a working copy. ``umadmin`` can only check out from
the mirror.

.. code-block:: shell

    fcm co fcm:um.xm_tr@vnX.Y umX.Y_install
    cd umX.Y_install

First check that the upgrade has gone successfully and the new install will
appear in the correct place. Do this by running,

.. code-block:: shell

    rose stem --group=install -S CENTRAL_INSTALL=false -S PREBUILDS=false \
        -S USE_EXAB=true

    cylc play <name-of-suite>

and check that ``~umadmin/cylc_run/<working_copy_name>/runN/share/vnX.Y``
exists and is the new version number. If that has worked, change the
CENTRALL_INSTALL flag to true and rerun,

.. code-block:: shell

    rose stem --group=install -S CENTRAL_INSTALL=true -S PREBUILDS=false \
        -S USE_EXAB=true

    cylc play <name-of-suite>


Next, rerun the install for the 2nd host zone,

.. code-block:: shell

    rose stem --group=ex1a_install -S CENTRAL_INSTALL=true \
        -S PREBUILDS=false -S USE_EXCD=true

    cylc play <name-of-suite>

Finally, rerun the install for the EXZ,

.. code-block:: shell

    rose stem --group=ex1a_install -S CENTRAL_INSTALL=true \
        -S PREBUILDS=false -S USE_EXZ=true

    cylc play <name-of-suite>

The release is now installed and can be announced.

Make Release Prebuilds
----------------------

Now it is time to install the prebuilds.

.. important::

    Use Cylc 7 (``export CYLC_VERSION=7``) to install the prebuilds. It is
    important to set the source to the UM fcm mirror in the commands below,
    and use the config option to point at the rose-stem directory. If this
    wasn't done, prebuild availability would depend on the host machine you
    are currently on being available. rose-stem in cylc8 doesn't support this,
    hence using cylc7.

    A fix for this will likely become available with the move to git. The
    timescales for that are shorter than for removing Cylc7.

First install the prebuilds on Azure Spice and EXAB,

.. code-block:: shell

    export CYLC_VERSION=7
    rose stem --group=prebuilds --source=fcm:um.xm_tr@vnX.Y \
        --name=vnX.Y_prebuilds --config=./rose-stem \
        -S MAKE_PREBUILDS=true -S USE_EXAB=true

And then on the EXCD - make sure to **not** use ``--new`` in this command or
the previous set will have been overwritten.

.. code-block:: shell

    export CYLC_VERSION=7
    rose stem --group=ex1a_fcm_make,ex1a_fcm_make_portio2b \
        --source=fcm:um.xm_tr@vnX.Y --name=vnX.Y_prebuilds \
        --config=./rose-stem -S MAKE_PREBUILDS=true -S USE_EXCD=true

And finally on the EXZ - make sure to **not** use ``--new`` in this command or
the previous set will have been overwritten.

.. code-block:: shell

    export CYLC_VERSION=7
    rose stem --group=ex1a_fcm_make,ex1a_fcm_make_portio2b \
        --source=fcm:um.xm_tr@vnX.Y --name=vnX.Y_prebuilds \
        --config=./rose-stem -S MAKE_PREBUILDS=true -S USE_EXZ=true


Monsoon Installation
--------------------

.. tip::

    This section can be done in parallel with the previous one

We also install the UM onto Monsoon - to do this you will need a Monsoon
account with access to the ``umadmin.mon`` shared account.

First, log into Monsoon as ``umadmin.mon`` and then check out the trunk at the
new version just released.

.. code-block:: shell

    fcm co fcm:um.xm_tr@vnXX.Y

Next, symlink the input data as was done for other platforms,

.. code-block:: shell

    mv vn11.5 vn11.6; ln -s vn11.6 vn11.5

Now run the central install group,

.. code-block:: shell

    rose stem --group=ex1a_install -S CENTRAL_INSTALL=true -S PREBUILDS=false
    cylc play <name-of-suite>

Install prebuilds on Monsoon. Note the ``--no-run-name`` is required to force
the install location to be consistent with other platforms.

.. code-block:: shell

    rose stem --group=ex1a_fcm_make,ex1a_fcm_make_portio2b \
        -S MAKE_PREBUILDS=true -n vnX.Y_prebuilds --no-run-name
    cylc play <name-of-suite>

Finally we need to install the kgo for the release. Do this by running the
``ex1a`` group. Once that is finished, run the kgo install script(sourced from
the SimSys_Scripts repo).

.. code-block:: shell

    rose stem --group=ex1a
    cylc play <name-of-suite>
    # Wait for tests to complete
    python3 SimSys_Scripts/kgo_updates/kgo_update/kgo_update.py -N vnX.Y \
        -P ex1a --new-release --non-interactive

Check that the kgo has been installed in place correctly at
``$UMDIR/standard_jobs/kgo``.

