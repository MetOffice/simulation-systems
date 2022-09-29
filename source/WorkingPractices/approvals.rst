.. _approvals:

Approval Process
================
Every ticket will need to get approval from a group of people. These approvals
are marked on the Ticket Summary wiki pages by those signing off the approval.

Code Owners
-----------
Every file in the code bases has a :ref:`code_owner`, and every file changed
will need checking by the code owners - no matter how small the change.

A list of current code owners for each project can be found in
`trunk/CodeOwners.txt`.

.. Tip::

    It is always worth talking to the main code owners involved early in the
    process. These people have good oversight on changes in an area and will be
    able to guide your change to fit in with the bigger picture of what is
    happening.

Config Owner
------------
:ref:`Configuration Owner's <config_owner>` are responsible for a combination of
settings in the model that achieve a particular aim (e.g. the current GAL or RAL
setup used operationally). Within the rose-stem testing these configurations
will be used and any changes to the answers shown in testing will need sign off
from the config owner.

In some repositories, the code owner is supported by module leaders who
will sign-off scientifically significant changes to their areas of interest. The
module leaders in this case will also act as configuration owners for their
science settings.

A list of current config owners for the UM is found in `trunk/ConfigOwners.txt`.
Others are combined with the Code Owner lists above.

Optimisation Approvals
----------------------
Changes that modify code within an OpenMP section will require approval from the
:ref:`hpc_opt_team`.