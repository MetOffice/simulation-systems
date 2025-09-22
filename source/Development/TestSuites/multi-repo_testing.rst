.. _multi-repo_testing:

Multi-Repository Testing
========================

Multi-repository changes are expected to pass the regression tests for all the
repositories involved. To carry out the tests involved in a linked ticket it
can be helpful to refer to the :ref:`repository figure <multirepo>`; testing
both child and parent repositories as needed. Further details of how testing
in each repository is handled can be found on the :ref:`Testing
page<testing>`. Compatible code revisions are needed for testing across
repositories as described above.

Testing changes in JULES, LFRic Core, UKCA, or any other child repositories is
as simple as running the standalone test procedures for these codebases.

.. important::

    When specifying an alternative source in the ``dependencies.sh`` file the
    revision for the source **must** be updated.

    * If setting the source as an fcm URL, the mirror (``.xm_``) needs to be
      used and the revision can either be blank (for latest commit) or any
      valid revision for that branch.
    * If setting the source as a Working Copy, the hostname needs to be
      provided (as Hostname:Path) and the revision must be blank.

Testing the UM with other repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To test the UM, any changes to JULES, UKCA, Socrates, CASIM etc will also need
to be included. This is done by adding another source to the rose stem command
line.

1. Checkout a UM working copy
    - this may be your branch from a linked ticket, or a clean trunk copy at
      either the last release or a suitable head of trunk revision.

2. Run rose stem, including a source code path to every branch involved. As a
   minimum run ``developer`` group and all groups that cover the repositories
   being tested.

.. code-block:: shell

    rose stem --group=developer,jules,ukca --source=. \
        --source=/path/to/jules/changes --source=/path/to/ukca/changes

The source paths involved can either be to local working copies or links to the
fcm source control e.g. ``fcm:jules.xm_br/dev/user/branch_name``. As many
source paths as needed can be added to the list.

Testing LFRic Apps with other repositories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

LFRic Apps testing needs to encompass all of the other repositories affected.
Paths to the other codebases involved should be added to ``dependencies.sh``
under each of the ``*_sources`` variables. Again these paths can either be to
local changes or those in the repository.

1. Checkout an LFRic Apps working copy

- this may be your branch from a linked ticket, or a clean trunk copy at either
  the last release or a suitable head of trunk revision.

2. Update dependencies.sh to point to all other code changes, e.g.

.. code-block::

    lfric_core_rev=
    lfric_core_sources=fcm:lfric.xm_br/path/to/branch

    casim_rev=
    casim_sources=vldXXX:/path/to/casim/working/copy

3a. Run the lfric_atm developer test-suite

- suitable for testing changes in other repositories that do not include any
  LFRic Apps changes

.. code-block:: shell

    export CYLC_VERSION=8
    rose stem --group=lfric_atm_developer
    cylc play <working copy name>
    cylc gui

3b. Run the full developer test-suite

- suitable for testing LFRic Apps changes with other repositories, or expanding
  testing if lfric_atm tests have shown errors.

.. code-block:: shell

    export CYLC_VERSION=8
    rose stem --group=developer
    cylc play <working copy name>
    cylc gui

More details on LFRic Apps testing are found on the
:ref:`Testing LFRic Apps page<lfric_apps_test>`.

.. note::

    If any of the testing shows up failures then there are two possible ways to
    proceed:

    1. The changes made should be re-written to avoid breaking the dependant
       repositories

    2. The changes made directly affect the interface between repositories and
       therefore a change is also needed to the parent repository to adapt to that change.

    If you're uncertain which route to take then the Code Owners involved will
    hopefully be able to advise.
