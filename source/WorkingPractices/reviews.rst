Reviews
=======
Changes will usually go through a 2-stage review process:

    1. SciTech review; carried out by someone that understands the area of code being developed
    2. CodeSys review; carried out by a member of the Simulation Systems and Deployment Team or the Core Capability Development Team

Trivial tickets are an exception and do not require a SciTech review.

:ref:`Linked tickets <linked>` will move through the review states together.

.. note::
    Expect some iteration with the reviewers. This aims to improve the quality of
    your change, considering a range of scientific and technical aspects. Normally,
    this process is indicated by ticket ownership changing whilst maintaining the
    ticket status. By exception, if a change needs major reworking, then it will be
    regressed to 'in progress'.

.. tip::
    Tickets included in a release are based on those in code review before the
    code review deadline. Get ready for review with plenty of time to give
    SciTech reviewers and the approvers time to do their jobs.

Preparing for Review
--------------------
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
The SciTech review is done by someone who is familiar with the area being
changed to check that the change does what is says, in a sensible way, and
doesn't do what it shouldn't. First refusal for completing the SciTech review
should go to the main code owner(s) for the area affected. If they don't want to
then they may have suggestions for other suitable reviewers or you can approach
anyone who would have good insight into the changes made.

The review process will iterate between the developer and reviewer until the
changes made are agreed to be of sufficient quality. The SciTech reviewer will
fill in a :ref:`SciTech Review Checklist <template>` which makes sure all
aspects of the ticket are considered. Once the reviewer is satisfied, they will
pass the ticket on to code/system review.

Guidance for the SciTech reviewer can be found :ref:`here <scitech_review>`.

.. _codereview:

Code and System Review
----------------------
Organising the code reviewer is the responsibility of the developer and is
done by emailing the :ref:`ssd`. Reviewers are assigned to email requests a
couple of times a week.

The code reviewer will check that the change meets the coding standards and fits
with the overall system design. They will also fill in a :ref:`Code Review
Checklist <template>` to ensure that nothing is overlooked.

Again, the review process is likely to be iterative between the code reviewer
and the developer with the ticket ownership passing between the two while keeping
the status as Code Review. If major changes are needed then the ticket may be
rejected which will put it back to `In Progress` and a further SciTech Review
will be needed in this case.

..
    .. note::
    For LFRic only developments you can also contact the :ref:`cap_dev_team`
    directly or use the *request a code review* option on the ticket to
    move your ticket into `ready_for_code_review` status. Once a week tickets
    in this status are assigned a reviewer.

Once the code reviewer is satisfied they will move the ticket into the `approved`
state, ready for commit to the trunk.

Guidance for the code reviewer can be found :ref:`here <code_review>`.

-----

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
    4. The page created will contain an appropriate checklist which should be completed by deleting each Y/N/NA and adding comments as appropriate.
