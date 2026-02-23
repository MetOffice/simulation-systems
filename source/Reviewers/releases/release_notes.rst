.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _release_notes:

Release Notes
=============

Release notes are included in each repository that has a release. An overarching
set of release notes in also included in the simulation-systems wiki pages.

Ask key people for input on what should be included. This might include managers
of involved teams, developers who have contributed multiple PRs, and the Code
Reviewer pool.

* The repository releases are versioned with ``vnX.Y``. The number varies by repository.
* The Simulation Systems releases are versioned as ``YYYY.MM.N``.

Repository Release Notes
------------------------

When creating a release, use the ``Generate Release Notes`` button to create a
full list of changes being included. Then above this add a summary section that
is formatted like this:

.. code-block::

    # <Repository Name> vnX.Y release notes

    Summary statement if appropriate

    ## Key Changes
        * ...

        Tip: If lots of these, split into subsections as appropriate

    ## Breaking Changes
    _These changes will affect suites upgrading to this release_
        * ...

        No known breaking changes at this release.

    ## Known Issues
        * ....

        No known issues at this release.

    ## Linked Changes
    This release is part of the [YYYY.MM.N Simulation Systems Release.]
    (https://github.com/MetOffice/simulation-systems/wiki/YYYY.MM.N). All
    codebases required by <repository>, including <some other repositories>
    etc, have been tagged ``YYYY.MM.N``.


Simulation Systems Release Notes
--------------------------------

Create a new wiki page:

.. image:: images/gh_screenshots/release_notes_light.png
    :class: only-light border

.. image:: images/gh_screenshots/release_notes_dark.png
    :class: only-dark border

#. Click the pencil in the `wiki sidebar <https://github.com/MetOffice/simulation-systems/wiki>`_
   to edit it.

#. Add the new release YYYY.MM.N to the release notes section and save.

#. Click the link in the sidebar you just created to add the new page.

#. The contents of this page should be formatted like this:

.. code-block::

    # Simulation Systems YYYY.MM.N Release

    Release date:

    ## Included Releases
    * [LFRic Apps vnX.Y](https://github.com/MetOffice/lfric_apps/releases/tag/vnX.Y)
    * [LFRic Core vnX.Y](https://github.com/MetOffice/lfric_core/releases/tag/vnX.Y)
    * [UM vnX.Y](https://github.com/MetOffice/um/releases/tag/vnX.Y) (private within the MetOffice organisation)
    * [JULES vnX.Y](https://github.com/MetOffice/jules/releases/tag/vnX.Y) (currently private, will hopefully soon be publically available)

    ## Key Highlights
    * A few highlights the affect multiple repositories
    * or that are particularly special and are worth raising the profile of at this level

    ## Software Stack Updates
    * Any package changes to the software stack
    [Full LFRic Software Stack details](https://metoffice.github.io/lfric_core/getting_started/installation/software_dependencies.html)
