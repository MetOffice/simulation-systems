.. _forking:

Creating and Managing Forks
===========================

.. tip::

    For more information see the `github documentation
    <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks>`__

Forks are repositories that share code and visibility settings with the
upstream repository. They provide a place for development work to take place
while allowing the upstream repo to maintain limited write access. Forks can
all merge branches with each other as well as with the upstream repository,
meaning a pull request can be opened to merge a branch in a fork into the
upstream main.

Creating a Fork
---------------

Creating a fork is something that only needs to be done once per upstream
repository. Once created, branches can be created in the fork as desired by
the owner.

.. tab-set::

    .. tab-item:: Web Browser

        First navigate to the upstream repository you wish to fork. Then select
        the fork button.

        .. image:: images/gh_screenshots/fork_button_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/fork_button_dark.png
            :class: only-dark border

        On the next page you can rename your fork if desired and select which
        branches to fork - ensure this box is unticked to fork all branches.

        .. important::

            Ensure the option to only clone the default branch is unticked.

        .. image:: images/gh_screenshots/fork_page_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/fork_page_dark.png
            :class: only-dark border

    .. tab-item:: gh cli

        Run the following command, substituting for the required upstream owner
        and repository name,

        .. code-block:: shell

            gh repo fork <OWNER>/<REPO>

        .. tip::

            Add ``--clone`` to immediately clone the forked repo


Maintaining a Fork
------------------

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

        Navigate to your fork in github that you wish to sync. Select the
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

        Run the following command, substituting for the downstream fork owner
        and repo name. Without the ``-b`` option, only the default branch will
        be synced. You may want to sync both ``stable`` and ``main``,
        particularly at a release.

        .. code-block:: shell

            gh repo sync <OWNER>/<REPO> -b <BRANCH>

        The synced branch will still only exist in the remote repository. If
        you require them in a local clone make sure to ``fetch`` or ``pull``
        the repository.

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

