.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _ai:

AI Policy
=========

The primary objective of this policy is to prevent the introduction of
third-party intellectual property rights (IPR)-protected code into the
simulation systems.

This policy is written so it can be reused across open source repositories
using the BSD-3-Clause licence, which does not define requirements for
AI-assisted contributions.

Scope
-----

This policy applies to AI-assisted contributions in:

* source code
* tests
* scripts and configuration
* documentation, including prose/narrative content and code examples

For this policy, AI-assisted means content generated, completed, or
substantially refactored by a Generative AI tool.

Core Principles and Tool Restrictions
-------------------------------------

* **Acknowledge Public-Domain AI Risks**: AI tools trained on public
  repositories can generate code that violates open-source licences or
  copyrights.
* **Do Not Use Free or Personal-Tier Tools**: Use of free or personal-tier
  AI coding tools is *strictly prohibited* for project contributions.
* **Use Approved Enterprise-Tier Tools Only**: Contributors may only use
  enterprise-tier AI tools approved by their employing organisation or the
  repository maintainers.
* **Prohibit AI Agents From Committing Code**: AI tools and agents are not
  permitted to directly commit code, open pull requests, or perform repository
  operations. All AI-generated or AI-assisted content must be reviewed,
  validated, and committed by a human contributor with explicit intent and
  accountability.
* **Assume Full Contributor Responsibility**: The human contributor is
  responsible for all submitted content, including correctness, licensing
  checks, and project standards compliance.

.. dropdown:: Internal Met Office Contributors

    For guidance specific to the Met Office, consult the
    `central Met Office AI Policy <https://metoffice.sharepoint.com/sites/AICommsSite/SitePages/Met-Office-AI-Policy.aspx>`__.

Approved enterprise-tier tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An approved tool must satisfy all of the following:

* enterprise-tier licence with auditable terms of use
* terms that allow open source contribution workflows
* explicit organisational approval by employer or project maintainers
* controls appropriate to institutional IPR and data handling requirements

If a contributor cannot use an approved enterprise-tier tool, code must be
written manually without the use of any AI or machine learning (ML) code
generation assistants.

Legal framing and BSD-3-Clause compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This policy adds process controls for AI use. It does not alter the
BSD-3-Clause licence terms, warranties, or disclaimers.

Attribution and review requirements in this policy are **mandatory**
contribution conditions for the simulation systems repositories.

Attribution Requirements
------------------------

If an approved Generative AI tool is used, you **must** provide attribution in
two places:

**1. the source file header**

Add a comment near the top of the file, including documentation-only files
(for example ``.rst`` files with no code examples). Use the native comment
style for the language or markup, for example:

.. tab-set::

   .. tab-item:: Fortran

      .. code-block:: f90

         ! Some content in this file was generated or refactored with assistance from
         ! - [Tool Name] ([Model Version]).

   .. tab-item:: Python

      .. code-block:: python

         # Some content in this file was generated or refactored with assistance from
         # - [Tool Name] ([Model Version]).

   .. tab-item:: C++

      .. code-block:: cpp

         // Some content in this file was generated or refactored with assistance from
         // - [Tool Name] ([Model Version]).

   .. tab-item:: reStructuredText

      .. code-block:: rst

         ..
            Some content in this file was generated or refactored with assistance from
            - [Tool Name] ([Model Version]).

.. dropdown:: Internal example (non-normative)

    For Met Office contributors, the following is an acceptable example tool
    identifier: ``Met Office GitHub Copilot Enterprise (Claude Sonnet 5)``.

    This example is provided for convenience. It does not change the
    requirement that only approved enterprise-tier tools may be used.

Do not repeat attribution or the tool name in the file header if it is already
included. If you use a new tool or version, add it to the list instead. For
example, on first use:

.. code-block:: text

  Some content in this file was generated or refactored with assistance from
  - [Institution Name] [Tool Name] (Claude Haiku 4.7)

After a newer version of the same tool is used:

.. code-block:: text

  Some content in this file was generated or refactored with assistance from
  - [Institution Name] [Tool Name] (Claude Haiku 4.7/4.8)

After a second tool is also used:

.. code-block:: text

  Some content in this file was generated or refactored with assistance from
  - [Institution Name] [Tool Name] (Claude Haiku 4.7/4.8)
  - [Other Institution Name] [Other Tool Name] (Claude Opus 4.8)

**2. the pull request description**

Commit messages are easy to forget, especially across multiple commits, and
are not reliably enforceable before merge. The pull request description
**must** therefore identify the tool and what it assisted with, for example:

.. code-block:: text

  Assisted-by: [Tool Name] ([Model Version])
  for spatial interpolation optimisation.

Repeating the same note in individual commit messages is encouraged for
traceability, but is not a substitute for the pull request description, which
is what reviewers check before merge.

Attribution must be specific enough for later audit. Include tool name,
model/version where available, and date in the source file header.

Code Review Guidelines
----------------------

Reviewers must remember that AI-generated code is not self-authenticating.
The human contributor remains fully responsible for its contents.

Reviewer Checklist Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^

+------+--------------------+------------------------------+------------------------+
| Step | Action             | Pass Criteria                | Fail Action            |
+======+====================+==============================+========================+
| 1    | Check file header  | Explicitly names approved    | Block merge if         |
|      | and PR description | enterprise-tier tool and     | free/personal tier     |
|      |                    | includes required attribution| is used                |
+------+--------------------+------------------------------+------------------------+
| 2    | Check licence      | No obvious proprietary or    | Pause merge and        |
|      | compatibility      | or restrictively licensed    | request proof of       |
|      |                    | copy-pasted snippets         | origin/provenance      |
+------+--------------------+------------------------------+------------------------+
| 3    | Assess Logic and   | Reviewer understands every   | Request revisions for  |
|      | Edge Cases         | line; edge cases are handled | "black box" code       |
+------+--------------------+------------------------------+------------------------+
| 4    | Run Test Suite     | Code passes all unit,        | Block merge until      |
|      |                    | integration, and             | tests pass natively    |
|      |                    | regression tests             |                        |
+------+--------------------+------------------------------+------------------------+

Enforcement and Remediation
---------------------------

The enforcement model is corrective-first, except where banned tools or
unresolved IPR risk is involved.

* Missing attribution: request correction before merge.
* Free/personal-tier AI use: block merge until replaced with compliant
  contribution.
* Suspected licence/IPR conflict: pause review, request provenance, and escalate
  to maintainers.

If an IPR issue is discovered after merge, maintainers should choose one of:

* revert the change
* rewrite affected code
* retain with verified, compatible attribution where legally valid
