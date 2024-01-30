.. _howtocommit:

How To Commit
=============

The process for committing a ticket follows this sequence with details for each of these steps outlined below.

.. image:: images/commit_process.png

.. important::
    Before You Start:
      * Is anyone else committing?

        * `Trunk Status`_ is used to coordinate trunk commits for UM, JULES and UKCA.
        * LFRic Trunk commits are coordinated through the dashboard in the Model Systems Teams Chat.
        * Simple, not conflicting commits can be done in parallel if reviewers all agree.
        * Changes with KGO or Macros usually require sole access to the trunk.
      * Check how many commits have happened today. Suggested limit per day, per repository is 4.

        * More than 4 can be committed if `all` groups have been run by a team member.


.. important::
    **Linked Tickets?**

    If this is a set of linked tickets then the commit process will need to be
    followed for each repository in parallel. See :ref:`committinglinkedtickets`
    for more details of how this works.

    .. toctree::
        :hidden:

        committinglinkedtickets

1. Merge
--------

Check out the trunk, merge the changes from the branch into that trunk copy and
resolve any conflicts.

.. tab-set::

    .. tab-item:: UM

        .. code-block:: RST

            fcm co fcm:um.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:um.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: JULES

        .. code-block:: RST

            fcm co fcm:jules.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:jules.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: UKCA

        .. code-block:: RST

            fcm co fcm:ukca.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:ukca.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: LFRic

        .. code-block:: RST

            fcm co fcm:lfric.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:lfric.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: UM docs

        .. code-block:: RST

            fcm co fcm:um_doc.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:um_doc.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: JULES docs

        See :doc:`JULES documentation changes </WorkingPractices/jules_docs>`

Always merge in the developers **dev** branch, not the **test** branch.

Only resolve `conflicts <http://metomi.github.io/fcm/doc/user_guide/code_management.html#svn_basic_conflicts>`_
that appear simple and you are comfortable with. If there are more complicated
conflicts ask the developer to create a head of trunk branch to resolve the
conflicts themselves and retest the changes.

If there are conflicts in versions.py then see the details in the macro section below.

2. Macros (if required)
-----------------------
**If** the ticket includes meta-data changes, upgrade macro changes or a new rose-stem app
then you will need to upgrade the test-suite.

.. dropdown:: versions.py

    versions.py contains a sequence of upgrade macros. Each macro contains a
    `BEFORE_TAG` and an `AFTER_TAG` which should create a single chain, starting
    at the last release and finishing with the ticket you are committing. The
    tags have the format version_ticket, i.e. `vnXX.Y_tZZZZ`.

    When resolving conflicts in this file make sure that the new macro being added
    by your ticket is added to the end of the file. Modify the `BEFORE_TAG` to
    match the `AFTER_TAG` of the previous macro in the chain.

    If this is the first macro since the release then the `BEFORE_TAG` will be
    the version number with no added ticket number.

    Remove the template macro if it is still present.

.. dropdown:: Applying Macros

    To update the test suite for an upgrade macro, please run:

    .. tab-set::

        .. tab-item:: UM

            .. code-block:: RST

                ~frum/bin/update_all.py --path=/path/to/working/copy/of/trunk --um=vnXX.Y_tZZZZ

            where `--um=vnXX.Y_tZZZZ` is the `AFTER_TAG` of the latest upgrade macro.

            If there is a macro for fcm_make or createbc then check that the makes `version*_*.py` has the
            correct BEFORE and AFTER tags and append `--makeum=vnXX.Y_tZZZZ` and/or `--createbc=vnXX.Y_tZZZZ`
            to the above command.

        .. tab-item:: JULES

            .. code-block:: RST

                ./bin/upgrade_jules_test_apps vnX.Y_tZZZZ

            where `vnX.Y_tZZZZ` is the `AFTER_TAG` of the latest upgrade macro.
            The upgrade is expected to fail for the `fab_jules`, `metadata_checker` and `umdp3_checker` apps.

.. dropdown:: New rose-stem app?

    If the ticket introduces a new rose-stem app, but doesn't otherwise have a macro
    then that app will need to be updated to match the metadata at the Head Of Trunk.

    1. In the new app directory get a list of all available upgrade points by running

        .. code-block:: RST

            rose app-upgrade -a -y -M path/to/working_copy/rose-meta

    2. Select the latest upgrade point from the list provided and then run the command again, adding this to the end

        .. code-block:: RST

            rose app-upgrade -a -y -M path/to/working_copy/rose-meta vnX.Y_tZZZZ

    The app should now be updated to the same metadata version as the rest of the apps on the Trunk.
    This can be checked with:

        .. code-block:: RST

            rose macro --validate -M path/to/working_copy/rose-meta

