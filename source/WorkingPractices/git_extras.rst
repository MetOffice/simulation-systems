.. _git_extras:

Extra Git Working Practices
===========================

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

The URL for the desired repository can be found from the Code button on github
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

    Then ensure that any synced changes are available in your local clone,

    .. code-block:: shell

      git fetch origin

    Now you can merge the synced branch into your development branch,

    .. code-block:: shell

      git merge <branch>

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
