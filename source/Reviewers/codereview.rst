.. _code_review:

Code and System Review
======================

Purpose of the review
---------------------
The purpose of the code/system review is to analyse a change for its impact
and to ensure that all concerned parties are made aware of changes that are required.

Fundamentally this review is to ensure that the change is well thought-out and
that no system aspects have been missed. The review should be an active one and should question anything that is poorly coded.

Reviewer responsibilities and checkpoints
-----------------------------------------
The Code/System review template exists to help you think through all the areas
of concern. A completed :ref:`review template <template>` should be appended to
the ticket once you are finished.

Work through the code review template considering each question in turn. These
will include areas such as:

.. dropdown:: Is the ticket and testing complete?

    * A Ticket Summary should be attached and filled in. This includes:
        * Proof of :ref:`testing <testing>` completed. All tests should pass
          with the exception of any known changes in answers.
        * Approvals from the code owners for every file changed.
        * If the change affects answers then approval from the owners of the affected configurations.
        * If the change modifies OMP code sections then approval from the optimisation team.
    * It should be possible to understand the purpose of the ticket from the details provided.

    .. tip::
        The testing summary (trac.log) provides details of the code and configuration
        owner approvals needed for each change. The approvals should be added by the
        owners themselves and this can be checked using the page history.

    .. tip::
        If the ticket has been completed by a non-Met Office developer it is useful
        to run tests ourselves early in the review process as different compilers
        may behave differently. It may also be necessary to run tests for systems
        that the partner has not had access to.

    .. tip::
        Quantity of testing required will vary with the complexity of the change
        and the repositories involved. Developer test groups are required as a
        minimum. As a guide for further testing consider the following:

        * does the change affect answers? If so `all` group must be run
        * does the change affect multiple repositories? If so the UM testing must include e.g. the `jules` or `ukca` groups as appropriate
        * had the reconfiguration been altered? If so the UM testing must include the `recon` group
        * is there another rose-stem group that covers this area of code? See :ref:`um_testing` for common examples

.. dropdown:: Is this a :ref:`multi-repository<multirepo>` ticket?

    Each of the repositories covered by these WPs have overlapping use of code.

    The Ticket Summary/Code Review templates in each repository contain the details
    of when testing against other repositories are required. These highlight where
    the code is likely to interact. *e.g. if code in the shared/science folder in*
    *JULES is modified then both the UM and LFRIc Apps test suites will need to be run with that change.*

    If this testing doesn't pass then either
        a) the change in ticket will need modifying so that the parent repository's test suite passes
        b) this change requires a linked ticket in that repository so that all tests can pass.

    .. tip::
        All linked tickets are reviewed as a group. Each ticket in the group should
        contain links to all the others and the correct keywords applied to make it
        easier to keep track of them all.

        Care is needed when :ref:`committing these tickets <committinglinkedtickets>`.

.. dropdown:: Is the code up to scratch?

    Generally this is about making sure the code complies with the relevant
    style guides, and is consistent with the design of the code it sits in.

    * `UMDP3 (UM and JULES FORTRAN) <https://code.metoffice.gov.uk/doc/um/latest/umdp.html#003>`_,
    * `LFRic Coding Styles <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/CodingStandards>`_
    * `PEP 8 (Python) <https://legacy.python.org/dev/peps/pep-0008/>`_

    `This page <https://code.metoffice.gov.uk/trac/um/wiki/CodeReviewCribSheet>`_
    provides some common (though UM-centric) things to confirm and think about.
    It is not an exhaustive list, just a starting point.

Final decision points and actions
---------------------------------

The ticket will likely iterate between the reviewer and the developer during the
review process while retaining it's code review status. However, the reviewer
has the option to "reject and assign" back to the code author should the
documentation or code not meet the required standards and major alterations/improvements
are required. In this case the change will need a further SciTech review before
it can be returned to the code reviewer.

Once you are happy that the change is appropriate and correct, complete the
approval section of the Code/System review template and change the ticket status
to **approved**.

From here follow the :ref:`How To Commit<howtocommit>` guide through to ticket closure.