.. dropdown:: Temporary Logical?

    If a new temporary logical has been added, or an old one retired, then
    update the `table that lists them <https://code.metoffice.gov.uk/trac/um/wiki/TempUMlogicals>`_.

3. Test (if no KGO)
--------------------

The amount of testing to be done at this stage depends on the complexity
of the ticket, and what has already been done. A minimum level is required for
even trivial tickets to check that the merge has not caused issues, or that there
are no clashes with what else has gone on trunk.

.. note::
    Linked tickets will need to be tested together as discussed :ref:`here <tesinglinked>`.

.. tab-set::

    .. tab-item:: UM

        Run any necessary testing; at the very least run a compile group,
        generally run developer, and more complex tickets warrant running everything:

        .. code-block:: RST

            rose stem --group=debug_compile
            rose stem --group=developer,ex1a_developer
            rose stem --group=all,ex1a

        If there is a change to the build configs then you may need to turn off
        prebuilds. To do so update `rose-stem/site/meto/variables.rc` such that

        .. code-block:: RST

            {% do SITE_VARS.update({"PREBUILDS" : false}) %}

    .. tab-item:: JULES

        The JULES test suite is quick to run, so it's usual to test `all` for any ticket.
        If you have the appropriate environment setup then include the `fab` group too.

        .. code-block:: RST

            rose stem --group=all,fab


    .. tab-item:: UKCA

        The UKCA rose-stem contains minimal tests at the moment, but should be run to
        confirm the style checker passes.

        .. code-block:: RST

            rose stem --group=all

        UKCA testing should also be carried out using the UM rose stem. Check
        out the UM trunk, and then run

        .. code-block:: RST

            rose stem --group=developer,ukca --source=. --source=/path/to/UKCA/working/copy


    .. tab-item:: LFRic

        LFRic has many rose-stem suites for its different applications. Run the
        test suite command from the top level of the repository to run a complete
        set of the rose-stem suites.

        .. code-block::

            make test-suite
                and
            make test-suite SUITE_GROUP=nightly

    .. tab-item:: UM docs

        Check the documentation builds correctly:

        .. code-block:: RST

            ./build_umdoc.py [XXX YYY etc]

        where XXX YYY are the details of which docs require building.

    .. tab-item:: JULES docs

        Check the documentation builds correctly:

        .. code-block:: RST

            cd docs/user_guide
            module load scitools
            make clean html
            firefox build/html/index.html

            make clean latexpdf
            evince build/latex/JULES_User_Guide.pdf &



4. KGO (if required)
--------------------

**If** your change is known to alter answers, you need to update rose-stem KGO
for all affected tests before you commit to the trunk.

*NB: These instructions are Met Office specific, other sites may manage their KGO differently*

.. dropdown:: Setup for first KGO install.

    Before you start the process below there is a one-time setup step required to
    allow you to generate KGO using the update script.

    Edit `~/.metomi/rose.conf` on *all platforms* - Desktop, XCE/F, XCS and EXZ
    to contain the following:

    .. code-block::

        [rose-ana]
        kgo-database=.true.

