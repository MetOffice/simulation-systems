.. _committinglinkedtickets:

Committing Linked Tickets
=========================

How do linked tickets work?
---------------------------

Linked tickets contain changes that all need to be committed together to work
successfully. With only some of the changes committed the repositories are
considered "out of sync", with some of the test suites likely to fail as the
api between the codebases is broken. For this reason, where possible, all
parts of a linked ticket should be committed on the same day to avoid nightly
tests failing.

:ref:`Multi-repository <multirepo>` changes are nested, and the different
branches will need approaching in the correct order. The UM and LFRIc Apps are
the key places where these overlap.

1. Everything except UM and LFRic Apps can be worked on separately and should
   be committed first.
2. LFRic Apps and the UM each rely on code from all of the above code bases,
   and will need that code for both testing and committing. They do not rely on each other.

.. tip::

    While it is possible to work through the commit process for each repository
    in turn, following this list in order, this can take a lot of time and so
    it is prudent to parallelise the process where possible.

    A suggested sequence would be as follows:

    1. Complete the merge and macro stages for every repository. These steps
       are entirely isolated and so order doesn't matter.

    2. Test all of the changes together as described below.

    3. Install KGO files for all repositories requiring them

    4. Commit the tickets as described below.


.. _testinglinked:

Testing linked tickets
----------------------

With the branches from all the tickets merged into a working copy of their
respective Head of Trunk these can all be used together to test the change.

Details for testing multi-repository tickets are included on the
:ref:`Working with Multiple Repositories page<multirepo>`.

**In summary:**

- JULES, UKCA, LFRic Core and other child repositories can be tested using
  their standalone test suites as described on the How to Commit page.

- Local working copies can be passed to the UM on the command line

    .. code-block:: shell

        rose stem --group=developer,ukca,jules --source=. \
            --source=/path/to/jules/working/copy \
            --source=/path/to/ukca/working/copy

    Make sure you test the group that will exercise the interface between those
    repositories(e.g. in the above example the jules and ukca groups are
    tested).

- Local working copies of any linked JULES, UKCA or other repositories can be
  passed to LFRic Apps through <lfric_apps_trunk>/dependencies.sh.

.. code-block:: shell

    jules_sources=vldXXX:/path/to/um/working/copy


.. tip::

    It is always important that branches and working copies used for testing
    multiple repositories together have been taken at the same point in time.
    If this isn't the case then API breaking changes may be included in one
    repository but not another which will cause tests to fail.

    The developer will likely have used branches taken from the last releases
    which are a known set of stable revisions which work together.

    Make sure the testing done here (just prior to commit) is using the latest
    head of all the trunks. Assuming nightly tests are passing then this is
    also a known set of revisions that work together.

.. tip::

    If some of the changes in this set of tickets have already been committed
    then see steps 2 and 4 below on how to include those changes in your
    testing. This is instead of the steps described above.

    e.g. If JULES changes have been committed and the revision number modified
    in rose-suite.conf then the working copy no longer needs supplying as a
    `source` to the UM testing.

.. _committinglinked:

Committing linked tickets
-------------------------

.. admonition:: todo

    Ensure that dependencies.yaml file instructions below are correct

Once you are happy with all your testing then the commit sequence is as
follows:

* Commit all trunks **except** UM and LFRic Apps. Make note of the commit
  revision numbers.

* For each of LFRic Apps and UM as required,

    * In a clone of the branch, edit the ``dependencies.yaml`` file:

        * Remove any references from the ``*_sources`` variables.
        * Modify ``*_ref`` variables for all other repositories you have
          updated to point to the the new commit hashes.
        * e.g. If a JULES ticket has been committed with has abc123 and a UKCA
          ticket at 456def,

        .. code-block:: shell

            export jules_sources=MetOffice/jules
            export jules_ref=abc123

            export ukca_sources=MetOffice/UKCA
            export ukca_ref=456def

    * Commit these changes and push back to the developers branch, along with
      any changes to macros and KGO. Finally you can :ref:`commit <commit>`
      the pull request.
