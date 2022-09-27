.. _planning:

Planning Your Change
====================

There's often a tendency to jump straight into a change. This is fine for small and
simple changes where the purpose of the change is well-understood. However, for more complex
changes having a plan for the change before developing it can be very beneficial. Writing code
without a plan can lead to ill-thought out development and in some cases leads to a time-consuming
rewrite of the code during the development process. This is also a good time to consult with code owners
(and also with configuration owners, if necessary).

Planning a change should not take long and should take no more than a few minutes.
A plan is there to assist the developer; there is no requirement to submit your plan for review
as the final code should speak for itself. A plan can be entirely within the developer's head,
on paper or in electronic format. The most important aspect is for the developer to work though
a thought process about what the code change will involve, so that they understand the task
and hopefully understand what potential issues could arise before development work starts.

The following are some general hints and tips in planning code changes successfully.


General Considerations
----------------------

**How complex is your change likely to be?** (e.g. roughly how many subroutines or lines of code do
you expect to alter or add?) This is an important consideration as the more complex a change is, the
more time will be required in development, the more code owners will need to approve it and so forth.
If a change is overly complex, the developer could consider breaking it up into smaller, more
managable tickets.

**Who will SciTech review the change?** This is a useful consideration as not everyone who uses the
repository has the knowledge or to review every ticket that is being developed. It can be worth
identifying a SciTech reviewer before starting work to avoid having developed the ticket, only to
find nobody is available to review it.

**Does your change fix a bug or are you investigating a bug in the code?** If so, be aware than any
changes to answers will require a KGO update and configuration owners to approve the change, which
can take longer.

**Is the code you need to alter on a single repository or is it spread over multiple repositories?**
If it's over multiple repositories you need to consider linked tickets.

(Link here to linked changes?)

**Does similar code functionality already exist in the model?**


Specific Tips for Scientific changes
------------------------------------

**Does the change add a new option or feature to the code?** If so, you probably need a new namelist
variable to switch the new option off and maintain regression. This will also require metadata and


**Does the change need any new diagnostics to make sense of the code?**


Specific Tips for Technical changes
-----------------------------------
