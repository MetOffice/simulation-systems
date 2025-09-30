Curating a Release
==================

.. toctree::
    :maxdepth: 1

    releases/um_test_release
    releases/partner_testing
    releases/software_stack
    releases/jules_release
    releases/shumlib_release
    releases/mule_release
    releases/um_main_release
    releases/lfric_apps_release
    releases/release_notes
    releases/standard_suites
    releases/stash_browser
    releases/umdp_release
    releases/wiki_pages
    releases/shared_accounts
    releases/updating_prebuilds

.. _reference-tagging:

Release Issue
-------------

Open a ``git_playground`` release Curation Ticket, and assign tasks as a team,

.. code-block::

    The following tasks are required to deliver <Month>/<Year> releases:

    | Item | Led By | PR |
    | :--- | :--- | :--- |
    | **Pre Release** |  |  |
    | UM Test Release |  |  |
    | Partner Testing |  |  |
    | Scientific Software Stack Update |  |  |
    | **Release** |  |  |
    | Jules Release |  |  |
    | Shumlib + Mule Releases |  |  |
    | UM Main Release |  |  |
    | LFRic Apps Release |  |  |
    | **Post Release** |  |  |
    | Release Notes |  |  |
    | Update Standard Suites |  |  |
    | Install Stash Browser |  |  |
    | UMDP Release |  |  |
    | Standard Jobs + Wiki Page |  |  |
    | Review repo and shared account permissions |  |  |

    [https://metoffice.github.io/simulation-systems/Reviewers/curaterelease.html Curating a release Page]

.. _github-releases:

Stable + Main Release
---------------------

This section describes the process of merging a release branch onto main and
stable. It assumes that a branch has been created from main, and that any
changes required for the release have been committed to it and tested. This
section is relevant for all repositories with a stable and main branch setup.

.. note::

    Some repos (Socrates, Casim) do not require release changes, so a PR should
    just be opened to merge the ``main`` branch into the ``stable`` branch. Then
    a second PR should be opened to merge ``stable`` back into ``main`` to
    ensure ``main`` is never behind. Any tags required can then be made at this
    point.

The release process will be completed by 2 people with commit privilege to the
relevant repository, at least one of whom must be an ``admin``. One will have
developed the release branch and the other will review it (**developer** and
**reviewer** below).

* Once development and local testing has been completed, the **developer**
  should open a PR, targetting the ``stable`` branch.
* The **reviewer** will then review and commit the branch. When committing the
  branch, ensure that the merge method is ``merge``. This should be the default
  for the ``stable`` branch as we want to keep the history of ``main`` in the
  ``stable`` branch.
* The **developer** will then create a new PR, to merge the ``stable`` branch
  into ``main``.
* At this point an admin will need to modify the branch protection rules for the
  ``main`` branch, so that the commit can be performed with a normal merge. This
  keeps ``main`` and ``stable`` with an identical history.

  * Navigate to the ``main`` ruleset.
  * Disable ``Require linear history``.
  * Set ``merge`` as an allowed merge strategy and disable ``squash``.

* The **reviewer** can now ``merge`` the second PR.
* The admin **must** now revert the 2 settings above.
* Finally, the release can be created and tagged,

  * From the github repo, select ``releases`` and then ``Draft a new release``.
  * Create a new tag and title the release with the same name, eg. ``vn14.0``.
  * Select to ``Generate release notes``.
  * Then ``Publish release``.


Pre-Release
-----------

:ref:`UM Test Release<um_test_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
The point of the test release is to test the release system/process works
before we have to do it for real. Typically aim for 1-2 weeks before release
day. However, before a test release can be done, all changes to fcm-make
config files, major rose-stem changes (things like basic upgrade macro or KGO
updates don't necessarily need to be included) and modifications to the
release_new_version.py script need to be on trunk, so this will cause some
variation as to when the test release is done from release to release.


:ref:`Partner Testing<partner_testing>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All source code changes must be on trunk along with any rose-stem changes that
affect multiple sites before partner testing can start. Ideally the test
release will also have been completed.


:ref:`Software Stack<software_stack>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Any potential changes to platform software stacks


Main Release
------------

:ref:`Jules Release <jules_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Partner Testing, All Jules tickets committed


:ref:`Shumlib Release<shumlib_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All shumlib tickets


:ref:`Mule Release<mule_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All mule tickets, Shumlib release (if required), UM release (to actually
install)


:ref:`UM Main Release<um_main_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All UM Tickets, Test Release, Partner Testing, Jules Release


:ref:`LFRic Apps Release<lfric_apps_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All LFRic Tickets (Apps + Core), Jules Release


Post Release Tasks
------------------

`Release Notes <release_notes>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Most of this can be done pre-release but some details of revision numbers will
be dependent on the main release being done.


:ref:`Updating Standard Suites <standard_suites>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM + Apps Releases


`Stash Browser <stash_browser>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release


`UMDP Release <umdp_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release, Standard Suites Upgrade


:ref:`Standard Jobs and Wiki Pages <wiki_pages>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM + Apps Releases


:ref:`Trunk and Shared Account Permissions <shared_accounts>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
None
