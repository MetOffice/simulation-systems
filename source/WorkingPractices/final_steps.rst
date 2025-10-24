Final Steps
===========

Once your change is approved, the code reviewer will follow the
:ref:`howtocommit` process on any branches in order to commit them to the
``main`` of each project. Depending on any linked PRs and documentation updates,
there may be several commits to different trunks involved.

.. note::

    Sometimes there can be a delay between a code change being approved and the
    commit to ``main``. This can be for a number of reasons and rarely will be
    due to your change. If you have any concerns, please contact your CodeSys
    Reviewer in the first instance.

Overnight and Weekly Testing
----------------------------

Each project is tested overnight. This includes several related repositories
being tested together (e.g. the UM and JULES repositories are related, so the
head of the UM ``main`` is tested with the head of the JULES ``main``). Testing
is usually based on the rose stem system.

In addition, most projects run weekly tests, which involve some longer jobs not
normally tested in the nightly tests.

Closing Pull Requests
---------------------

GitHub will automatically close PRs upon merge. The code reviewer will check the
output of nightly testing, and if this shows errors may begin a discussion on
the pull request. Some testing is only run weekly, so some issues may take
longer to show up.


When Main is Broken
-------------------

Occasionally, the overnight testing will fail. If the issue can't be
immediately solved, the ``main`` of affected projects will be closed to new
changes. The relevant teams will investigate and aim to resolve the issue and
reopen the ``main`` as soon as possible. Two possible scenarios may occur:

  #. For **simple or obvious fixes**, a trivial PR to fix ``main`` is preferred.

  #. If the reason for the failure is complex or less obvious, the team will
     revert the offending change off ``main`` .

In both cases any further PRs should link back to the original.


Changes to the Working Practices
--------------------------------

These working practices have evolved over many years of experience and in order
to try and catch as many issues as possible. However, feedback is welcome at
any time. Please suggest improvements to the Simulation Systems and Deployment
team.

Suggestions received will be evaluated and responded to, but a final decision
as to whether the working practices will be modified lies with the Simulation
Systems and Deployment team and ultimately the Simulation Systems Governance
Group.
