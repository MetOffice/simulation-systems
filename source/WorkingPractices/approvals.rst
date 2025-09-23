.. _approvals:

Approval Process
================

Every pull request will need to get approval from a group of people. Code Owner
approvals are automatically requested when the pull request is marked as `Ready
for Review`, while required Configuration Owner approvals will be listed on the
trac.log testing summary.

.. tip::

    Make it really clear and easy for approvers to understand your change and
    know what needs approving - some get a lot of requests!

    You may need to chase up approvals occasionally. People are not perfect and
    remember to :ref:`be kind <code_of_conduct>`.

.. important::

    New UM Ancils must be submitted to the MIAO team for approval. Please
    follow their process for `Requesting New UM Ancils
    <https://code.metoffice.gov.uk/
    trac/ancil/wiki/ANTS/ProjectManagement/updating_UMDIR>`__.

Code Owners
-----------

Every file in the codebases has a :ref:`code_owner`, and every file changed
will need checking by the code owners - no matter how small the change.

A list of current code owners for each project can be found in the top level
``CODEOWNERS`` file.

Code Owners should complete a review requesting changes if needed, and
approving once they are happy. They only need to review changes that fall in their
area.

.. Tip::

    It is always worth talking to the main code owners involved early in the
    process. These people have good oversight on changes in an area and will
    be able to guide your change to fit in with the bigger picture of what is
    happening.

Code Owners are good candidates for choosing as a SciTech reviewer.

Config Owner
------------

:ref:`Configuration Owner's <config_owner>` are responsible for a combination
of settings in the model that achieve a particular aim (e.g. the current GAL
or RAL setup used operationally). Within the rose-stem testing these
configurations will be used and any changes to the answers shown in testing
will need sign off from the config owner.

In JULES, the code owner is supported by module leaders who will
sign-off scientifically significant changes to their areas of interest. The
module leaders in this case will also act as configuration owners for their
science settings.

A list of current config owners for the UM is found in
``trunk/ConfigOwners.txt``. Others are combined with the Code Owner lists
above.

Other Approvals
---------------

There are other changes that require specific approval and these are made clear
in the pull request description. For example, changes that modify code within an
OpenMP section will require approval from the :ref:`hpc_opt_team` and changes
that modify or add PSyKAl-lite code will require approval from the TCD Team.
