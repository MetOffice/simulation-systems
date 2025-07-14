.. _gh_dev_init:

Beginning a Github Development
==============================

This section will guide you through the development process assuming you are already authorised with github (:ref:`gh_authorisation`) and have already created a fork (:ref:`forking`).

Create an Issue
---------------

.. important::

    It is not guaranteed that opening an Issue will result in action or even visibility by the relevant maintainers or code owners. If you think a team or individual should be aware of an issue, then contact them directly in addition to opening an Issue.

An Issue in github can be used to document a problem in the codebase or as somewhere to document the development process for a new feature. Sub-Issues can also be created if a large piece of work wants breaking down into smaller sections. If you are working on an Issue, then assign yourself to it so that others know that you are working on it. Issues are created in the Upstream repository.

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
--------------------

A clone is a local copy of a repository - you can have a local clone of either an upstream repository or a fork. A clone will have an active branch which will initially be the default branch of the repository upon merging. All other branches in the repository can be accessed using the ``checkout`` command (see below). For general development, you should now get a clone of your fork.

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
---------------

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



