.. _code_review:

Code and System Review
======================

.. tip::

  GitHub documentation on the review process and interface:
  `Reviewing Proposed Changes in a Pull Request <https://docs.github.com/en/pull
  -requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/
  reviewing-proposed-changes-in-a-pull-request>`_

Purpose of the review
---------------------
The purpose of the code/system review is to analyse a change for its impact and
to ensure that all concerned parties are made aware of changes that are
required.

Fundamentally this review is to ensure that the change is well thought-out and
that no system aspects have been missed. The review should be an active one
and should question anything that is poorly coded.

Focus on the code, not the contributor; providing constructive, respectful and
actionable feedback. Critique the implementation, not the individual and always
explain the reasoning behind your suggestions.

Reviewer responsibilities and checkpoints
-----------------------------------------

The pull request template that populates the pull request description box
contains a Code Review section with questions to help you think through all the
areas of concern. This Code Review section should be completed once you are
finished.

Work through the code review template considering each question in turn. These
will include areas such as:

.. dropdown:: Is the pull request and testing complete?

    * The Pull Request Template should be filled in. This includes:
        * Proof of :ref:`testing <testing>` completed. All tests should pass
          with the exception of any known changes in answers.
        * Approvals from the code owners for every file changed.
        * If the change affects answers then approval from the owners of the
          affected configurations.
        * If the change modifies OMP code sections then approval from the
          optimisation team.
    * It should be possible to understand the purpose of the pull request from
      the details provided.

    .. tip::

        The testing summary (trac.log) provides details of the code and
        configuration owner approvals needed for each change. The approvals
        should be added by the owners themselves and this can be checked using
        the page history.

    .. tip::

        If the pull request has been completed by a non-Met Office developer it is
        useful to run tests ourselves early in the review process as different
        compilers may behave differently. It may also be necessary to run
        tests for systems that the partner has not had access to.

    .. tip::

        Quantity of testing required will vary with the complexity of the
        change and the repositories involved. Developer test groups are
        required as a minimum. As a guide for further testing consider the
        following:

        * does the change affect answers? If so `all` group must be run
        * does the change affect multiple repositories? If so the UM testing
          must include e.g. the `jules` or `ukca` groups as appropriate
        * had the reconfiguration been altered? If so the UM testing must
          include the `recon` group
        * is there another rose-stem group that covers this area of code?


.. dropdown:: Is this a :ref:`multi-repository<multirepo>` pull request?

    Each of the repositories covered by these WPs have overlapping use of
    code.

    The pull request templates in each repository contain the
    details of when testing against other repositories are required. These
    highlight where the code is likely to interact. *e.g. if code in the
    shared/science folder in JULES is modified then both the UM and LFRIc Apps
    test suites will need to be run with that change.*

    If this testing doesn't pass then either

        a) the change in pull request will need modifying so that the child
        repository's test suite passes

        b) this change requires a linked pull request in that repository so that
        all tests can pass.

    .. tip::

        All linked pull requests are reviewed as a group. Each pull request in
        the group should contain links to all the others and labels applied to
        make it easier to keep track of them all.

        Care is needed when :ref:`committing these pull requests
        <committinglinkedtickets>`.

.. dropdown:: Is the code up to scratch?

    Generally this is about making sure the code complies with the relevant
    style guides, and is consistent with the design of the code it sits in.

    * `UMDP3 (UM and JULES FORTRAN)
      <https://code.metoffice.gov.uk/doc/um/latest/umdp.html#003>`__,
    * `LFRic Coding Styles
      <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/CodingStandards>`__
    * `PEP 8 (Python) <https://legacy.python.org/dev/peps/pep-0008/>`__

    `This page
    <https://code.metoffice.gov.uk/trac/um/wiki/CodeReviewCribSheet>`__
    provides some common (though UM-centric) things to confirm and think
    about. It is not an exhaustive list, just a starting point.

Final decision points and actions
---------------------------------

The pull request will likely iterate between the reviewer and the developer
during the review process while retaining it's code review status. The Code
Reviewer can `Resolve Conversations` when they feel each query has been
satisfactorily answered.

In the case where a reviewer believes a PR requires substantial changes to be
made in order to reach sufficient quality for commit, the PR may be closed
without merging. This will be done in consultation with the developer and other
Code Owners and Reviewers.

Once you are happy that the change is appropriate and correct, and the code
review parts of the pull request template have been completed, submit a
review that `approves` the change.

From here follow the :ref:`How To Commit<howtocommit>` guide through to pull request
closure.
