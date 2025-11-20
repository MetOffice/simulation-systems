.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _dos_donts:

Do's and Don'ts
===============

Please Do
---------

**Consult** Code Owners and system team. This will help maintain awareness and
mitigate problems early on. This is the most common root cause of problems,
sometimes years later.

**Plan** your work aimed across single or multiple Issues and Pull Requests:

  * Each pull request should contain a single coherent change.
  * Consider using an overarching issue to link everything together

**Document your work** using Issues and pull requests, :ref:`formal documentation
<docs>` and code comments. These help others and your future-self understand
your work.

**Meaningful names** for issues, pull requests, branches and variables. These
help others and your future-self understand your work. "My_Branch", "Fix" are
not helpful.

**Be considerate** of other users/developers. Their skill-sets and working days
may be very different to yours. All changes are visible to all users
worldwide.

**Link to issues/pull requests in other repositories**, eg ``MetOffice/jules#1``,
``MetOffice/ukca:#72``

Please Do Not
-------------

**Do not merge ``main`` into your branch** during the development process. To
aid scientific evaluation, changes should be kept in standalone branches based
on the last stable version.

When your change is ready for Code Review, we then suggest merging in ``main``
and resolving any conflicts.

**Licensing** - Don't add code to any project (or to any branch thereof) that
has been developed under a different license without agreement from the
Simulation Systems and Deployment Team. This includes lifting Fortran code or
text from books. Our repositiories must not infringe copyright.

**Request support by raising an issue**. Newly raised issues are not
monitored. Use the appropriate :ref:`support` channels.
