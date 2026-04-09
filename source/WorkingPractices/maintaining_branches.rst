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

Upgrading to a release and maintaining old version branches
-----------------------------------------------------------

A common working style for scientific development is to maintain the changes at
multiple different versions, to aid scientific testing. In this case we
recommend working from a main development branch, that is up to date with the
latest release. Branches for previous versions can be created from this
development branch as required. We also recommend using :ref:`tags <tags>` as a
way of providing human-readable labels to individual commits.

Below is a diagram demonstrating this suggested way of working.

.. mermaid::

  ---
  config:
    theme: neutral
    themeVariables: {lineColor: '#58a6ff', fontSize: 10px}
  ---

  flowchart TB
    classDef dev_branch fill:#8eb6e8,stroke:#5bc0de,stroke-width:2px,color:#000
    classDef tag fill:#a8ffcf,stroke:#57ffa2,stroke-width:2px,color:#000
    classDef vn_branch fill:#ffde91,stroke:#fcc43f,stroke-width:2px,color:#000


    create_dev[Create a Development Branch<br>*new_feature_branch*]:::dev_branch
    tag_xy{{Tag Branch Before Upgrading<br>*tagX.Y_feature_branch*}}:::tag
    upgrade_xy1[Upgrade to vnX.Y+1<br>*new_feature_branch*]:::dev_branch
    branch_xy[Create vnX.Y Development Branch<br>*vnX.Y_feature_branch*]:::vn_branch
    develop_xy[Further Develop Changes at vnX.Y<br>*vnX.Y_feature_branch*]:::vn_branch
    tag_xy1{{Tag Branch Before Upgrading<br>*tagX.Y+1_feature_branch*}}:::tag
    retag_xy1{{Update tag to include further changes<br>*tagX.Y+1_feature_branch*}}:::tag
    upgrade_xy2[Upgrade to vnX.Y+2<br>*new_feature_branch*]:::dev_branch
    branch_xy1[Create vnX.Y+1 Development Branch<br>*vnX.Y+1_feature_branch*]:::vn_branch
    develop_xy1[Further Develop Changes at vnX.Y+1<br>*vnX.Y+1_feature_branch*]:::vn_branch


    subgraph vnX.Y["<span style='display:block; width:100%; text-align:left; white-space: nowrap; font-size:15px; font-weight:100; color:#000000;'><i>vnX.Y Steps</i></span>"]
      create_dev -->|Development Changes| tag_xy
      tag_xy --> branch_xy --> develop_xy
    end

    subgraph vnX.Y+1["<span style='display:block; width:100%; text-align:left; white-space: nowrap; font-size:15px; font-weight:100; color:#000000;'><i>vnX.Y+1 Steps</i></span>"]
      tag_xy --> upgrade_xy1 -->|Development Changes| tag_xy1
      tag_xy1 --> branch_xy1 --> develop_xy1 --> retag_xy1
      tag_xy1 --> retag_xy1
    end

    subgraph vnX.Y+2["<span style='display:block; width:100%; text-align:left; white-space: nowrap; font-size:15px; font-weight:100; color:#000000;'><i>vnX.Y+2 Steps</i></span>"]
      tag_xy1 --> upgrade_xy2
    end

    subgraph legend[" "]
      direction TB
      dev_box[Development Branch]:::dev_branch
      vn_box[Versioned Branch]:::vn_branch
      tag_box{{Tag Creation}}:::tag
    end

* Create a development branch and develop your new feature on this branch. This
  branch will be upgraded to newer versions when required and will be submitted
  via a Pull Request.
* When ready to upgrade to a newer version:

  * Create a tag before updating the branch. This allows easy identification of
    the pre-updated branch, without needing to read the git log to find the
    particular commit. It can be used as the ``ref`` value in
    ``dependencies.yaml`` files in rose-stem and standalone suites. See below
    for advice about creating tags.

    To aid readability of different refs, we recommend following the naming
    scheme ``tagX.Y_dev_branch_name`` where ``X.Y`` is substituted for the
    release this tag represents.
  * If further development at the previous version is likely, then a version
    branch can be created based off the new tag,
    ``git switch -c vnX.Y_dev_branch_name tagX.Y_dev_branch_name`` where
    ``vnX.Y`` represents that this is now a version branch. As changes are made
    to this branch, the associated version tag can be safely updated to point at
    the latest commits.
  * The main development branch can now be updated to the newest version. This
    can be done by running ``git merge stable``, having first ensured the
    ``stable`` branch in the fork is up to date with the upstream repository.
    More details on this process can be seen :ref:`below <updating_branch>`.

* This process can be repeated across multiple version upgrades, creating tags
  and branches for old versions as desired.

We recommend this process of maintaining a single development branch which moves
to new releases as the source branch of Pull Requests cannot be changed.
Therefore, if the Pull Request spans multiple releases, it doesn't need to be
closed and a new one opened as new branches are created.

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
      ``tagX.Y_branch_name``.
    * Including a message with further details is optional
    * ``-f`` can be included to move an existing tag to a new commit.

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

