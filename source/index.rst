.. WorkingPractices documentation master file, created by
   sphinx-quickstart on Thu Sep  8 14:00:33 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:html_theme.sidebar_secondary.remove: true

Simulation Systems Working Practices
====================================

**These pages describe the working practices of the following simulation and
model codes owned by the Met Office:** `LFRic Applications <https://github.com/MetOffice/lfric_apps>`_,
`LFRic Core <https://github.com/MetOffice/lfric_core>`_ `UM <https://github.com/MetOffice/um>`_,
`JULES <https://github.com/MetOffice/jules>`_, `SOCRATES <https://github.com/MetOffice/socrates>`_,
`CASIM <https://github.com/MetOffice/casim>`_ and `UKCA <https://github.com/MetOffice/ukca>`_.

This includes how to get started, key points on developing your change and how
to test those developments. There is guidance on making changes that span multiple
projects and how to progress your change through review.

There are then notes for reviewers on how to tackle the different types of review
and how to commit to the trunk.



.. grid:: 1 1 2 2

    .. grid-item-card::
        :text-align: center

        Working with git and github to contribute to the simulation models.

        +++
        .. button-ref:: working_practices_index
            :ref-type: ref
            :color: primary
            :outline:
            :expand:

                Working Practices

    .. grid-item-card::
        :text-align: center

        Guides to planning, developing and testing changes to the simulation models

        +++
        .. button-ref:: development_index
            :ref-type: ref
            :color: primary
            :outline:
            :expand:

                Developing Your Change

.. grid:: 1 1 2 2

    .. grid-item-card::
        :text-align: center

        Information on reviewing for, committing to and releasing these projects.

        +++
        .. button-ref:: reviewers_index
            :ref-type: ref
            :color: primary
            :outline:
            :expand:

                Guides for Reviewers

    .. grid-item-card::
        :text-align: center

        Support information, glossary and code of conduct.

        +++
        .. button-ref:: further_details
            :ref-type: ref
            :color: primary
            :outline:
            :expand:

                Further Details






.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Working Practices

    WorkingPractices/working_practices

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Developing Your Change

    Development/developing_change

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Guides for Reviewers

    Reviewers/index

.. toctree::
    :maxdepth: 1
    :hidden:
    :caption: Further Details

    FurtherDetails/index


More detailed, project specific, documentation is also available. See the wiki pages in each repository as well as
the :ref:`docs` page for more information on what is available and how to contribute to it.
