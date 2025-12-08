.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _branch_migration:

Migrating a branch from fcm to git
==================================

.. important::

    If migrating an old trac ticket, please make sure to,

    * Cross-link between both the trac ticket and github PR/Issue
    * Add a ``git_migration:#NNN`` keyword to the trac ticket to avoid duplicate
      migrated tickets

This page is intended to act as a guide when migrating branches from fcm to git
after the initial git release. It assumes that you have already :ref:`created
a fork <forking>` of the repo you are migrating to.

.. important::

    The process below involves rsyncing the changes in your fcm working copy to
    a git clone. This requires that the two branches have equivalent branch
    points, so ensure this is the case.

    For convenience, the ``git_migration`` tag is provided as a branch point in
    both fcm and git. However all ``fcm`` revisions and tags have a direct
    equivalent commit on git - tags will have the same name on both, revisions
    of specific commits will need to be manually aligned with a commit hash by
    comparing commit messages.

#. Optionally, create a new branch in ``fcm`` using the tag ``git_migration``.
   Then merge your development branch onto this one, eg.

   .. code-block::

     fcm bc --type=dev branch_for_migration fcm:lfric_apps.x_tr@git_migration
     ...
     fcm merge fcm:lfric_apps.x_br/dev/USER/BRANCH

   Resolve any conflicts and then commit these changes to this branch,
   ``fcm ci``.

   For Jules users, upgrading to the ``git_migration`` tag is required.

#. Move into your git clone and :ref:`create a new branch <create_branch>` with
   the same start point as your fcm branch. If you are branching from an
   untagged revision, you will need to manually find the relevant hash for that
   commit from the git log by comparing commit messages.

   .. code-block::

     git switch -c <branch name> <tag/hash to branch from>
     e.g. git switch -c new_migrated_branch git_migration

   If the ``git_migration`` tag doesn't exist in your clone, then you may need
   to :ref:`sync tags <sync_fork_tags>`.

#. Rsync the changes over from the fcm working copy to the git clone. Use
   ``--delete`` to remove any files you have deleted in your branch. Use
   ``--exclude=.git --exclude=.svn`` so that the version control directories
   aren't modified.

   .. code-block::

     # NOTE: You need the trailing backslash on the fcm source path
     rsync -av --delete --exclude=.git --exclude=.svn path/to/fcm/working/copy/ path/to/git/clone

#. Check carefully the output of the rsync via ``git status``. If you have new
   files on your branch these will need adding via ``git add``.
#. Finally, all branches will **need** to update to the initial git release in
   order to run the test suites. This can be done by merging the ``stable``
   branch into your new branch. See :ref:`updating a branch <updating_branch>`
   for more details, noting that you will need to use one of the options
   using ``git commands`` for this step.

   If you have a linked ticket you will manually need to :ref:`update the
   dependencies.yaml <multi-repo_testing>` to point at your linked branches. For
   lfric_apps branches, ensure that the ``dependencies.sh`` file hasn't been
   readded to the branch.
#. It may be worth running the :ref:`test suite <testing>` to ensure the branch
   has been properly migrated.

.. tip::

    There will be significant changes to the rose-stem test suites between the
    ``git_migration`` point and the initial git release. Therefore, conflicts
    are expected when updating rose-stem changes to the initial release. The UM,
    Jules and UKCA test suites have all had file extensions renamed from ``.rc``
    to ``.cylc``.

    For lfric_core a minor source code change has been added to github, which
    may result in conflicts in ``components/lfric-xios/source/lfric_xios_file_mod.f90``
