.. _planning:

Planning Your Change
====================

There's often a tendency to jump straight into a change. This is fine for small
and simple changes where the purpose of the change is well-understood.
However, for more complex changes having a plan for the change before
developing it can be very beneficial and a well-thought plan improves the
chances of a successful code change.

Planning a change

* should not take long
* does not require submission for a review - the final code should speak for
  itself
* should help you understand the task and what it will involve
* should highlight some potential issues before development work starts

This is also a good time to consult with code owners(and also with
configuration owners, if necessary). Use the appropriate :ref:`support`
channels.

The following are some general hints and tips in planning code changes successfully.

.. tip::

    For more complex LFRic changes you can submit your plan to the Core Capability
    Development team for a Design Review.

.. seealso::
    :ref:`dos_donts`

General Considerations
----------------------

**How complex is your change likely to be?** (e.g. roughly how many subroutines
or lines of code do you expect to alter or add?) This is an important
consideration as the more complex a change is, the more time will be required
in development, the more code owners will need to approve it and so forth. If a
change is overly complex, the developer should consider breaking it up into
smaller, more manageable and, where possible, "self contained" tickets.

**How does your proposed change fit in with the structure of the model?** Try
and make your code changes in-scope and no larger than they need to be. If you
find yourself having to edit large areas of code in other, unrelated sections
of the model purely to get your change to work, chances are that you're doing
something wrong. Please do seek advice.

**Ensure that your code change meets coding standards** All models have various
coding standards and things to avoid, so it is useful for the developer to be
aware of these.

* `UMDP3 (UM and JULES FORTRAN)
  <https://code.metoffice.gov.uk/doc/um/latest/umdp.html#003>`__
* `LFRic Coding Styles
  <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/CodingStandards>`__
* `PEP 8 (Python) <https://legacy.python.org/dev/peps/pep-0008/>`__

**Who will SciTech review the change?** This is a useful consideration as not
everyone who uses the repository has the knowledge or experience to review
every ticket that is being developed. Get in touch with your SciTech reviewer
early in the process as they will have valuable insights that can help to shape
your change.

**Does your change fix a bug or are you investigating a bug in the code?** If
so, be aware that any changes to answers will require a KGO update and
configuration owners to approve the change, which can take longer. Code changes
which require a change in answers and configuration owner approval should be
planned well in advance of the code review deadline to allow time for the
approvals to take place.

**Is the code you need to alter on a single repository or is it spread over
multiple repositories?** If it's over multiple repositories you need to use
linked tickets. See :ref:`multirepo` for further details.

**Does similar code functionality already exist in the model?** It's a good
idea **not** to re-invent the wheel or have code duplication! Speaking to code
owners of the appropriate sections can help in this instance.

Specific Tips for Scientific changes
------------------------------------

**Does the change add a new option or feature to the code?** If so, you
probably need a new namelist variable to switch the new option off and maintain
regression. This will also imply changes to the metadata are required and an
upgrade macro to include the switch into the upgraded configuration.

**How are you going to prove that your change works scientifically?** It's
vital to make sure your code changes work when switched **on** and give the
same answer when the code is run over different processor configurations.
Producing a quick plot or plots to show the impact of your code and including
them on your ticket can aid your SciTech reviewer in showing that your code
works properly.

**Does the change need any new diagnostics to make sense of the code?** Many
changes will be able to use the existing diagnostics available, but if some
novel functionality is being developed it may require new diagnostics to be
added. The developer needs to check that new diagnostics output correctly and
look sensible.

**Does your change need new prognostic variables including?** If so, these need
to be added and it is worth checking that these work properly. In the UM in
particular, adding prognostic variables involves editing a lot of routines and
is quite time-consuming.


Specific Tips for Technical changes
-----------------------------------

**Avoid wholesale technical changes** These can be very cumbersome to review;
if it's possible, split the change into more manageable chunks.

**How does your change affect the performance of the model?** If your change
intends to optimise code, be prepared to provide evidence of how things have
improved.

..
    Comment: Are there any more that can be thought of? These tickets will
    mostly be done by experienced developers and usually inside the Met
    Office.
