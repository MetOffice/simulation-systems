.. _multirepo:

Working with Multiple Repositories
==================================

The repositories covered by these working practices all interact with and have
dependencies on each other. This means that changes that affect multiple
repositories need handling with extra care.

LFRic Apps and the UM both act as top level parents to a number of child
repositories such as JULES, UKCA, SOCRATES and CASIM. These child repositories
work independently as well as being used by the parent repositories. LFRic
Apps also utilises the infrastructure in LFRic Core.

This means that changes to the science code in any of the child repositories
will need testing with both the UM and LFRic Apps to check for any
interactions.

.. note::

    From LFRic Apps vn2.1 and UM vn13.8 there are duplicate copies of the
    physics code in both the UM and LFRic Apps.

    Consideration should be made as to whether changes to the physics schemes
    are best made in LFRic Apps, the UM or both. If in doubt then the copy in
    LFRic Apps is considered the master version.

.. image:: images/repos.png
    :class: only-light

.. image:: images/repos_dark.png
    :class: only-dark

.. _linked:

Preparing Linked Pull Requests
------------------------------

Every repository in a set of linked changes requires a PR. These PRs will be
treated as a group with the same reviewers and committed at the same time.

Do:
    * Make sure every PR has a cross reference to the others in the set. A
      section will exist in the PR template for this. Use the format
      ``MetOffice/um#1234``
    * Use keywords to show which other repositories are involved
    * Get the PRs ready for review at the same time
    * Ask for help testing if you don't have access to all the codebases
      involved

.. important::

    Code branches in linked PRs will require branching from compatible
    revisions to ensure they work together.

    If working with branches from a release then all repositories will  be
    tagged with suitable keywords, e.g. um13.0 to work with UM vn13.0, or apps2.
    0 to work with LFRic Apps vn2.0.

    For head of trunk revisions make sure that all branches/revisions being
    used are at least as recent as the commits associated with the hash in the
    ``dependencies.yaml`` file.

    If in doubt, please contact the Simulation Systems and Deployment Team for
    advice.

.. _multirepo_testing:

Multi-Repo Testing
------------------

Please see :ref:`this page <multi-repo_testing>` for details on how to test
multiple repositories together.
