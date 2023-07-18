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

**Is the ticket and testing complete?**

    * A Ticket Summary should be attached and filled in. This includes:
        * Proof of :ref:`testing <testing>` completed.
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

**Is this a :ref:`multi-repository <multirepo>` ticket?**

    Each of the repositories involved have overlapping use of code. There are
    details in the Ticket Summary and Code Reviewer templates of when testing
    is required for tickets that may interact with other repositories.

    If this testing doesn't pass then a ticket with code change will be required
    in that other repository and the ticket is considered linked to the one you
    are reviewing.
    * If this is a multi-repository change then links to all those tickets should be present along with the relevant keywords.
      Care is needed when :ref:`committing these tickets <committinglinkedtickets>`.
    * What does LFRic testing mean?

**Is the code up to scratch?**

    Generally this is about making sure the code complies with the relevant
    style guides, and is consistent with the design of the code it sits in.

    It's impossible to provide a complete checklist for this, but below are some
    common things to confirm.

    UM:
    * Are the default settings for any new inputs `.FALSE.`, `imdi` or `rmdi`?
    * Have any change to the `atmos_physics` routines in `atm_step` been replicated in `scm_main`?
    * Do all new `ALLOCATE` statements have a counterpart `DEALLOCATE`?
    *


