.. _reviews:

Reviews
=======

Changes will usually go through a 2-stage review process:

#. SciTech review; carried out by someone that understands the area of code
   being developed
#. CodeSys review; carried out by a member of the Simulation Systems and
   Deployment Team or the Core Capability Development Team

Trivial tickets are an exception and do not require a SciTech review.

:ref:`Linked tickets <linked>` will move through the review states together.

.. note::

    Expect some iteration with the reviewers. This aims to improve the quality
    of your change, considering a range of scientific and technical aspects.
    Normally, this process is indicated by ticket ownership changing whilst
    maintaining the ticket status. By exception, if a change needs major
    reworking, then it will be regressed to 'in progress'.

.. tip::

    Tickets included in a release are based on those in code review before the
    code review deadline. Get ready for review with plenty of time to give
    SciTech reviewers and the approvers time to do their jobs.

.. important::

    Get in touch with your SciTech Reviewer before you feel ready for review.
    They will have valuable insights into the code and, particularly for
    larger changes, may appreciate the opportunity to look at your work as it
    progresses.

.. important::

    While your reviewers are in a good position to advise and make suggestions
    on your changes it is also important that they are able to maintain an
    impartial perspective, and therefore should not get involved in the
    development.

    In the case that a reviewer, either SciTech or Code, does get too involved
    then another person should be brought in to finish the review process and
    provide that external viewpoint.

.. tip::

    The reviewer will likely leave comments, all of which should be addressed
    by the developer. The developer should **not** resolve these comments
    themselves, instead allowing the reviewer to resolve them when they are
    happy with the response.


Preparing for Review
--------------------

To help you get ready for review a :ref:`Ticket Summary <template>` should be
attached to each ticket involved in your change. This will provide a checklist
of things to consider including approvals, documentation and testing.
Following this through completely makes a big difference to the review
experience.

Once you are happy that everything is in place then you are ready to continue
to review.

.. important::

    If your development changes answers then make sure you have followed the
    steps on :ref:`preparing a KGO ticket for review.<kgo>`

    If you suspect there may be a change in answers but none have shown up
    during testing then run the rose-stem ``all`` group to confirm this.

.. Tip::

    Check that your changes meet the coding standards for the codebase you are
    working on:

    * `UMDP3 (UM and JULES FORTRAN)
      <https://code.metoffice.gov.uk/doc/um/latest/umdp.html#003>`_,
    * `LFRic Coding Styles
      <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/CodingStandards>`__
    * `PEP 8 (Python) <https://legacy.python.org/dev/peps/pep-0008/>`_

.. Tip::

    Remember to follow all code-related steps and commit all your changes
    before running final testing to avoid needing to re-run.

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
should go to the main code owner(s) for the area affected. If they don't want
to then they may have suggestions for other suitable reviewers or you can
approach anyone who would have good insight into the changes made.

Changes that have a linked LFRic Core ticket should find a SciTech reviewer
from the CCD Team.

The review process will iterate between the developer and reviewer until the
changes made are agreed to be of sufficient quality. The SciTech reviewer will
fill in a :ref:`SciTech Review Checklist <template>` which makes sure all
aspects of the ticket are considered. Once the reviewer is satisfied, they
will pass the ticket on to code/system review.

Guidance for the SciTech reviewer can be found on the
:ref:`SciTech review page <scitech_review>`.

.. _codereview:

Code and System Review
----------------------

Requesting a code reviewer is the responsibility of the developer and is done
by emailing the :ref:`SSD Team <ssd>`. Reviewers are assigned to email
requests a couple of times a week.

The code reviewer will check that the change meets the coding standards and
fits with the overall system design. They will also fill in a :ref:`Code
Review Checklist <template>` to ensure that nothing is overlooked.

Again, the review process is likely to be iterative between the code reviewer
and the developer with the ticket ownership passing between the two while
keeping the status as Code Review. If major changes are needed then the ticket
may be rejected which will put it back to `In Progress` and a further SciTech
Review will be needed in this case.

Once the code reviewer is satisfied they will move the ticket into the
``approved`` state, ready for commit to the trunk.

Guidance for the code reviewer can be found on the
:ref:`Code Review page <code_review>`.

.. _reviewer_edits:

Code Reviewer Edits
^^^^^^^^^^^^^^^^^^^

As part of the process to commit certain tickets, code reviewers will sometimes
need to commit changes to the branch of a developer. Common reasons for doing
this include,

* Updating KGO's
* Applying upgrade macros
* Updating commit hashes for linked tickets

The ability to commit back to another users fork is only available to those
with ``maintainer`` access or above and they can only do so for branches with
an open pull request and the ``Allow edits by maintainers`` option selected.

-----

.. _template:

.. admonition:: todo

    Check all references to the template reference defined here
