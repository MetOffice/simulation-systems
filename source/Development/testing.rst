.. _testing:

Testing Your Change
===================

Change to the Rose Stem Suite in Git
------------------------------------

.. _github_testing:

With the move to git and GitHub, the test suites of the Simulation Systems
repositories will no longer use the rose-stem infrastructure, instead becoming
purely Cylc workflows. The only impact on the end user will be a change to the
commands required to launch the test suite. The contents of the test suite and
the process to add new tests will remain unchanged. The test suite
infrastructure will continue to live in a ``rose-stem`` directory, and we will
continue referring to the test suite as the ``rose-stem`` suite in these working
practices.

Running the rose-stem suite will now directly call cylc commands with the
following syntax,

* ``cylc vip`` - This will install and launch the test suite. If desired, it
  can be replaced with separate ``install`` and ``play`` commands which would
  need to be run separately.
* ``-z g=`` or ``-z group=`` - This sets the test suite groups to run, and
  takes a comma separated list of groups. For example, ``-z g=developer,
  lfric_atm`` will run the ``developer`` and ``lfric_atm`` groups.
* ``-S VALUE=SETTING`` - these options behave as they did before, and can be
  added to the ``cylc vip`` command. See the table below for some suggestions.
* ``-S USE_MIRRORS=`` - An example of the above settings, this is newly added
  with the git migration. By default this is ``false`` and remote GitHub
  repositories will be accessed via ssh. If set to ``true``, local GitHub
  mirrors will be used instead. This is recommended particularly for shared
  accounts.
* ``-n name_of_suite`` - The new test suites will name themselves after the
  directory containing the test suite. Unfortunately this is always
  ``rose-stem`` so it is recommended to give the suite a name using this option.
* ``/path/to/rose-stem`` - The path to the rose-stem directory must be specified
  if not launching from in that directory.

For example,

.. code-block::

    cylc vip -z group=developer -S USE_MIRRORS=true -n my_rose_stem_suite ./rose-stem

will launch the test suite with the ``developer`` group, using the GitHub
mirrors and naming it ``my_rose_stem_suite``.

``-S`` Options (non-exhaustive):

* ``-S USE_MIRRORS=true`` - Use local GitHub mirrors instead of ssh.
* ``-S USE_TOKENS=true`` - Authenticate with GitHub using a :ref:`personal
  access token <GitHub_pat>` instead of ssh. If both this and ``USE_MIRRORS``
  are true, then the mirrors will be used instead. On Monsoon, this is
  automatically set.
* ``-S USE_HEADS=true`` - Use the head of the default branch for the GitHub
  source, only intended for usage in nightly testing.
* ``-S USE_EX[AB/CD/Z]=true`` - MetOffice only, specify the host machine for
  EX1A jobs.
* ``-S HOUSEKEEPING=false`` - Stop housekeeping tasks from running.

What Testing to Run
-------------------

Every change should be thoroughly tested, using your judgement as to what this
involves based on the complexity of your change. There are three main methods
for you to choose from:

Rose-stem:
    Every repository has a rose-stem test suite that provides integration and
    regression testing - and in some cases unit tests as well. Committing
    changes to the ``main`` of each repository is dependant on these tests
    passing; they are there to ensure the integrity of the codebase.

Standard suites:
    As well as the rose-stem tests you should also consider how best to prove
    that your change does what it says it does, and not what it doesn't. There
    may be other standard suites that will exercise your change in a
    scientific or technical way. If you're unsure on what that is then talk to
    the code owners involved for advice.

Bespoke:
    If the above hasn't satisfied you (or your SciTech reviewer) then you may
    wish to consider further evaluation by creating your own tests.


.. toctree::
   :maxdepth: 1
   :caption: Test Suites

   TestSuites/um
   TestSuites/lfric_apps
   TestSuites/lfric_core
   TestSuites/jules
   TestSuites/ukca
   TestSuites/multi-repo_testing

Test branches & Upgrade Macros
------------------------------

