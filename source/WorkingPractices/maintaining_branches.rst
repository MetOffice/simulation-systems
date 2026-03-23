.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _maintaining_branches:

Maintaining Branches
====================

Simulation Systems repositories use version branches to aid in scientific
evaluation and testing. This means that all new branches should be taken from a
release and should not be updated with the latest changes on ``main`` until
ready to be merged. Exceptions can be made for changes that are specifically
building on changes already merged since the last release.

Developments that take longer than one release cycle can be upgraded to the
new release when convenient, and should be upgraded before opening a pull
request.

.. _upgrading_to_release:

Upgrading to a release
----------------------
There are two main ways to upgrade your branch to a new release. If you are
developing the same change in parallel at different versions then you may wish
to create a new branch from latest release and merge the old changes into this.
Otherwise we would recommend merging the release from ``stable`` into your branch.

In both cases we recommend use of tagging to mark the changes on your branch for
including in suites at different versions. This will give a human-readable
identifier to make it clear which version the suite user is including. Tags can
be applied retrospectively if needed, and can be used as a branch point if
development is needed at an older revision. Tags can also be moved to track
the latest developments.

Below are an example set of commands for both cases. There are many ways to
achieve the same result so see the sections on
:ref:`Synchronise your fork<syncing_fork>` and
:ref:`Updating a branch<updating_branch>` for more details.

.. tab-set::

  .. tab-item:: Merging in Stable

    #. tag latest commit on branch to mark the latest developments at the old release
    #. update stable branch in fork
    #. fetch that into clone
    #. merge stable into branch
    #. push


  .. tab-item:: Creating a New Branch

    #. update stable branch in fork
    #. fetch that into clone
    #. create branch from stable
    #. merge old development branch into new development branch
    #. tag both?


.. important::
    Do not use ``git rebase`` to upgrade your branch to the latest release. This
    rewrites the history of the branch and makes it impossible for suites to
    include your changes at a previous release.

.. admonition:: Tagging

    Tagging gives a human-readable label to a specific commit. You are free
    to apply whatever tags you wish within your fork of a repository.

    .. code-block::

        git tag -a <label name> -m <message> <commit hash>

    * If no commit hash is included then the latest commit will be tagged.
    * If tagging a branch for use with a specific revision we recommend the format
      ``vnX.Y_branch_name``.
    * Including a message with further details is optional
    * ``-f`` can be included to move an existing tag to a new location

    ``git push`` does not, by default, push tags. To push a tag to your
    repository use

    .. code-block::

        git push origin tag <tag_name>


.. _updating_branch:

Updating Branches
-----------------

It will often be necessary to merge in changes from a remote repository into
your local branch, eg. when updating your branch to a new release, or when
merging in ``main`` to resolve conflicts. This can be done by,

.. tab-set::

  .. tab-item:: Web Browser

    .. tip::

      This is only applicable when updating a branch with ``main`` in an open
      PR. For other uses, such as updating an old branch to a new release, see
      the next tabs.

    Navigate to the pull request page and locate the branch status box. This is
    towards the bottom of the conversation. Here, you can select the button to
    update the branch. If merge conflicts exist, it will take you to a page
    where these can be fixed.

    .. image:: images/gh_screenshots/update_branch_light.png
      :class: only-light border

    .. image:: images/gh_screenshots/update_branch_dark.png
      :class: only-dark border

  .. tab-item:: git commands (from fork)

    .. tip::

      This section gets the changes via your remote fork. You will first update
      your fork with changes from the upstream repository, then merge the
      updated ``main`` or ``stable`` to your
      development branch. This results in changes to the fork ``main`` or ``stable``
      and so is generally recommended. However, sometimes you may want to
      skip this, so the next tab would has been provided as an alternative.

    Navigate to your clone and ensure that the branch you wish to update is your
    active branch,

    .. code-block:: shell

      cd /path/to/clone
      git switch <desired-branch>

    Ensure that your fork is up to date with the upstream repository. See
    :ref:`syncing your fork <syncing_fork>` for details on how to do this.

    Then ensure that knowledge of any synced changes is available in your
    local clone,

    .. code-block:: shell

      git fetch origin

    Now you can merge the synced branch into your development branch,

    .. code-block:: shell

      git merge origin/<branch>

    If there are any merge conflicts you can now fix these using your conflict
    tool of choice.

  .. tab-item:: git commands (from upstream)

    .. tip::

      This section gets the changes from the upstream repository, and merges
      these directly onto your branch. It will **not** update ``main`` or ``stable``
      in your fork.

    Navigate to your clone and ensure that the branch you wish to update is your
    active branch,

    .. code-block:: shell

      cd /path/to/clone
      git switch <desired-branch>

    Ensure that the upstream repository is available as a remote source. See
    :ref:`setting git remote sources <git_remote>` for more details.

    Then fetch the upstream repository and merge in the desired branch,

    .. code-block:: shell

      git fetch upstream
      git merge upstream/<branch>

    If there are any merge conflicts you can now fix these using your conflict
    tool of choice.

