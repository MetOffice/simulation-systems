.. _dos_donts:

Do's and Don'ts
===============

Please Do
---------

**Consult** Code Owners and system team. This will help maintain awareness and
mitigate problems early on. This is the most common root cause of problems,
sometimes years later.

**Plan** your work aimed at the trunk across single or multiple tickets:
    * Ensure tickets are not too big or small.
    * Coherent parts of the overall change are contained in a single ticket
    * Consider using an overarching ticket to link everything together

**Document your work** using tickets, TRAC pages, :ref:`formal documentation
<docs>` and code comments. These help others and your future-self understand
your work.

**Meaningful names** for tickets, branches and variables. These help others and
your future-self understand your work. "My_Branch", "Fix" are not helpful.

**Be considerate** of other users/developers. Their skill-sets and working days
may be very different to yours. All changes are visible to all users
worldwide.

**Keep the ticket status up to date.** This enables the Simulation Systems and
Deployment Team to monitor the progress of your ticket and potential
conflicts.

**Link to tickets in other MOSRS repositories**, eg jules:#1, ukca:#72

Please Do Not
-------------

**Do not use svn commands.** Please use `FCM
<http://metomi.github.io/fcm/doc/user_guide/>`__ for all development work.

**Do not merge the trunk into your branch** for UM, JULES, UKCA and LFRic Apps
changes as this breaks many aspects of how TRAC and fcm work. This will cause
diffs to display incorrectly and causes database problems when merging.
Instead, please create a head of trunk branch and merge in your old branch.

**Do not develop using head of trunk branching if not needed.** Many aspects of
the UM, JULES and UKCA workflows rely on version branching.

**Licensing** - Don't add code to any project (or to any branch thereof) that
has been developed under a different license without agreement from the
Simulation Systems and Deployment Team. This includes lifting Fortran code or
text from books. Our repositiories must not infringe copyright.

**Add or link to old code** or tickets that predate MOSRS, for example...

* Link to tickets in old internal repositories- links will either not resolve
  or be incorrect
* Add a version of the UM code older than UM 9.2 as a branch to the UM
  repository

**Request support by raising a ticket**. Newly raised tickets are not
monitored. Use the appropriate :ref:`support` channels.
