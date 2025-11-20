.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _multi-repo_testing:

Multi-Repository Testing
========================

Multi-repository changes are expected to pass the regression tests for all the
repositories involved. To carry out the tests involved in a linked pull request
it can be helpful to refer to the :ref:`repository figure <multirepo>`; testing
both child and parent repositories as needed. Further details of how testing in
each repository is handled can be found on the :ref:`Testing page<testing>`.

All Simulation Systems repositories containing a test suite will also contain a
``dependencies.yaml`` file in the top directory of the repository. This file
contains the details of all sources used by the test suite in the format (using
lfric_core as an example):

.. code-block:: yaml

    lfric_core:
        source: git@github.com:MetOffice/lfric_core.git
        ref: <Long Hash / Tag>

The ``source`` setting sets the location of the repository on GitHub. By
default, the test suite will access GitHub repositories by using ssh, as shown
by the ``git@github.com`` part of the source. This line can be modified to point
at users fork of the repository instead, eg.
``source: git@github.com:UserName/lfric_core.git``. The ``source`` can also be a
local git clone, in which case it should take the form,
``source: <HOSTNAME>:/path/to/clone``.

The ``ref`` setting takes a git tree-ish value. Common settings will be a commit
hash, a tag or a branch name as demostrated by the examples below. At
release, the refs will be tags and will be changed to the long form of the relevant
commit hash as part of linked pull requests.

If left blank the behaviour depends on the source:

* **a GitHub source:** the Head of the repositories default branch will be used.
* **a local clone:** the state of the repository at source extraction time will be used.
  It is recommened to set a ref when setting the source to a local clone.  That way
  if you switch branches in the clone, the correct branch for testing will be used.

Various different configurations of an lfric_core source are shown below with an
explanation of each,

.. code-block:: yaml

    # The upstream lfric_core repository at tag 3.0
    lfric_core:
        source: git@github.com:MetOffice/lfric_core.git
        ref: core3.0

    # The upstream lfric_core repository at a specific commit hash
    lfric_core:
        source: git@github.com:MetOffice/lfric_core.git
        ref: a1b2c3d4e5f67890abcdef1234567890abcdef12

    # As above, but with a shortened form of the hash (7 characters in this case)
    lfric_core:
        source: git@github.com:MetOffice/lfric_core.git
        ref: a1b2c3d

    # The upstream lfric_core repository, with the default branch (main) at Head
    lfric_core:
        source: git@github.com:MetOffice/lfric_core.git
        ref:

    # A Users fork of the lfric_core repoistory, on branch my_branch
    lfric_core:
        source: git@github.com:UserName/lfric_core.git
        ref: my_branch

    # A Users fork of the lfric_core repository at a specific hash
    lfric_core:
        source: git@github.com:UserName/lfric_core.git
        ref: f9e8d7c

    # A local clone of the lfric_core repository, pointing at my_branch
    lfric_core:
        source: hostname:/path/to/lfric_core
        ref: my_branch

    # A local clone of the lfric_core repository, pointing at a specific hash
    lfric_core:
        source: hostname:/path/to/lfric_core
        ref: f9e8d7c


.. note::

    If any of the testing shows up failures then there are two possible ways to
    proceed:

    1. The changes made should be re-written to avoid breaking the dependant
       repositories

    2. The changes made directly affect the interface between repositories and
       therefore a change is also needed to the child repository to adapt to that change.

    If you're uncertain which route to take then the Code Owners involved will
    hopefully be able to advise.
