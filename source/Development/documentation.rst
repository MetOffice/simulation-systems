.. _docs:

Documentation
-------------

All projects have their own scientific and technical documentation. Most
notably:

+----------------------------+-----------------------------+-------------------------------------------------+
| UM Documentation Papers    |`view UM`_                   | `edit UM`_                                      |
+----------------------------+-----------------------------+-------------------------------------------------+
| JULES User Guide           |`view JULES`_                | :doc:`edit JULES <jules_docs>`                  |
+----------------------------+-----------------------------+-------------------------------------------------+
| LFRic Documentation Papers |`view LFRic`_                | `edit LFRIc`_                                   |
+----------------------------+-----------------------------+-------------------------------------------------+

LFRic Apps and Core also use doxygen to document the code and all changes
should include appropriate doxygen changes to go with them. Doxygen guidelines
are available on the `LFRic Technical pages
<https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/Documentation/DoxygenUsage>`__.

.. toctree::
    :hidden:

    jules_docs

.. _view UM: https://code.metoffice.gov.uk/doc/um/latest/umdp.html
.. _edit UM: https://code.metoffice.gov.uk/trac/um/wiki/WorkingPractices/Documentation/UpdatingUMDPs
.. _view JULES: https://jules-lsm.github.io/latest/index.html
.. _edit JULES: https://code.metoffice.gov.uk/trac/jules/wiki/BuildingEditingUserGuide
.. _view LFRic: https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicDocumentationPapers
.. _edit LFRIc: https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical#Documentation

Small changes and bug fixes rarely need documentation to be updated, but when
new science is added to a project, the documentation must be updated to ensure
that it remains contemporary with the code.

.. tip::

    Searching the relevant documentation for words related to your change is
    often useful when deciding whether to update the documentation.

Documentation changes that are held within a repository are formally reviewed,
and should be included on the same ticket as the code changes - making sure
both code and docs branches are clearly listed and the `doc` keyword is
applied.
