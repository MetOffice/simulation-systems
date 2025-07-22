.. _gh_dev_init:

Beginning a Github Development
==============================

This section will guide you through the development process assuming you are already authorised with github (:ref:`gh_authorisation`) and have already created a fork (:ref:`forking`).

Create an Issue
---------------

.. important::

    It is not guaranteed that opening an issue will result in action or even visibility by the relevant maintainers or code owners. If you think a team or individual should be aware of an issue, then contact them directly in addition to opening an issue.

An issue in github can be used to document a problem in the codebase or as somewhere to document the development process for a new feature. Sub-issues can also be created if a large piece of work wants breaking down into smaller sections. If you are working on an issue, then assign yourself to it so that others know that you are working on it. Issues are created in the upstream repository.

.. tab-set::

    .. tab-item:: Web Browser

        Navigate to the ``Issues`` tab for the relevant **upstream** repo and select the ``New Issue``. Write an suitable title and description, and use the options on the right as desired/appropriate.

        .. image:: images/gh_screenshots/issues_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/issues_dark.png
            :class: only-dark border

    .. tab-item:: gh cli

        The following command can be used to create an issue from the command line. The available options can be seen in the `gh cli documentation <https://cli.github.com/manual/gh_issue_create>`_.

        .. code-block::

            gh issue create -R <OWNER>/<REPO> [options]

There is no requirement to open an issue before making a pull request, as long as the change documentation is sufficient. For instance, small changes may not benefit from the separate issue.

.. _clone_repo:

Clone the Repository
--------------------

A clone is a local copy of a repository - you can have a local clone of either an upstream repository or a fork. A clone will have an active branch which will initially be the default branch of the repository. All other branches in the repository can be accessed using the ``checkout`` command (see below). For general development, you should now get a clone of your fork.

.. tip::

    For those familiar with svn/fcm, a clone is the git equivalent to a working copy. However, unlike a working copy, which can only access a single branch, a clone can be switched to any branch in the repository.

.. tab-set::

    .. tab-item:: gh cli

        To clone a repository using gh cli run the following command,

        .. code-block::

            gh repo clone <OWNER>/<REPO> <CLONE_NAME>

        where ``CLONE_NAME`` is the desired directory name of the clone. It will default to the name of the repository.

        .. tip::

            Using gh cli to clone a fork will automatically add the upstream repository as a remote source which can be helpful.

    .. tab-item:: git commands

        To clone a repository using git, run the following in a terminal:

        .. code-block::

            git clone <URL> <CLONE_NAME>

        where ``CLONE_NAME`` is the desired directory name of the clone. It will default to the name of the repository.

        The ``URL`` can be found from github,

        .. image:: images/gh_screenshots/clone_button_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/clone_button_dark.png
            :class: only-dark border

        selecting the url as desired.


Create a Branch
---------------

Branches for developing Simulation Systems repositories should generally be branched from ``stable`` where this exists (some smaller repositories only contain a ``main`` branch). Creating a branch from ``main`` may be acceptable if the development is continuing on from a ticket already committed at that release.

To create a branch and switch to it from the command line, the syntax is,

.. tab-set::

    .. tab-item:: Web Browser

        Navigate to the github repository where you would like to create a
        branch. You will need ``write`` permission for that repository in order
        to create the branch.

        Choose to view all branches in the repository,

        .. image:: images/gh_screenshots/all_branches_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/all_branches_dark.png
            :class: only-dark border

        then select the new branch button,

        .. image:: images/gh_screenshots/new_branch_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/new_branch_dark.png
            :class: only-dark border

        Finally, name your branch and select the source branch as desired.

    .. tab-item:: git commands

        .. code-block::

            git branch <branch_name> <source_branch>
            git checkout <branch_name>

            # or

            git checkout <source_branch>
            git checkout -b <branch_name>


Developing a Change
-------------------

Now that you have a new branch, you are ready to begin development. See :ref:`development_index`, for advice on how to plan and implement new developments in a Simulation Systems repository, including advice on Metadata, KGO's and testing.

.. tip::

    To see the status of your current clone you can run ``git status``

While developing you will likely want to commit your changes and push to the remote repository. First you will need to stage any files that have been modified and you would like to include in your commit,

.. code-block::

    git add path/to/file1 [path/to/file2...]

And then commit the change,

.. code-block::

    git commit -m "An Informative Commit Message"

.. tip::

    In git you do not need to commit all modified files unlike in svn/fcm. It is also possible to only commit certain parts of a modified file. For more information see the relevant man page, ``man git add``.

Finally, you may want to push any commits stored in your local clone.

.. code-block::

    git push

.. important::

    Unlike svn/fcm, committing in git will not push your changes to the remote server. The ``git push`` command must also be used to do this.

.. _git_remote:

Setting Remote Sources in git
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When cloning a repository git will automatically set the source URL as a remote
source with the default name of ``origin``. To list the remote sources currently
configured for a clone, run ``git remote -v``. For example, cloning the
repository containing these working practices via ssh will produce the output,

.. code-block::

    $ git remote -v
    origin	git@github.com:MetOffice/simulation-systems.git (fetch)
    origin	git@github.com:MetOffice/simulation-systems.git (push)

It is possible to set another repository as a remote source using the syntax,

.. code-block::

    git remote add <name> <url>

The URL for the upstream can be found from the Code button on github (see
:ref:`Cloning a Repository <clone_repo>`).

.. tip::

    :ref:`Cloning <clone_repo>` a repository with the gh cli will automatically
    set the upstream repository as remote named ``upstream``.

A common use case for this would be to add the upstream repository as a remote
source in order to merge the ``main`` branch into your development branch. For
example, in a clone of a fork of these working practices,

.. code-block::

    $ git remote add upstream git@github.com:MetOffice/simulation-systems.git
    $ git remote -v
    origin	git@github.com:userName/simulation-systems.git (fetch)
    origin	git@github.com:userName/simulation-systems.git (push)
    upstream	git@github.com:MetOffice/simulation-systems.git (fetch)
    upstream	git@github.com:MetOffice/simulation-systems.git (push)

You will need to manually sync the fork with the remote source by fetching it
with the command ``git fetch <name>``, eg.

.. code-block::

    git fetch upstream

To interact with remote branches you can use the ``<name>/<branch>`` syntax. For
example, to merge the upstream main into the current branch, use,

.. code-block::

    git merge upstream/main

