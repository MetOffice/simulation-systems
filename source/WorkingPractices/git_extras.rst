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
