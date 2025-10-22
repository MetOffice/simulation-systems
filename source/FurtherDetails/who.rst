Who's Who
=========

Every member of the community acts in one or more roles, depending on the work
at hand. These roles often align to different teams for practical purposes.

User
----

Users, in general, are anticipated to:

* Edit and manage rose suites via the roses repositories
* Edit suite tasks to manage code version (including use of upgrade macros),
  branches, science configuration and other settings to their needs
* Manage their usage of compute resource in-line with relevant guidance
* Ensure the scientific integrity of their use case

Notably, users in this context do not edit source code.

Developer
---------

Developers, in general, build on the User role:

* Write and edit source code
* Follow the Working Practices, even if their work is not intended for the
  trunk.
* Manage their work to allow reasonable time for approvals and reviews.

Notably, the Working Practices encourage and require engagement with other
roles. This helps promote cohesion and consistency, ultimately underpinning
confidence in the models as a whole.

.. _code_owner:

Code Owner
----------

Code Owners and their deputies take responsibility for defined parts of the
codebase:

* Working knowledge of the code, and any supporting items such as metadata
* Generally, focus will be on the scientific/functional aspects of the code,
  but also includes consideration of technical aspects with support from the
  Simulation Systems and Deployment Team
* Oversee the general arc of development of their sections
* Review and sign-off all changes to the code they own on an acceptable
  timescale
* In some cases they may make suggestions regarding changes outside of their
  section
* Often act as the Sci/Tech reviewer if their section is the primary focus of a
  change

.. _config_owner:

Configuration Owner
-------------------

Configuration owners are people that have chosen to protect a model
configuration (a specific arrangement on input settings and options) using the
rose-stem test harness.

* Working knowledge of the configuration
* Generally, focus will be on the scientific/functional aspect of the
  configuration, but also includes consideration of technical aspects with
  support
* Maintain, update and retire configurations to ensure they are relevant and
  useful
* Will often be the owner or a experienced user of standalone science
  evaluation suites that may be used to understand the magnitude of changes in
  model evolution
* Review and sign-off all changes to model output on an acceptable timescale

Importantly, rose-stem are the single source of truth for pass/fail protection
of model evolution.

.. _scitech_reviewer:

Sci/Tech Reviewer
-----------------

A Sci/Tech reviewer is assigned for every ticket and comprises the first stage
of review that considers the change as a whole. Further details are found in
the :ref:`Scitech Reviewers Guide<scitech_review>`. In some cases, the reviewer
can delegate parts of the work to another person.

Reviews should be turned around on a reasonable timescale and follow the
SciTech review guidance.

It is the responsibility of the developer to identify and arrange the Sci/Tech
reviewer. Often they will be someone in the same team as the developer or the
most relevant code owner.

.. _code_reviewer:

Code Reviewer
-------------

The Code Reviewer performs the 2nd stage of review for every ticket. Further
details are described in the :ref:`Code Reviewers Guide<code_review>`.

Reviews should be turned around on a reasonable timescale and follow the Code
Review guidance.

It is the responsibility of the developer to arrange the code reviewer.

Open Pull Requests will be assigned a Code Reviewer by the Simulation Systems
and Deployment team.

.. _simIT:

Simulation IT
-------------

The Simulation IT department are responsible for the various codebases that comprise
the Simulation Systems. The department includes the following teams:

Simulation Systems and Deployment Team:
    The SSD Team oversees the curation of the repositories, working practices
    and other supporting documentation, infrastructure and systems for all of
    the Simulation Systems projects.

    They provide support for the last 12 months of UM and LFRic Apps releases
    to the Met Office and Partners.

    The team can be contacted at ML-Simulation_Systems_and_Deployment@metoffice.gov.uk.

Core Capability Development Team:
    The CCD team is responsible for the LFRic Core infrastructure code which
    underpins several LFRic applications including the Momentum(r) atmosphere model.
    The team is keen to ensure that application developments continue to follow
    recommended standards such that applications benefit from the separation of
    concerns principles and portable performance capabilities that the LFRic
    core design and LFRic application development standards aim to support.

    The team can be contacted at CoreCapabilityDevelopmentTeam@metoffice.gov.uk.

Tools and Collaborative Development Team:
    The TCD Team is responsible for the development and integration of third
    party tools with LFRic including Psyclone, XIOS and LFRic Inputs.

    The team can be contacted at ToolsCollabDevTeam@metoffice.gov.uk



.. _hpc_opt_team:

HPC Optimisation Team
---------------------

The HPC optimistation team take a general lead in matters relating to compute
performance of the UM, LFRic and other systems.

* Examine and improve the performance and scalability of the UM and coupled
  models.
* Develop and maintain GCOM, the communications layer used by the UM and other
  systems in the Met Office.
* Development and support of the UM Packing/Unpacking?, Dump and I/O routines.
* Benchmarking UM software for HPC evaluations/procurement.
* Act as 'code' owners for performance-related aspects of the UM, notably
  OpenMP and compiler directives

The team can be contacted at Sci_Weath_hpc_opt@metoffice.gov.uk.

Momentum Partnership Team
-------------------------

The Momentum Partnership Team is responsible for engagement and support with
users and developers at Core and Associate `Momentum Partner
<https://www.metoffice.gov.uk/research/approach/collaboration/momentum-partnership>`_
organisations. The team can be contacted at
momentum_partnership@metoffice.gov.uk.
