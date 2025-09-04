.. _pull_requests:

Pull Requests
=============

Once you are happy with your development and the :ref:`test suites <testing>`
pass then you are ready to pass your ticket to review. Reviews in github are
done through pull requests.

Opening a Pull Request
----------------------

The first step to the begin the review process in github is to open a pull
request. A pull request shows the proposed changes to the target branch and
provides a space for reviews and discussion to take place. There a number of
ways of opening a pull request. If your branch has had recent changes, then a
box may appear in the either of the Upstream or Fork github pages, with a button
to ``Compare & pull request``.

Alternatively, navigate to the github page of your fork and select the
``Contribute`` button,

.. image:: images/gh_screenshots/contribute_light.png
    :class: only-light border

.. image:: images/gh_screenshots/contribute_dark.png
    :class: only-dark border

The resulting page will allow you to create a pull request. The first thing to
check are the target and source branches for the pull requests.

.. image:: images/gh_screenshots/branch_pr_light.png
    :class: only-light border

.. image:: images/gh_screenshots/branch_pr_dark.png
    :class: only-dark border

You have 4 options to consider.

* ``base repository`` - This is the repository where the pull request will be
  merged into. It will be the upstream repository you forked from.
* ``base`` - This is the branch in the ``base repository`` where the pull
  request will be merged into. It will default to the repositories default
  branch which for Simulation Systems repositories will be ``main`` which is as desired.
* ``head repository`` - This is the repository where the pull request changes
  are coming from - it will be your forked repository.
* ``compare`` - This is the branch in the ``head repository`` containing
  proposed changes. It will be the branch you switched to above, but this can be
  changed now. It is **not** possible to edit this once the pull request has
  been opened, so make sure it is correct now.

.. important::

    Make sure the base and compare branches are correct.

Fill out the rest of the pull request by giving an appropriate title and
supplying a description. The description box will contain a pull request
template to fill out - this can be completed now, or edited later before passing to review.

Finally, ensure that the option to allow edits by maintainers
is selected (see :ref:`reviewer_edits` for details).

.. image:: images/gh_screenshots/maintainer_edit_light.png
    :class: only-light border

.. image:: images/gh_screenshots/maintainer_edit_dark.png
    :class: only-dark border

Once you are happy with the pull request details open the pull request.
Initially you can choose to do this in draft mode, to allow you time to do any
final fixes based on continuous integration. If you use draft mode mark the pull request as ``ready for review`` once you are satisfied.

.. tip::

    It is possible to `link your pull request with an issue
    <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>`_

Continuous Integration
----------------------

Once the pull request has been opened, any changes to either it or the source
branch will trigger continuous integration (CI). CI is a way of running tests on
the changes proposed by the pull request. Due to resource constraints, these
tests are constrained in their size and usually target items such as code
styling.

.. important::

    CI tests will not run any atmosphere or integration models of simulation
    system code as these are too computationally expensive. These tests are run
    as part of the :ref:`rose-stem suites <testing>`. Some of the tests run by
    the continuous integration are also run as part of the rose-stem suites.

Continuous Integration is reported on towards the bottom of the pull request
conversation. In the example below, all CI tests have passed. If you encounter
failures, then you can click on the failing job to find the log messages.
Certain CI tests are required to pass in order for the branch to be mergeable,
for example the ``WIP`` test below which is marked with a ``required`` label.
Even if CI tests are not marked as required, the pull request will likely be
rejected with failing tests.

.. image:: images/gh_screenshots/ci_light.png
    :class: only-light border

.. image:: images/gh_screenshots/ci_dark.png
    :class: only-dark border

.. _updating_branch:

Updating a branch
-----------------

Most development work in simulation-systems repositories will take place on a
branch created from ``stable``. Therefore it will need to be updated to match
the latest changes from ``main`` when a pull request is open. Github provides
functionality to do this in the browser, with the ability to fix merge
conflicts. Alternatively, you can do this from a terminal using git.

.. important::

    In order to aid the development of scientific suites, the majority of
    development should be done on a branch from ``stable`` without merging in
    changes from ``main``. Only when the development has been completed and the
    pull request is almost ready for commit should you merge in ``main``.

.. tab-set::

    .. tab-item:: Web Browser

        Navigate to the pull request page and locate the branch status box. This
        is towards the bottom of the conversation. Here, you can select the
        button to update the branch. If merge conflicts exist, it will take you
        to a page where these can be fixed.

        .. image:: images/gh_screenshots/update_branch_light.png
            :class: only-light border

        .. image:: images/gh_screenshots/update_branch_dark.png
            :class: only-dark border

    .. tab-item:: git commands

        Navigate to your clone and ensure that the branch you wish to update is
        your active branch,

        .. code-block::

            cd /path/to/clone
            git switch <desired-branch>

        Ensure that the upstream repository is available as a remote source.
        See :ref:`setting git remote sources <git_remote>` for more details.

        Then fetch and merge in the upstream main,

        .. code-block::

            git fetch upstream
            git merge upstream/main

        If there are any merge conflicts you can now fix these using your
        conflict tool of choice.


Final Steps
-----------

Ensure that you have found a Sci/Tech reviewer and have had a Code reviewer
assigned. See :ref:`reviews` for how to do this. If your pull request is in
draft mode, you should now change it to active, indicating it is ready for
review.
