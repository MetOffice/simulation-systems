Working with Multiple Repositories
==================================

The repositories covered by these WP's all interact with and have dependencies
on each other. This means that changes that affect multiple repositories need
handling with extra care.

To think about how the repositories work together it's useful to think about
them as almost concentric circles. The child repositories such as JULES or UKCA
sit in the centre and are mostly independent of anything else. The UM
is a parent of those repositories and is dependant on changes in it's own code
base and on those in the children. LFRic is then another layer again and is
dependant on both the UM physics and the other child repositories.

This means that changes to the science code in JULES etc will need testing with
both the UM and LFRic to check for any interactions. Likewise, changes to the
atmosphere code in the UM will require LFRic testing.

.. image:: images/repo_circles.svg
    :width: 300
    :align: center


Preparing Linked Tickets
------------------------
Every repository in a set of linked changes requires a ticket. Guidance on
setting these up can be found in :ref:`ticket`. These tickets will be treated
as a group with the same reviewers and committed at the same time.

Do:
    * Make sure every ticket has a cross reference to the others in the set, e.g. ``um:#1234``
    * Use keywords to show which other repositories are involved
    * Get the tickets ready for review at the same time
    * Ask for help testing if you don't have access to all the codebases involved

.. note::
    Code branches in linked tickets will require branching from compatible revisions
    to ensure they work together. The last released revisions will all be tagged
    with suitable keywords, or for head of trunk revisions please contact the
    Simulation Systems and Deployment Team for advice.

Testing Changes Together
------------------------
Multi-repository changes are expected to pass the regression tests for all the
repositories involved. To carry out the tests involved in a linked ticket it can
be helpful to refer to the semi-concentric circles above; layering the testing
from the inside out as needed. Further details of how testing in each
repository is handled can be found :ref:`here <testing>`.

    1. Firstly, testing changes in JULES, UKCA, or any other child repositories is
    as simple as running the standalone test proceedures for these codebases.

    2. Next, to test the UM, any changes to JULES etc will also need to be included.
    This is done by adding another source to the rose stem command line. So from a UM
    working copy:

    .. code-block::

        rose stem --group=developer,jules --source=. --source=/path/to/jules/changes --source=/path/to/ukca/changes

    The source paths involved can either be to local working copies or links to the
    fcm source control e.g. ``fcm:jules.x_br/dev/user/branch_name``. As many source
    paths as needed can be added to the list.

    3. Finally LFRic testing needs to encompass all of the other repositories
    affected. Paths to the other codebases involved should be added to
    ``fcm-make/parameters.sh`` under each of the ``*_sources`` variables. Again
    these paths can either be to local changes or those in the repository.

.. note::
    If any of the testing shows up failures then there are two possible ways to
    proceed:

    1. The changes made should be re-written to avoid breaking the dependant
       repositories

    2. The changes made directly affect the interface between repositories and
       therefore a change is also needed to the parent repository to adapt to that change.

    If you're uncertain which route to take then the Code Owners involved will
    hopefully be able to advise.