.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _maintaining_forks:

Maintaining Forks
=================

.. _git_remote:

Setting Remote Sources in git
-----------------------------

When cloning a repository git will automatically set the source URL as a remote
source with the default name of ``origin``. To list the remote sources
currently configured for a clone, run ``git remote -v``. For example, cloning
the repository containing these working practices via ssh will produce the
output,

.. code-block:: shell

    git remote -v

    # origin    git@github.com:MetOffice/simulation-systems.git (fetch)
    # origin    git@github.com:MetOffice/simulation-systems.git (push)

It is possible to set another repository as a remote source using the syntax,

.. code-block:: shell

    git remote add <name> <url>

The URL for the desired repository can be found from the Code button on GitHub
(see :ref:`Cloning a Repository <clone_repo>`).

.. tip::

    :ref:`Cloning <clone_repo>` a repository with the gh cli will automatically
    set the upstream repository as remote named ``upstream``.

A common use case for this would be to add the upstream repository as a remote
source in order to merge the ``main`` branch into your development branch. For
example, in a clone of a fork of these working practices,

.. code-block:: shell

    git remote add upstream git@github.com:MetOffice/simulation-systems.git
    git remote -v

    # origin    git@github.com:userName/simulation-systems.git (fetch)
    # origin    git@github.com:userName/simulation-systems.git (push)
    # upstream  git@github.com:MetOffice/simulation-systems.git (fetch)
    # upstream  git@github.com:MetOffice/simulation-systems.git (push)

You will need to manually sync the fork with the remote source by fetching it
with the command ``git fetch <name>``, eg.

.. code-block:: shell

    git fetch upstream

To interact with remote branches you can use the ``<name>/<branch>`` syntax.
For example, to merge the upstream main into the current branch, use,

.. code-block:: shell

    git merge upstream/main

.. _syncing_fork:

Syncing a Fork
--------------

Most work to maintain a fork involves syncing it with the upstream repository.
Syncing a fork will ensure that changes to the upstream repository are copied
into the fork. Syncing is done on a per branch basis. For example, after a new
release, syncing the ``stable`` branch will ensure the forks ``stable`` branch
contains the newly released code.

.. important::

    It is recommended that developers do not modify the synced branches from
    upstream in their forks as this may cause issues with merge conflicts when
    syncing a fork. Instead all work should be carried out in a branch.

.. tab-set::

    .. tab-item:: Web Browser

        Navigate to your fork in GitHub that you wish to sync. Select the
        ``Sync Fork`` button and if required, update the branch. This will
        only sync the branch you are currently on - to sync other branches
        select one from the branch dropdown menu. You may want to sync both
        ``stable`` and ``main``, particularly at a release.

        .. image:: images/gh_screenshots/sync_fork_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/sync_fork_dark.png
            :class: only-dark border

        The synced branch will still only exist in the remote repository. If
        you require them in a local clone make sure to ``fetch`` or ``pull``
        the repository.

    .. tab-item:: gh cli

        .. code-block:: shell

            gh repo sync [<owner>/<repo>] [-b <branch>]

        * The command syncs changes from a remote repository to your fork or
          local copy.
        * Both ``<owner>/<repo>`` and ``-b <branch>`` are optional.
        * If ``-b <branch>`` isn't specified, it will sync the default branch
          (main),
        * There is no built-in ``gh repo sync`` option for all branches,
          therefore the user needs to specify a branch name when not syncing the
          not the default branch.
        * If you run this without ``<owner>/<repo>``, it will sync changes from
          the remote origin to your local clone.

          * Doing this will not update your remote fork, this will also require
            a ``git push`` command.

        * By providing your username and fork name to ``<owner>/<repo>``, it
          will sync changes from the upstream parent repository into your remote
          fork.

          * Doing this will not update your local clone, this will also require
            a ``git pull`` command for each branch you wish to update.

    .. tab-item:: git commands

        Ensure that the upstream repository is available as a remote source and
        the latest changes have been fetched. See :ref:`setting git remote
        sources <git_remote>` for more details.

        Then run the following commands for each branch you wish to sync. The
        example below will use ``main``.

        .. code-block:: shell

            # Change to the desired branch
            git switch main

            # Merge in changes from the upstream
            git merge upstream/main

            # Push the changes back to the remote fork
            git push

.. tip::

    Note that the options above will result in the synced branch being available
    in different locations. Using the web browser will not update your
    local clone while using ``git`` commands will not update the remote
    repository without pushing. ``gh`` can be used to update either.

.. _sync_fork_tags:

Syncing Fork Tags
-----------------

If you wish to sync tags to your fork, this requires using git commands. Ensure
that the upstream repository is set as a :ref:`remote source <git_remote>`. Then
run the following,

.. code-block::

    git fetch --tags upstream
    git push --tags

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
