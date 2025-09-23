.. _working_practices_index:

Working Practices
=================

The Working Practices (WPs) are a developers guide and are to be followed for
all UM, LFRic Applications, JULES, and UKCA developments (though reference is
also made to LFRic Core, CASIM, SOCRATES and Shumlib where relevant).

If this is your first development we highly recommend following these pages
through in sequence.

Suggestions for changes to these WPs are always gratefully received, though
note that we get regular feedback that the WPs are both too long and too
short. What may be overwhelming detail for one person may be insufficient
detail for another.

.. note::

    Details of recent changes to these practices can be found :ref:`here
    <changes>`

Development Cycle Overview
--------------------------

The general features of the development cycle are similar to those found in
other scientific software. However, the details are tuned to meet the needs of
the community as a whole. A key feature is the use of versions as a way of
periodically bringing everything together.

The release cycle follows a semi-regular cadence, balancing flexibility to
facilitate high priority goals against stability for the broader developer
pool. Each release will consist of a development window spanning from release
of the previous version to a pre-announced code review deadline. Following
this, submissions will be processed culminating in the next release. From time
to time, some or all parts of a repository may be subject to an agreed closed
release to facilitate an intense or disruptive development.

.. image:: images/development_cycle.png
    :class: only-light

.. image:: images/development_cycle_dark.png
    :class: only-dark

The release cycle is overseen by the Simulation Systems and Deployment Team
with the oversight and support of the Simulation Systems Governance Group, who
impartially consider the needs of all developers and users.


Development Process
-------------------

The process of developing a change for each repository is described through
these Working Practices. A flowchart of this process for the UM is included
below, but the process is very comparable to that of the other repositories
too.

.. note::

    In the following Working Practices, we will endeavour to provide options
    for using the Github Web Interface and the ``gh`` cli where possible.
    Further information will be available in the github documentation.

    To get started with the ``gh`` cli, see the `gh quickstart guide
    <https://docs.github.com/en/github-cli/github-cli/quickstart>`__

.. admonition:: Definitions

    ``Clone``: a local copy of either the upstream or the forked repository.

    ``Fork`` or ``Downstream``: a copy of the upstream repository, owned by the
    developer. This is where development branches are created and worked on.

    ``Origin``: the default name for the remote source of a cloned repository.

    ``Remote``: the version of either the upstream or the forked repository
    that is hosted by Github.

    ``Upstream``: the primary or parent repository, owned by the MetOffice
    github organisation. Only code reviewers are able to directly interact
    with this repository, rather than being required to use forks.


    Further definitions can be found in the `GitHub Glossary
    <https://docs.github.com/en/get-started/learning-about-github/github-glossary>`__.

Simulation Systems github repositories are setup with at least 2 protected
branches, ``main`` and ``stable`` (with the potential for additional version
branches to be added).

* ``main`` - This is the default github branch and is the branch that new
  development pull requests should target. It will never be behind ``stable``
  branch, but will regularly be ahead.
* ``stable`` - This branch represents the codebase at a version release and
  will generally remain unchanged throughout a release cycle. New branches
  should be made from this branch (or from a release tag.) Only new releases
  and small hotfixes to a release will be merged back into this branch.

All general development for Simulation Systems Github repositories will take
place on forks of that repository. It is the responsibility of the developer
to maintain their own fork. See :ref:`forking` for advice on forking.

The development cycle can be seen below.

.. image:: images/git-dev-strategy.svg
    :class: dark-light

For detailed explanation of these steps, see pages on :ref:`gh_dev_init` and
:ref:`pull_requests`.

Before You Start
----------------

All developments should be planned using a risk-based approach. Before
starting, consider the complexity and impact of what you want to do. This will
act as a guide for the level of planning and consultation required. There is
no definitive process for this and developers should use their experience and
judgement.

As you begin, there are various people you might consider consulting:

* Relevant :ref:`Code and Configuration Owners <approvals>`
* Simulation Systems and Deployment Team
* Core Capability Development Team
* Less experienced developers may benefit from a 'buddy'

For larger changes, consider splitting the work over multiple tickets:

* Tickets laying foundations for later are OK
* Tickets should make sense on their own, with a clear scope, to allow for
  separate testing, review and commit
* Tickets should not be too small or too large
* Beware of the 'also trap'- the 'also' bits can swamp the main aim of your
  change!
* An overarching ticket that sets out the overall picture and tracks the
  progress of the work is recommended and all sub-tickets should link back to
  it

Consider the timing of your work:

* Be aware of others doing work in similar areas
* Be aware of code review deadlines
* Be aware of closed releases or planned outages
* Allow contingency time when agreeing broader project deadlines. Trunk
  integrity will not be compromised to meet your deadlines.

Consider bringing planning together using an overarching ticket. It can be very
helpful for documenting and monitoring progress of your work.

.. tip::

    Early planning and consultation is strongly recommended to prevent
    disappointment later. More detailed guidance is provided on the
    :ref:`planning` page.


.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Working Practices

    gh_authorisation
    forking
    gh_dev_init
    multi_repository
    approvals
    pull_requests
    final_steps
    git_extras
