.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _fortitude_linter:

========================================
Fortitude Linter
========================================

Fortitude is a fortran linter that runs automatically when you run the test
suite. Links to the official documentation are included below:

Command line interface:
`<https://fortitude.readthedocs.io/en/stable/configuration/#full-command-line-interface>`_

Lint Rules and their Codes:
`<https://fortitude.readthedocs.io/en/stable/rules/>`_



Re-running Fortitude to fix lint errors
========================================

Lint errors go to job.err and in that report you can also see the: rule code, rule name, 
auto-fix options, and a summary of the repositories with errors at the bottom of the report.

When you have resolved the lint issue, see the instructions below on how to 
re-test quickly.

N.B. Some errors can be :ref:`fixed automatically <auto-fix>` by fortitude. 
This is rule dependent and Fortitude will let you know if the specific failure has this 
option under each error listed.

Testing with Test Suite:
------------------------

Run these commands from the inside the top directory of the codebase:

- You can re-run fortitude_linter individually:

.. code-block:: shell

    cylc vip -z group=fortitude_linter -n suite_name ./rose-stem

- Or with scripts group:

.. code-block:: shell

    cylc vip -z group=scripts -n suite_name ./rose-stem


Testing manually from the terminal:
----------------------------------------

The following commands run fortitude on specific files and specify the rule or 
configuration file. 
Fortitude can be run without specifying these things but it may pick up existing 
errors in the codebase that are unrelated to your changes.

The rule code associated with the error is given in the job.err report.

If the repository with the error uses the universal configuration 
(*lfric_apps/rose-stem/app/check_fortitude_linter/file/fortitude.toml*) 
for its fortitude tests, the job.out specifies that in that repo’s output 
section.
Otherwise, it will use its own configuration file, located in its top 
directory e.g. *lfric_apps/lfricinputs/fortitude.toml*.

Run the following commands from the inside the top directory of the codebase:

**First, load the lfric environment:**

.. code-block:: shell

    ml use ~lfricadmin/lmod
    module load lfric

**Then run fortitude with 1) the rule code, or 2) the config file :**

**1) With rule code:**

.. code-block:: shell

    fortitude check --select rule_code ./path_to_file_with_lint_error

**2)  With config file specified:**

2.A) If app/repo has its own configuration (.toml) file:

.. code-block:: shell

    fortitude --config-file ./path_to_repo_config_file check ./path_to_test_repo

2.B) If it uses the universal configuration (see job.out) then use this file path to it:

.. code-block:: shell

    fortitude --config-file ./rose-stem/app/check_fortitude_linter/file/fortitude.toml check ./path_to_repo_to_check

.. _auto-fix:

**If an automatic fix is available:**

Add ``--fix`` after the "check" in the command:

.. code-block:: shell

    fortitude --config-file ./path_to_repo_config_file check --fix ./path_to_file_with_lint_error

**Example commands:**

``fortitude check --select S101 ./applications/lfricinputs``

``fortitude check --select S101,PORT011 ./applications/lfricinputs``

where S101, or S101 and PORT011 are the lint rule(s) you want to test with.

``fortitude --config-file ./applications/lfricinputs/fortitude.toml check ./applications/lfricinputs``









