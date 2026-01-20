.. _review_process:

Review Process
==============

.. tip::

    Github allows reviewers to directly make suggestions to the code. This is
    very useful for easily suggesting changes. However, the developer should
    always check carefully that the change is sensible and doesn't contain any
    errors or bugs.

Selecting Reviewers
-------------------

There is a space in the pull request template to list the GitHub user ID of the
scitech and code reviewers - these will also be filled into the appropriate
:ref:`project spaces <review_project>`.

.. admonition:: Requesting a Review

    Review requests are handled in the ``Reviewers`` pane on the right hand
    side of a pull request.

    In Simulation Systems repositories, SciTech and Code Reviewers will be
    automatically requested by a workflow, based on entries in the Pull Request
    Template.

    To request a review manually, select the cog, and then search for the person
    you wish to review by either name or GitHub user ID.

    .. image:: images/gh_screenshots/review_cog_light.png
       :class: only-light border

    .. image:: images/gh_screenshots/review_cog_dark.png
        :class: only-dark border

    Code owners in some repositories will automatically be added to this
    reviewers section based on the files being changed.


SciTech Review
^^^^^^^^^^^^^^

First refusal for completing the SciTech review should go to the main code
owner(s) for the area affected. If they don't want to then they may have
suggestions for other suitable reviewers or you can approach anyone who would
have good insight into the changes made.

Once you have found a reviewer and are ready for review, add their GitHub user
ID to the pull request description. Their review will automatically be
requested by the :ref:`review project workflow <review_project>`.

Guidance for the SciTech reviewer can be found on the
:ref:`SciTech review page <scitech_review>`.

Code Review
^^^^^^^^^^^

Code reviewers are assigned by the Simulation Systems and Deployment Team from
a pool of repository maintainers. New ``ready for review`` pull requests will be
assigned a reviewer on a regular basis. If you need your pull request looking at
more urgently than that, or think your pull request has been overlooked, then
leave a comment for ``@MetOffice/ssdteam`` on the pull request.

The assigned person will be listed in the pull request description and
:ref:`Review Tracking project <review_project>`. Once the SciTech review has
been completed, the Code Reviewer will be automatically requested (unless they
are already requested as a Code Owner - in this case you may want to tag them to
make them aware).

Guidance for the Code reviewer can be found on the
:ref:`Code review page <code_review>`.

.. _review_project:

Simulation Systems Review Tracker
---------------------------------

All open pull requests will be added to a GitHub Project called
``Simulation Systems Review Tracker``, which causes this box to appear in the
sidebar of the pull request:

.. image:: images/gh_screenshots/project_scitech_light.png
    :class: only-light border

.. image:: images/gh_screenshots/project_scitech_dark.png
    :class: only-dark border

The project is used to give pull requests a status that distinguishes between
the different review states, and to monitor who is doing the reviews. The state
and fields of the project are automatically updated by github actions.

* The developer should tag the SciTech Reviewer in the Pull Request template
  when you are ready for review. This will request a review from them and update
  the state to SciTech Review.
* The SSD team will add a Code Reviewer. When the Scitech Review has been
  completed a review from the Code Reviewer will automatically be requested, and
  the project state updated. If the Pull Request is trivial, you will need to
  manually request a review from the Code Reviewer.
* As reviews are completed the state will move to ``Changes Requested`` and
  ``Approved`` as appropriate. Re-request a review once any changes have been
  made.

  .. image:: images/gh_screenshots/rerequest_light.png
    :class: only-light border

  .. image:: images/gh_screenshots/rerequest_dark.png
    :class: only-dark border

* You can ``@username`` in any comment to draw that persons attention to the
    pull request.


.. _reviewer_edits:

Code Reviewer Edits
-------------------

As part of the process to commit certain tickets, code reviewers will sometimes
need to commit changes to the branch of a developer. Common reasons for doing
this include,

* Updating KGO's
* Applying upgrade macros
* Updating commit hashes for linked tickets

The ability to commit back to another users fork is only available to those with
``maintainer`` access or above and they can only do so for branches with an open
pull request and the ``Allow edits by maintainers`` option selected.
