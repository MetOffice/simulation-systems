Simulation Systems Glossary
===========================

Please suggest new entries to the Simulation Systems and Deployment Team

Closed Release:
    A release cycle where the only accepted changes to the trunk relate to a
    particular piece of work, either technical or scientific. A release can
    also be partially closed, with only one area of a code base locked down in
    this way, and the rest free for changes.

Code Review Deadline:
    The date by which all tickets aiming to be included in a release have been
    moved into code review.

Colon Keyword:
    The formatting pattern for certain ticket keywords. For example CR:user to
    indicate that "user" will be performing the Code System Review.

CodeSys Review:
    A technical review of the changes involved in the ticket, including checks
    that code standards have been upheld and that the working practices have
    been followed. These reviews are generally completed by a member of the
    Simulation Systems and Deployment Team. Once a review has been approved
    the Code Systems Reviewer is then responsible for committing the change to
    the trunk.

..
    or the Core Capability Development Team (for LFRic only reviews).

Development Window:
    The period of time between the release of one software version and the code
    review deadline for the following release in which new developments are
    accepted for review.

Further Commit:
    Where a problem is found with a ticket after it has been committed, any
    additional commits needed are associated with the same ticket and labelled
    as a "Further Commit". Only essential and immediate fixes are treated this
    way.

Known Good Output (KGO):
    In order to verify that the model output hasn't been modified by a set of
    changes the test suite contains a stored set of output as a reference.
    This is known as the KGO and changes that alter this require special
    treatment. For more information see :ref:`kgo`.

Head of Trunk:
    The most recent code revision on the trunk. Branches are taken from here
    when the work being done *has* to be built on top of changes already made
    since the last revision.

Linked Ticket:
    Work that spans two or more repositories, requiring tickets that should be
    treated together and committed as a group.

Overarching Ticket:
    Where a piece of work has been split into multiple sections and tickets an
    extra ticket can be used to track this work. It should be closed when the
    whole arc has been completed.

Regression:
    A set of tests that prove that a set of code changes have not degraded the
    model output. Comparisons are made between the results produced and the
    Known Good Output.

SciTech Review:
    A science or technical review, completed by someone who is familiar with
    the area being changed. The aim of this review is to confirm that the
    changes made do what they say they should, and that the method used was
    appropriate.

Simulation Systems and Deployment Team:
    The team responsible for the oversight of these working practices. For more
    information see :ref:`ssd`.

Simulation Systems Governance Group:
    The governing body that oversees the work of the Simulation Systems and
    Deployment Team.

Version:
    Each release of the codebase is completed by tagging the latest revision of
    the trunk with a version number. This version should be used for creating
    code branches from and will also be used by the parallel suite teams as a
    starting point for creating the next operational suite.
