.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

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
    releases/feeder_repos
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

Open a Release Curation Issue in the ``git_playground``, using the release
Issue template.

.. _github-releases:

Stable + Main Release
---------------------

This section describes the process of merging main and stable. It assumes that
any required release changes have already been merged into main and that all
sources in the dependencies.yaml file are as they should be. This section is
relevant for all repositories with a stable and main branch setup.

The release process will be completed by 2 people with commit privilege to the
relevant repository, at least one of whom must be an ``admin``. One will have
developed the release branch and the other will review it (**developer** and
**reviewer** below).

* The **developer** should open a PR directly in the MetOffice repository,
  targeting the ``stable`` branch.

    .. image:: images/gh_screenshots/main_stable_light.png
       :class: only-light border

    .. image:: images/gh_screenshots/main_stable_dark.png
        :class: only-dark border

* The **reviewer** will then review and commit the PR. When committing the
  branch, ensure that the merge method is ``merge``. This should be the default
  for the ``stable`` branch as we want to keep the history of ``main`` in the
  ``stable`` branch.
* The **developer** will then create a new PR, to merge the ``stable`` branch
  into ``main``.

    .. image:: images/gh_screenshots/stable_main_light.png
       :class: only-light border

    .. image:: images/gh_screenshots/stable_main_dark.png
        :class: only-dark border

* At this point an admin will need to modify the branch protection rules for the
  ``main`` branch, so that the commit can be performed with a normal merge. This
  keeps ``main`` and ``stable`` with an identical history.

  * Navigate to the ``main`` ruleset.
  * Disable ``Require linear history``.
  * Set ``merge`` as an allowed merge strategy and disable ``squash``.

* The **reviewer** can now ``merge`` the second PR.
* The admin **must** now revert the 2 settings above.
* The repository can be tagged with the Simulation Systems release tag in the
  format YYYY.MM.X.
  * In an upto-date clone of the repository:

  .. code-block:: shell

    git tag <tag_name>
    git push origin <tag_name>

* Finally, if appropriate, a release can be created and tagged,

  * From the GitHub repo, select ``releases`` and then ``Draft a new release``.
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
release_new_version.py script need to be on ``main``, so this will cause some
variation as to when the test release is done from release to release.


:ref:`Partner Testing<partner_testing>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All source code changes must be on ``main`` along with any rose-stem changes that
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
Partner Testing, All Jules PRs committed


:ref:`Shumlib Release<shumlib_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All shumlib PRs


:ref:`Mule Release<mule_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All mule PRs, Shumlib release (if required), UM release (to actually
install)


:ref:`feeder`
^^^^^^^^^^^^^^^^^^^

**Dependencies**
All PRs for each repository.


:ref:`UM Main Release<um_main_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All UM PRs, Test Release, Partner Testing, Jules Release


:ref:`LFRic Apps Release<lfric_apps_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All LFRic PRs (Apps + Core), Jules Release


Post Release Tasks
------------------

`Release Notes <release_notes>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Most of this can be done pre-release but some details of commit hashes will be
dependent on the main release being done.


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


:ref:`GitHub and Shared Account Permissions <shared_accounts>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
None