.. tab-set::

    .. tab-item:: UM + LFRic Inputs

        KGO files are stored in `$UMDIR/standard_jobs/kgo` or `$UMDIR/standard_jobs/lfricinputs/kgo` and are installed there
        using a script.

        1. Run the rose stem tasks that require a KGO update, plus any other testing required (see above) - if unsure run the `all,ex1a`.

            .. code-block::

                rose stem --group=all,ex1a --new

        2. You will need access to both your merged working copy and a clone of the `SimSys_Scripts github repo <https://github.com/MetOffice/SimSys_Scripts>`_ (one is available in $UMDIR). Run the script ``kgo_updates/meto_update_kgo.sh`` which is located in SimSys_Scripts.

        3. The script will ask you to enter some details regarding the ticket.

          * Platforms: enter each platform which has a kgo change, lower case and space seperated, e.g. `spice xc40 ex1a`
          * Path to your merged working copy - the script will check this exists and will fail if it can't be found.
          * The file extension of the variables file. Currently this should be ``.rc`` for the UM and ``.cylc`` for lfricinputs.
          * KGO directory: this will default to vnXX.X_tYYYY where XX.X is the version number and YYYY is the ticket number.
          * There are further prompts to the user through the script - in particular to check the shell script produced.

        4. If running on xc40s the script will ask whether to rsync UM files or lfricinputs files to the XCS. Select the appropriate option.

        5. Check that the new KGO has been installed correctly by restarting your suite, retriggering the failed rose-ana tasks and checking they now pass.

          * e.g. add `--reload` or `--restart` to the rose-stem command ran previously.

        6. Once committed, update the `bit comparison table <https://code.metoffice.gov.uk/trac/um/wiki/LoseBitComparison>`_.

        .. dropdown:: More details on KGO update script

            * This script will login as `frum` and `umadmin` as needed
            * After running for a platform, the newly created variables.rc and
              shell script will be moved to SPICE ~frum/kgo_update_files/<new_kgo_directory>.
            * The script is hard coded to always go to the xce (only 1 is
              required of xce and xcf). After running here it will rsync the kgo
              directory to xcs automatically.
            * Having run on each requested platform the new variables.rc files
              will be copied into your working copy
              rose-stem/site/meto/variables_<PLATFORM>.rc. There is no longer
              any need to merge the generated variables files. It is probably
              worth checking that the changes in these files are as expected.

        .. dropdown:: Updating KGO manually (rarely needed!)

            * Create a new directory for the new KGO. The naming convention is
              vnXX.X_tNNNN, where NNNN is the ticket number. The location of the
              KGO for the nightly is $UMDIR/standard_jobs.
            * Copy the new KGO from your rose-stem run into the directory
              vnXX.X_tNNNN created above. Note that you need to provide a
              complete set of files, not just ones which have changed answers.
              This includes the reconfiguration .astart file!
            * If a file hasn't changed you can optionally symlink forwards from
              the previous version (i.e. move the old file to the new KGO
              directory and replace it with a sym-link to the updated version)
              But do not do this if the old version was a major release revision
              (vnX.X), this is to allow intermediate revisions to be deleted later.
            * Remember to RSync and update the bitcomparison table (see above).

    .. tab-item:: JULES

        1. Run the standalone rose-stem with housekeeping switched off to generate new KGO.

            .. code-block::

                rose stem --group=all,ex1a --source=. -S HOUSEKEEPING=false --new

        2. Update KGO_VERSION in `rose-stem/include/variables.rc`.
        3. Copy the new KGO to the correct locations:

            .. code-block:: RST

                ssh -Y frum@localhost
                KGO_VERSION=vnX.X_txxxx
                USER_NAME=<user>
                SUITE=<suite>

                # Copy Linux output to the KGO location for Linux
                KGO_DIR=/project/jules/rose-stem/jules-kgo/$KGO_VERSION; mkdir -p $KGO_DIR && cp ~$USER_NAME/cylc-run/$SUITE/work/1/meto_linux_*/output/* $KGO_DIR

                # Copy Cray output to the KGO location for the Cray
                ssh -Y xcel00
                KGO_VERSION=vnX.X_txxxx
                USER_NAME=<user>
                SUITE=<suite>
                KGO_DIR=/projects/jules/rose-stem-kgo/$KGO_VERSION; mkdir -p $KGO_DIR && cp ~$USER_NAME/cylc-run/$SUITE/work/1/meto_xc40_*/output/* $KGO_DIR

                # DON'T forget the xcs!!!
                rsync -avz $KGO_DIR xcslr0:/projects/jules/rose-stem-kgo/

                exit
                # check the xcslr0
                ssh -Y xcslr0
                KGO_VERSION=vnX.X_txxxx
                KGO_DIR=/projects/jules/rose-stem-kgo/$KGO_VERSION
                ls $KGO_DIR
                exit

                # Copy EXZ output to the KGO location for EXZ (note <USERNAME> format is firstname.surname!)
                ssh -Y login.exz
                KGO_VERSION=vnX.X_txxxx
                USER_NAME=<user>
                SUITE=<suite>
                KGO_DIR=/common/jules/rose-stem-kgo/$KGO_VERSION; mkdir -p $KGO_DIR && cp ~$USER_NAME/cylc-run/$SUITE/work/1/meto_ex1a_*/output/* $KGO_DIR

        4. Rerun the rose-stem tests to make sure nothing is broken.

    .. tab-item:: LFRic

        KGO Checksums are stored in the repository alongside the code. If there
        is a merge conflict within these files it is the developers responsibility
        to update them.

        1. Organise a trunk freeze for LFRic at a time when the developer is available
        2. Developer updates their branch to the head of trunk and regenerates
           the KGO checksums.
        3. If there were also code conflicts in the science code then the new KGO
           checksums will need to be signed off by the science reviewer.
        4. Once the ticket is back with you, you can merge the branch to the
           trunk and run the test-suite as described above to confirm that all
           is working.

.. tip::
    Between running any required testing and installing the KGO check that the
    failing rose-ana tasks match those in the developers trac.log. If any have
    failed for other reasons (e.g. timeout) then these should be re-triggered
    before attempting to install the KGO files.

5. Commit
---------

Take a final review of the changes about to be applied looking for any obvious
merge errors

.. code-block:: RST

    fcm diff -g

.. note::
    Linked tickets will need to follow the sequence described :ref:`here <committinglinked>`.

Commit the change to the trunk

.. code-block:: RST

    fcm commit

An editor will open requesting a log message which should be in this format:

.. tab-set::

    .. tab-item:: UM

        .. code-block::

            #ticket_number : Author : Reason for the change : ticket_type : code_area : regression : severity

        This layout enables a script to parse the commits that make up each release.

        1. Ticket number
        2. Author : SRS username
        3. Reason for the change : Title of the ticket
        4. Ticket Type

          * enhancement, defect, task, optimisation

        5. Code Area -  Select the most appropriate from:

          * technical, dynamics, ukca, bl_jules, convection, radiation, gwd, lsp_cloud, stochastic_physics, coupling, idealised, rose_stem, fcm_make, meta_data, utils, fieldcalc, other

        6. Regression:

          * kgo_and_macro, update_kgo, upgrade_macro, regression

        7. Severity

          * wholesale, significant, minor, trivial


    .. tab-item:: JULES & JULES docs

        .. code-block::

            #<ticket number> for <original author> - <ticket title>

        where original author is the srs username.

    .. tab-item:: UKCA

        .. code-block::

            #ticket_number : Author : Ticket title

        where author is the srs username.

    .. tab-item:: LFRic

        .. code-block::

            #<ticket number> for <original author>: <ticket title>

        where original author is the authors proper name.

    .. tab-item:: UM docs

        .. code-block::

            #ticket_number : Author : Description : XXX (YYY ZZZ etc)

        where XXX, YYY etc are the three letter codes for any UMDPs modified.

.. note::
     New!! Remove any **blocks:** and **blockedby:** keywords from this ticket and any referenced. Comment on any unblocked tickets to alert the developers.

Update the ticket with the revision number of the commit, e.g. [100000] for revision 100000, comment whether the change is expected to alter results or not and update the ticket status to committed.

.. tip::
    Don't forget to let the team know you've finished with the trunks.

.. dropdown:: Modifying log messages

    If you need to modify the commit log message after commit, run this command and save to update the message:

    .. code-block:: RST

        fcm propedit --revprop svn:log -r xxxxxx fcm:um.x_tr

6. Close
--------

The following day review the nightly test harness results (details on `Trunk Status`_).

If nothing is broken then close the ticket, returning it to the original author.

If something is broken:

    * Announce to the team and on `Trunk Status`_.
    * If there is an obvious bug, or a simple fix then update the original branch and re-merge into the trunk.
    * If there isn't an easy fix then reverse the change to allow time for investigation.

.. dropdown:: Reversing Trunk Commits

    1. Check out the trunk
    2. Use the merge command to reverse the problematic change
        .. code-block::

            fcm merge --reverse -r <revision>

    3. Check the reverse merge has worked and commit it to the trunk
        * Use the same commit message format as usual.
    4. Update the ticket with details of the problem and assign it back to the author to fix

    .. note::
        If and when the author provides a fixed version of the branch a custom
        merge will be required (otherwise only the most recent commits will be merged).

        .. code-block::

            fcm merge --custom --revision <revision1>:<revision2> fcm:um.x_br/dev/etc...

        where revision 1 and 2 are the initial copy and the last change to the branch to be committed.


.. tip:: **Logging in as frum**

    * To access the frum account your ssh key will need to be added to frum authorised keys (contact Rich Gilham).
    * When logged in to your linux desktop run ``ssh -Y frum@localhost`` and this will log you in as frum.
      At this point you will be in UMDIR on the platform SPICE. You can then access frum on other machines via ssh -Y <HOSTNAME>.
    * Apart from on SPICE the frum home directories and UMDIR are separate. XCE/F share the same UMDIR and the UMDIR on XCS is kept in sync with this one.

.. _Trunk Status: https://code.metoffice.gov.uk/trac/um/wiki/TrunkStatus
