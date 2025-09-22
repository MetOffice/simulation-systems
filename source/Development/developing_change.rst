.. _development_index:

Developing Your Change
======================

How a change is developed generally depends on the nature of the change and the
size of the code change: small code changes of just a few lines can be written
in minutes before being tested. For anything longer and more complex, it is
worth developing the code in small sections or units, testing that each piece
of code works before committing back to the development branch. By following
this methodology, if one aspect of the code doesn't work, there is always the
option to revert the local changes and quickly return to a checkpoint in your
development that did work.


.. tip::

    Before embarking on a medium-sized or significant model change, it is
    useful to have an appropriate coding plan in place. See :ref:`planning`
    for further details.

.. note::

    Do not add AI-generated code, e.g., from GitHub CoPilot to any branches or
    forks.

Code changes should conform to the coding standards of the project.
Remember to ensure that your changes are easy to read and follow, using
comments to explain what the code is doing.

The vast majority of changes will be based around a project's source
code, though there are other infrastructure areas involved. Rarely, the
developer may alter one of these *without* modifying the source code.

Every change is different, but there are a few key attributes that
increase the complexity of a particular change and should be considered
carefully:



.. toctree::
    :caption: Development Checklist
    :maxdepth: 1

    planning_your_change
    documentation
    inputs
    kgo
    diagnostics
    rose_stem
    testing

.. important::

    All instructions regarding code locations in this section assume you are
    working in a clone of the appropriate repository. Please read
    the :ref:`working_practices_index` to discover more.
