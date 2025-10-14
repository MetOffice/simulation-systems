.. _branch_migration:

Migrating a branch from fcm to git
==================================

This page is intended to act as a guide when migrating branches from fcm to git
after the initial git release. It assumes that you have already :ref:`created
a fork <forking>` and you have an active :ref:`branch <create_branch>` to
migrate to.

.. important::

    This process involves merging the development branch up to the migration
    point in the fcm repository, denoted by the tag ``git_migration``. The
    source code in each is unchanged, however there are some changes in each
    repository which may cause clashes.

    In particular the rose-stem suites have all undergone significant changes
    which will likely cause clashes. If referencing a linked branch, this is
    done in the new :ref:`dependencies.yaml <multi-repo_testing>` file,
    replacing the old references in the ``dependencies.sh`` or
    ``rose-suite.conf`` files.

    For UM, Jules and UKCA, all rose-stem files have been renamed with a
    ``.cylc`` instead of ``.rc``.

* Firstly, create a new branch in ``fcm`` using the tag ``git_migration``. Then
  merge your development branch onto this one, eg.
  ``fcm merge fcm:um.x_br/dev/USER/BRANCH``. Resolve any conflicts and then
  commit these changes to this branch, ``fcm ci``.
* Create a patch file from your new branch at the migration point,

  .. code-block::

    fcm bdiff >> /path/to/repo_diff.patch

* Move into your git clone and ensure that the new git branch is active. Then
  apply your new patch,

  .. code-block::

    git apply --reject /path/to/repo_diff.patch

* This will apply all patches that do not conflict. If there are conflicts then
  these will be recorded in ``*.rej`` files. The output of the ``apply`` command
  will note any failures, or you can find them by running
  ``find . -name *.rej``. Fix any failures you find and then commit the changes.
* It may be worth running the :ref:`test suite <testing>` to ensure the branch
  has been properly migrated.

.. tip::

    It is recommended that the fcm branch to migrate is brought up to the
    ``git_migration`` tag, and the git branch is at the initial release. This
    will keep any merge conflicts to a minimum. However the process will work
    with different versions.

.. note::

    The migration of simulation system repositories has been completed using the
    internal MetOffice `gitlify tool <https://github.com/MetOffice/gitlify>`_.
    This can migrate the history of branches which might be of interest to some
    developers.