.. tip::

    While we continue to use ``dev`` and ``test`` branch nomenclature from fcm,
    in GitHub these terms have no technical meaning and are simply a way to
    distinguish between 2 branches.

There are a few cases where testing your change will require you to make changes
to your branch that don't want committing to ``main``. To do this you can create
a test branch. This is a branch-of-branch from your development branch and
allows you to make those changes in an isolated environment while leaving your
original development clean.

To create a test branch:

.. code-block:: shell

    git switch -c test_branch_name [<start_point>]

If not provided ``start_point`` will default to your
current branch.

If using a test branch then do link to this on your pull request and include the
results of this testing alongside those from your dev branch.

.. Note::

    If you need further updates to the dev branch which require retesting on the
    test branch, you can update the test branch by merging in the dev branch.

    .. code-block::

        git switch test_branch_name
        git merge dev_branch_name

    If testing upgrade macros however, you will likely need a new test branch,
    as the macros can only be applied once.

Macros
^^^^^^

If you have updated the model inputs and included an upgrade macro with your
change then this macro will be run by your code reviewer as part of the commit
process. In order to prove that the upgrade macro will be successful, and to
make those new model inputs available to your tests, you should create a test
branch as described above and run the upgrade macro with one of the following
commands, noting that ``--jules-path`` is only required if you have
**jules-shared** metadata changes. Please see the shared metadata
:ref:`guidance<shared-namelists>`.

+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UM    | ``./admin/rose-stem/update_all.py --path=/path/to/working/copy/of/test/branch --um=vnX.X_tXXXX [--jules-path=/path/to/jules/working/copy/of/branch]``                        |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| JULES | ``./bin/upgrade_jules_test_apps vnX.X_tXXXX``                                                                                                                                |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LFRic | ``apply_macros.py vnX.Y_tZZZZ [--apps=/path/to/apps] [--core=/path/to/core] [--jules=/path/to/jules]``                                                                       |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. tip::

    The ``apply_macros.py`` script is located in the `SimSys_Scripts GitHub
    repo <https://github.com/MetOffice/SimSys_Scripts>`__ (at meto an up to
    date clone is available in $UMDIR/SimSys_Scripts).

.. warning::

    Please ensure that Cylc7 is used with ``update_all.py`` @vn13.5. This is
    fixed at HoT and either Cylc7 or Cylc8 can be used.

.. Note::

  The update_all.py script suppresses warnings produced by upgrade macros.
  You can test these separately by upgrading a single app. A single app can
  be upgraded for testing using:

  .. code-block:: shell

      rose app-upgrade -M /path/to/rose-meta \
      -C /path/to/rose-stem/app/<app_name> -a <trunk_metadata_version>

  where the ``-C`` option can be omitted if inside the app's directory.

  .. Important::

      If there are **jules-shared** metadata changes these will need to be
      added to the metadata path. Please see the :ref:`rose config-edit
      example<metadata_changes>`.

      Please refer to `rose app-upgrade
      <https://metomi.github.io/rose/doc/html/api/command-reference.html#rose-app-upgrade>`__
      command reference for more details.

.. _traclog:

trac.log
--------

The output of rose-stem from each repository includes a trac.log. This is a
wiki formatted file that can be copied into the pull request description as a record of
testing run. Please make sure that the results of your latest testing are
included when passing a pull request for review.

.. code-block:: shell

    ~/cylc-run/<suite_name>/runN/trac.log


.. tip::

    If your suite has finished and no trac.log has been generated then it is
    possible to do so manually using `suite_report.py
    <https://github.com/MetOffice/SimSys_Scripts/blob/main/suite_report.py>`__

    On Met Office desktops a copy is stored locally allowing this to be done
    with:

    .. code-block:: shell

        python3 $UMDIR/SimSys_Scripts/suite_report_git/suite_report_git.py -S <workflow path>

    If this is a regular problem then get in touch with the :ref:`SSD team
    <simIT>` so we can investigate. Thanks.
