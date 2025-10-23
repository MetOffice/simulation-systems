.. _pull_requests:

Pull Requests
=============

Once you are happy with your development and the :ref:`test suites <testing>`
pass then you are ready to pass your ticket to review. Reviews in github are
done through pull requests.

Changes will usually go through a 2-stage review process:

1. SciTech review; carried out by someone that understands the area of code being
   developed
2. Code review; carried out by a member of the Simulation Systems Review Team

Trivial pull requests are an exception and do not require a SciTech review.

:ref:`Linked pull requests <linked>` will move through the review states together.

.. admonition:: Getting Ready for Review

  * If your development changes answers then make sure you have followed the
    steps on :ref:`preparing a KGO pull request for review.<kgo>`

  * Get in touch with your SciTech Reviewer before you feel ready for review.
    They will have valuable insights into the code and, particularly for larger
    changes, may appreciate the opportunity to look at your work as it
    progresses.

  * The review process will iterate between the developer and each reviewer
    until the changes made are agreed to be of sufficient quality. This aims to
    improve the quality of your change, considering a range of scientific and
    technical aspects.The reviewer will fill in their section of the pull
    request template which makes sure all aspects of the ticket are considered.

  * Review suggestions and comments are formed into conversations. The `Resolve
    Conversation` button is used by the reviewer when they are satisfied to
    close that part of the review. The developer should **not** resolve
    conversations themselves.

  * Feedback on code is not a refection of personal ability. All code can be
    improved and reviews are an opportunity for shared learning and collaboration.


Opening a Pull Request
----------------------

The first step to the begin the review process in github is to open a pull
request. A pull request shows the proposed changes to the target branch and
provides a space for reviews and discussion to take place. There a number of
ways of opening a pull request. If your branch has had recent changes, then a
box may appear in the either of the Upstream or Fork github pages, with a
button to ``Compare & pull request``.

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
  branch which for Simulation Systems repositories will be ``main`` which is
  as desired.
* ``head repository`` - This is the repository where the pull request changes
  are coming from - it will be your forked repository.
* ``compare`` - This is the branch in the ``head repository`` containing
  proposed changes. It will be the branch you switched to above, but this can
  be changed now. It is **not** possible to edit this once the pull request
  has been opened, so make sure it is correct now.

.. important::

    Make sure the base and compare branches are correct.

Fill out the rest of the pull request by giving an appropriate title and
supplying a description:

* The title will be used as the commit message and should be therefore be short
  and succinct. It should not contain any issue or pull request numbers.

* The description box will contain a pull request template to fill out
  including details of your change, any approvals needed, documentation
  required and testing performed.

Ensure that the option to allow edits by maintainers box
is selected (see :ref:`reviewer_edits` for details).

.. image:: images/gh_screenshots/maintainer_edit_light.png
    :class: only-light border

.. image:: images/gh_screenshots/maintainer_edit_dark.png
    :class: only-dark border

.. important::

    If an issue exists for the work being completed then you should `link your
    pull request with that issue. <https://docs.github.com/en/issues/
    tracking-your-work-with-issues/using-issues/
    linking-a-pull-request-to-an-issue>`_



Once you are happy with the pull request details open the pull request.
Initially you can choose to do this in draft mode, to allow you time to do any
final fixes based on continuous integration. **If you use draft mode mark the
pull request as ``ready for review`` once you are satisfied.**

.. _CI:

Continuous Integration
----------------------

Once the pull request has been opened, any changes to either it or the source
branch will trigger continuous integration (CI). CI is a way of running tests
on the changes proposed by the pull request. Due to resource constraints,
these tests are constrained in their size and usually target items such as
code styling.

.. important::

    CI tests will not run any atmosphere or integration models of simulation
    system code as these are too computationally expensive. These tests are
    run as part of the :ref:`rose-stem suites <testing>`. Some of the tests
    run by the continuous integration are also run as part of the rose-stem
    suites.

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

.. _merge_main:

Updating a branch
-----------------

Most development work in simulation-systems repositories will take place on a
branch created from ``stable``. Therefore it will need to be updated to match
the latest changes from ``main`` when a pull request is open. Github provides
functionality to do this in the browser, with the ability to fix merge
conflicts. Alternatively, you can do this from a terminal using git. For more
details see :ref:`updating a branch <updating_branch>`.

.. important::

    In order to aid the development of scientific suites, the majority of
    development should be done on a branch from ``stable`` without merging in
    changes from ``main``. Only when the development has been completed and
    the pull request is almost ready for commit should you merge in ``main``.
