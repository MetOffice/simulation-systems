About the Working Practices
===========================

The Working Practices (WPs) are to be followed for all LFRic, UM, JULES, and
UKCA developments.

If this is your first development we highly recommend following these pages
through in sequence. Note that we get regular feedback that the WPs are both too
long and too short. What may be overwhelming detail for one person may be
insufficient detail for another.

**Details of recent changes to these practices can be found here:** :ref:`changes`

Development Cycle Overview
--------------------------
The general features of the development cycle are similar to those found in
other scientific software. However, the details are tuned to meet the needs of
the community as a whole. A key feature is the use of versions as a way of
periodically bringing everything together. Although many elements of Continuous
Integration and related approaches to software management can be found, the
nature of LFRic and UM makes following these impractical.

The release cycle follows a semi-regular cadence, balancing flexibility to
facilitate high priority goals against stability for the broader developer pool.
Each release will consist of a development window spanning from release of the
previous version to a pre-announced code review deadline. Following this,
submissions will be processed culminating in the release of the next release.
From time to time, some or all parts of a repository may be subject to an agreed
closed release to facilitate an intense or disruptive development.

.. Todo - make a diagram of rough release schedule (pictures to help break up text!)

The release cycle is overseen by the Simulation Systems and Deployment Team with
the oversight and support of the **Atmos Project Board??**, and impartially consider
the needs of all developers and users.


Before You Start
----------------
All developments should be planned using a risk-based approach. Before starting,
consider the complexity and impact of what you want to do. This will act as a
guide for the level of planning and consultation required. There is no
definitive process for this and developers should use their experience and
judgement.

As you begin, there are various people you might consider consulting:

    * Consult relevant :ref:`Code and Configuration Owners <approvals>`
    * Consult the Simulation Systems and Deployment Team
    * Less experienced developers may benefit from a 'buddy'

Technical Considerations
^^^^^^^^^^^^^^^^^^^^^^^^

Consider splitting work over multiple tickets:

    * Tickets laying foundations for later are OK
    * Tickets should make sense on their own with a clear scope
    * Tickets should not be too small or too large
    * Beware of the 'also trap'- the 'also' bits can swamp the main aim of your change!

Consider the timing of your work:

    * Be aware of others doing work in similar areas
    * Be aware of code review deadlines
    * Be aware of closed releases or planned outages
    * Allow contingency time when agreeing broader project deadlines. Trunk integrity will not be compromised to meet your deadlines.

Consider bringing planning together using an overarching ticket. It can be very
helpful for documenting and monitoring progress of your work.

Early planning and consultation is strongly recommended to prevent
disappointment later. More detailed guidance is provided on the :ref:`planning` page.

Special Types of change
^^^^^^^^^^^^^^^^^^^^^^^

Every change is different, but there are a few key attributes that increase the
complexity of a particular change. Extra guidance is provided where appropriate.
Common 'specials' include:

    * Changing Known Good Output (KGO tickets)
    * Changing Inputs
    * Linked change across multiple repositories (Linked tickets)
    * Documentation
    * Wholesale

Further thoughts before you begin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   planning_your_change
   dos_donts
   terms_of_reference

.. toctree::
   :hidden:

   change_notes

