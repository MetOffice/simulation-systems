Final Steps
===========

Once your change is approved, the code reviewer will follow the
:ref:`howtocommit` process on any branches in order to commit them
to the trunk of each project. Depending on any linked tickets and
documentation updates, there may be several commits to different
trunks involved.

.. note::
   Sometimes there can be a delay between a code change being approved
   and the commit to trunk. This can be for a number of reasons. If you
   have any concerns, please contact your CodeSys Reviewer in the first
   instance.

Overnight and Weekly Testing
----------------------------

Each project is tested overnight. Often this involves several related
repositories being tested together (e.g. the UM and JULES repositories
are related, so the head of the UM trunk is tested with the head of the
JULES trunk). Testing is usually based on the rose stem system.

In addition, UM and related projects run weekly tests, which involve
some longer jobs not normally tested in the nightly tests.

Closing Tickets
---------------

If the test suite runs without issues, the CodeSys reviewer will close the
ticket(s) as 'fixed' and reassign them back to the developer. This is
usually the end of the process and the code changes will form part of the
next release.


When the Trunk is Broken
------------------------

Occasionally, the overnight testing will fail. Sometimes this may be
due to a transient issue (e.g. with jobs timing out), in which case
re-triggering the failed job will often suffice. If this doesn't
solve the issue, the trunk(s) of affected projects will be closed.
The Simulation Systems and Deployment team will investigate and
aim to resolve the issue and reopen the trunk(s) as soon as
possible. Two possible scenarios may occur:

  #. For **simple or obvious fixes**, a second commit is the preferred solution, allowing the change to be fixed, while remaining on the trunk.

  #. If the reason for the failure is complex or less obvious, the Simulation Systems and Deployment team will revert the offending change off the trunk(s).

In the first case, if the test suite comes back clean, the ticket will be closed,
as above. In the second case, the ticket will be returned to the original developer,
allowing them to fix the issue for a later commit, either during the current
release if time permits, or alternatively during a later release cycle.

Reopening Tickets
-----------------

Very rarely, an issue will be discovered with a ticket some time after it has been
committed to the trunk. The most common case is when the nightly tests pass, but
the weekly tests fail. In this case, the ticket will be reopened and the issues
fixed. In most cases, this is preferred to reverting the change off the trunk
as it can be cumbersome to revert a change after there have been several further
commits to the trunk head.


Changes to the Working Practices
--------------------------------

These working practices have evolved over many years of experience and in order
to try and catch as many issues as possible. However, feedback is welcome at
any time. Please suggest improvements to the Simulation Systems and Deployment
team.

Suggestions received will be evaluated and responded to, but a final decision
as to whether the working practices will be modified lies with the Simulation
Systems and Deployment team and ultimately the Atmos Project Board.
