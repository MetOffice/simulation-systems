Reviews
=======

To help you get ready for review a :ref:`Ticket Summary <template>` should be
attached to each ticket involved in your change. This will provide a checklist
of things to consider including approvals, documentation and testing. Following
this through completely makes a big difference to the review experience.

Once you are happy that everything is in place then you are ready to continue
to review.

.. Tip::
    Remember to follow all code-related steps and commit all your changes before
    running final testing to avoid needing to re-run.

.. Tip::
    Sometimes you may wish to proceed with the reviews without all approvals in
    place. Take a risk based approach and make sure the approvals are clearly
    pending.

    Some reasons to do this include:
        * An approver and their deputy have not replied
        * The outstanding approver is also one of the reviewers
        * Time pressure combined with a low risk or complexity of ticket

.. _scitech:

Science/Technical Review
------------------------


.. _codereview:

Code Review
-----------


.. _template:

.. Tip::
    **Page Templates**

    To help with the review process each step has a wiki page template that
    should be used and filled in. To do this:

    1. Add one of the below lines to the ticket (in either the `associated with` or `description` box), replacing tXXXX with your ticket number

    .. code-block::

       [wiki:ticket/tXXXX/TicketSummary]
       [wiki:ticket/tXXXX/TicketDetails]
       [wiki:ticket/tXXXX/SciTechReview]
       [wiki:ticket/tXXXX/CodeSystemReview]

    2. Click the `preview` button and you will see a greyed out link (as this doesn't yet exist). Click the link this creates to open a new "blank" wiki page.
    3. Select the appropriate template from the drop down list, then click `Create this page`.
