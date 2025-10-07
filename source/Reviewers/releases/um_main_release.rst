.. _um_main_release:

UM Main Release
===============

Create Branches
---------------

Ensure you have a :ref:`fork <forking>` of both the ``um`` and ``um_meta``
repositories, and that the ``main`` branches in each are up to date with the
upstream repository.

In a clone of these forks, :ref:`create a branch <create_branch>` using the
``main`` branch as the parent. In the UM branch, update the ``um_meta`` entry in
the ``dependencies.yaml`` file to point at your metadata branch.

.. important::

    Ensure you create branches from main, otherwise you will not include the
    changes from the past release.


Tagging Feeder Trunks
---------------------

* Add a ``umX.Y`` tag to each of the feeder repositories

  * Casim
  * Jules
  * Shumlib
  * Socrates
  * UKCA

Send an email to all repository owners to let them know that the the head of
the trunk has been tagged.

.. note::

    Jules should already have been done by the Jules release, but this is worth
    checking.

For each of these repositories, modify the ``ref`` in the UM
``dependencies.yaml`` file, to point at the new ``umX.Y`` tag. Commit this
change to the branch.


Apply Code Styling
------------------

* Switch to the UM branch
* Set ``export RUNFULL=1`` then run ./admin/code_styling/apply_styling
* If any files have changed, check nothing has gone wrong with a quick compile
  ``cylc vip -z g=fcm_make_ex1a_gnu_um_rigorous_omp -n um_release_style_check
  ./rose-stem``
* Commit any changes


Checking Metadata and Rose Apps
-------------------------------

.. important::

    The JULES release must be completed first and all jules-shared metadata
    changes from the JULES repository must be centrally installed before
    progressing.

* First switch to the UM branch.
* Check that the metadata meets the Rose standards: run ``rose config-dump -C
  rose-meta``. Do this before running ``release_new_version``, so that any
  metadata errors are fixed before the new vnX.Y metadata directories are
  created, otherwise you'll have to check both vnX.Y and HEAD.

  * Run ``git difftool origin/main``. Are the changes sensible? They often
    just involve moving sections of meta-data to be in the correct
    alphabetical order.

    .. important::

      `UM:#1824
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
* Commit all changes before moving onto the next section.


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


Final Checks
------------

**UM AUX Changes**

If there are changes to the AUX trunk in this release, then add a new tag to the
``um_aux`` repository and then update the ``ref`` in the UM
``dependencies.yaml`` file - commit this to the branch.

**Other Points**

* Check rose-stem/rose-suite.conf?

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

* For the rose_ana tasks to pass new KGO also needs to be generated for the new
  version, since you are about to run the ``all`` group test anyway you should
  use this opportunity to produce a new set of KGO.

  * KGO is installed using the scripts in SimSys_Scripts. In order for the
    script to work you must first change the KGO directories in the
    ``variables.cylc`` and platform-specific ``variables_PLATFORM.cylc``
    files back to whichever versions were present before the
    ``release_new_version.py`` script was run - you can do this with a
    simple copy from the head of main. Be careful to ensure this is
    only changing the KGO versions for each variable as expected. **DO NOT
    COMMIT this change - you will be reverting it later**.

  .. code-block:: shell

    git clone git@github.com:MetOffice/um.git um_main

    cp um_main/rose-stem/site/meto/variables* /path/to/um/branch/rose-stem/site/meto/

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

  cylc vip -z g=all -S HOUSEKEEPING=false -S USE_EXAB=true -n um_release_vnx.y ./rose-stem

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

.. important::

    The authentication for running as the shared user via ``sudo`` will likely
    have expired before each of the 2 rsync commands, so pay attention as the
    script nears these points. If you forget and the command times out, the
    command can be launched manually from the command line. Ask the team if
    for help if required.

Once you believe you have installed the KGO you should fcm revert the changes
you made to the variables*.cylc files to reset the KGO variables, ``git restore
rose-stem/site/meto/variables*``

.. tip::

    Has the ability to reload the test suite been enabled yet? If so ``cylc
    vr`` can likely be used to restart the original suite.

    This is likely the case after moving to github - try and update these WPs if
    so.

The test suite should now be rerun to confirm the kgo has been installed
properly. As we can't restart Cylc8 rose-stem suites, the entire thing needs
to be rerun. We're just checking that the kgo has been installed, so it's
probably unnecessary to wait for the entire thing - instead just ensure a
reasonable range of rose-ana tasks have passed.


Review and Commit
-----------------

Ensure all changes are committed to both branches and then create a PR for each
of the ``um`` and ``um_meta`` branches and pass along for a review and commit.

You and the reviewer should work through the process of committing the branches
together - :ref:`see here for details page<github-releases>`.


Install the Release
-------------------

First get a local clone of the head of the ``um`` repository, now that the
release has been committed. This makes it available to the shared account
without having to rely on the mirrors.

The main installation of ctldata, utilities and prebuilds can now take place.
This all takes place as the ``umadmin`` account so log in to that now.

Copy the ``um`` clone you created just now.

First check that the upgrade has gone successfully and the new install will
appear in the correct place. Do this by running,

.. code-block:: shell

    cylc vip -z g=install -S CENTRAL_INSTALL=false -S USE_EXAB=true -z umx.y_install ./rose-stem

and check that ``~umadmin/cylc_run/<working_copy_name>/runN/share/vnX.Y``
exists and is the new version number. If that has worked, change the
CENTRALL_INSTALL flag to true and rerun,

.. code-block:: shell

    cylc vip -z g=install -S CENTRAL_INSTALL=true -S USE_EXAB=true -z umx.y_install ./rose-stem


Next, rerun the install for the 2nd host zone,

.. code-block:: shell

    cylc vip -z g=ex1a_install -S CENTRAL_INSTALL=true -S USE_EXCD=true -z umx.y_install ./rose-stem

Finally, rerun the install for the EXZ,

.. code-block:: shell

    cylc vip -z g=ex1a_install -S CENTRAL_INSTALL=true -S USE_EXZ=true -z umx.y_install ./rose-stem

The release is now installed and can be announced.

.. tip::

    This is the point at which prebuilds used to be created. If prebuilds become
    possible again, update the working practices here.


Monsoon Installation
--------------------

.. tip::

    This section can be done in parallel with the previous one

We also install the UM onto Monsoon - to do this you will need a Monsoon
account with access to the ``umadmin.mon`` shared account.

First, log into Monsoon as ``umadmin.mon`` and then clone the ``um`` repo.

.. note::

    At time of writing, the solution for extracting from github on Monsoon has
    not been announced.

Next, symlink the input data as was done for other platforms,

.. code-block:: shell

    mv vn11.5 vn11.6; ln -s vn11.6 vn11.5

Now run the central install group,

.. code-block:: shell

    cylc vip -z g=ex1a_install -S CENTRAL_INSTALL=true -z umx.y_install ./rose-stem

Install prebuilds on Monsoon. Note the ``--no-run-name`` is required to force
the install location to be consistent with other platforms.

Finally we need to install the kgo for the release. Do this by running the
``ex1a`` group. Once that is finished, run the kgo install script(sourced from
the SimSys_Scripts repo).

.. code-block:: shell

    cylc vip -z g=ex1a -n umx.y_kgo ./rose-stem

    # Wait for tests to complete
    python3 SimSys_Scripts/kgo_updates/kgo_update/kgo_update.py -N vnX.Y \
        -P ex1a --new-release --non-interactive

Check that the kgo has been installed in place correctly at
``$UMDIR/standard_jobs/kgo``.
