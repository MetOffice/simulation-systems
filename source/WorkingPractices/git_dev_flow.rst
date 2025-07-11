.. _git_dev_flow:

Simulation Systems Github Development Flow
==========================================

.. note::

    In the following Working Practices, we will endeavour to provide options for using the Github Web Interface and the ``gh`` cli where possible. Further information will be available in the github documentation.

    To get started with the ``gh`` cli, see the `gh quickstart guide <https://docs.github.com/en/github-cli/github-cli/quickstart>`_

Overview
--------

Simulation Systems github repositories are setup with at least 2 protected branches, ``stable`` and ``main`` (with the potential for additional version branches to be added).

* ``stable`` - This branch is the default github branch and generally remains unchanged throughout a release cycle. It is the stable point from which new branches should be cut. Only new releases and small hotfixes to a release will be merged back into this branch.
* ``main`` - This branch is where new development PR's will be merged. It will never be behind the ``stable`` branch, but will regularly be ahead. All PRs should be set to target this branch (more on this later) and a CI check will fail if it isn't. When merge conflicts need fixing for commit, this is the branch that should be merged into the development branch.

All general development for Simulation Systems Github repos will take place on forks of that repo. It is the responsibility of the developer to maintain their own fork. See below for advice on forking.

The development cycle can be seen below. ``Upstream`` (blue) refers to parent repository, owned by the MetOffice github organisation. ``Downstream`` (grey) refers to the forked repository, owned by the developer.


.. image:: images/git-dev-strategy.svg
    :class: dark-light


Creating and Managing Forks
---------------------------

.. tip::

    For more information see the `github documentation <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks>`_

Forks are repositories that share code and visibility settings with the upstream repository. They provide a place for development work to take place while allowing the upstream repo to maintain limited write access. Downstream forks can all merge branches with each other as well as with the upstream repository, meaning a PR can be opened to merge a downstream branch into the upstream main.

Creating a Fork
^^^^^^^^^^^^^^^

Creating a fork is something that only needs to be done once per upstream repository. Once created, branches can be created in the fork as desired by the owner.

.. tab-set::

    .. tab-item:: Web Browser

        First navigate to the upstream repository you wish to fork. Then select the fork button.

        .. image:: images/gh_screenshots/fork_button_light.png
            :class: only-light

        .. image:: images/gh_screenshots/fork_button_dark.png
            :class: only-dark

        On the next page you can rename your fork if desired and select which branches to fork - ensure this box is unticked to fork all branches.

        .. important::

            Ensure the option to only clone the default branch is unticked.

        .. image:: images/gh_screenshots/fork_page_light.png
            :class: only-light

        .. image:: images/gh_screenshots/fork_page_dark.png
            :class: only-dark

    .. tab-item:: gh cli

        Run the following command, substituting for the required upstream owner and repository name,

        .. code-block::

            gh repo fork <OWNER>/<REPO>

        .. tip::

            Add ``--clone`` to immediately clone the forked repo


Maintaining a Fork
^^^^^^^^^^^^^^^^^^

Most work to maintain a fork involves syncing it with the upstream repository.

.. tab-set::

    .. tab-item:: Web Browser

        Navigate to your fork in github that you wish to sync. Select the ``Sync Fork`` button and if required, update the branch. This will only sync the branch you are currently on - to sync other branches select one from the branch dropdown menu. You may want to sync both ``stable`` and ``main``, particularly at a release.

        .. image:: images/gh_screenshots/sync_fork_light.png
            :class: only-light

        .. image:: images/gh_screenshots/sync_fork_dark.png
            :class: only-dark

    .. tab-item:: gh cli

        Run the following command, substituting for the downstream fork owner and repo name. Without the ``-b`` option, only the default branch will be synced. You may want to sync both ``stable`` and ``main``, particularly at a release.

        .. code-block::

            gh repo sync <OWNER>/<REPO> -b <BRANCH>

        .. tip::

            When using the gh cli to sync forks, remember that it won't pull the changes to local clone, this needs to be done manually.

It is recommended that developers do not modify the synced branches from upstream in their forks as this may cause issues with merge conflicts when syncing a fork. Instead all work should be carried out in a branch.


Development Workflow
--------------------

This section will guide you through the development process having already created a fork.

Create an Issue
^^^^^^^^^^^^^^^

.. important::

    It is not guaranteed that opening an Issue will result in action or even visibility by the relevant maintainers or code owners. If you think a team or individual should be aware of an issue, then contact them directly in addition to opening an Issue.

An Issue in github can be used to document a problem in the codebase or as somewhere to document the development process for a new feature. Sub-Issues can also be created if a large piece of work wants breaking down into smaller sections. If you are working on an Issue, then assign yourself to it so that others know that you are working on it.

.. tab-set::

    .. tab-item:: Web Browser

        Navigate to the Issues tab for the relevant **upstream** repo and select the ``New Issue``. Write an suitable title and description, and use the options on the right as desired/appropriate.

        .. image:: images/gh_screenshots/issues_light.png
            :class: only-light

        .. image:: images/gh_screenshots/issues_dark.png
            :class: only-dark

    .. tab-item:: gh cli

        The following command can be used to create an issue from the command line. The available options can be seen in the `gh cli documentation <https://cli.github.com/manual/gh_issue_create>`_.

        .. code-block::

            gh issue create -R <OWNER>/<REPO> [options]

There is no requirement to open an issue before making a pull request, as long as the change documentation is sufficient. For instance, small changes may not benefit from the separate issue.


Clone the Repository
^^^^^^^^^^^^^^^^^^^^

A clone is a local copy of a repository - you can have a local clone of either an upstream repository or a fork. A clone will have an active branch which will initially be the default branch of the repository upon merging. All other branches in the repository can be accessed using the ``checkout`` command (see below).

.. tip::

    For those familiar with svn/fcm, a clone is the git equivalent to a working copy. However, unlike a working copy, which can only access a single branch, a clone can be switched to any branch in the repository.

.. tab-set::

    .. tab-item:: git commands

        To clone a repository using git, run the following in a terminal:

        .. code-block::

            git clone <URL> <CLONE_NAME>

        where ``CLONE_NAME`` is the desired directory name of the clone. It will default to the name of the repository.

        The ``URL`` can be found from github,

        .. image:: images/gh_screenshots/clone_button_light.png
            :class: only-light

        .. image:: images/gh_screenshots/clone_button_dark.png
            :class: only-dark

        selecting the url as desired.

    .. tab-item:: gh cli

        To clone a repository using gh cli run the following command,

        .. code-block::

            gh repo clone <OWNER>/<REPO> <CLONE_NAME>

        where ``CLONE_NAME`` is the desired directory name of the clone. It will default to the name of the repository.

        .. tip::

            Using gh cli to clone a fork will automatically add the upstream repository as a remote source which can be helpful.


Create a Branch
^^^^^^^^^^^^^^^

Branches for developing Simulation Systems repositories should generally be branched from ``stable`` where this exists (some smaller repositories only contain a ``main`` branch). Creating a branch from ``main`` may be acceptable if the development is continuing on from a ticket already committed at that release.

To create a branch and switch to it from the command line, the syntax is,

.. code-block::

    git branch <branch_name> <parent_branch>
    git checkout <branch_name>

    # or

    git checkout <parent_branch>
    git checkout -b <branch_name>

.. note::

    It is also possible to create a new branch via github in a web browser.


Developing a Change
^^^^^^^^^^^^^^^^^^^





