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

Lint errors go to job.err and you can see the: repository name, file, rule code, 
rule name, number of errors in each repo, auto-fix options, and a summary of 
repos with errors at the bottom of the report. When you have resolved the lint 
issue, see the instructions below on how to re-test quickly. You may be able to 
use fortitude to run an automatic fix - this is rule-dependent and Fortitude 
prints if the rule has that option under the error message. 
See instructions below on how to do run with :ref:`automatic fixing <auto_fix>`

Testing with Test Suite:
------------------------

Run these commands from the inside the top directory of the codebase.

Can re-run fortitude_linter individually:

.. code-block:: shell

    cylc vip -z group=fortitude_linter -n suite_name ./rose-stem

Or with scripts group:

.. code-block:: shell

    cylc vip -z group=scripts -n suite_name ./rose-stem


Testing manually from the terminal:
----------------------------------------

With the either the A rule code, or B configuration file specified, 
and specific files to run on specified:
N.B. If you don’t specify rules or a config file, you will get lots of errors 
unrelated to your changes (that already exist in the codebase), so it is 
advised you do specify them.
The rule code associated with the error is given in the job.err report. 
If the repository with the error uses the universal configuartion 
(lfric_apps/rose-stem/app/check_fortitude_linter/file/fortitude.toml) 
for its fortitude tests, the job.out specifies that in that repo’s output 
section. Otherwise, it will use its own configuration file, located in its top 
directory e.g. lfric_apps/lfricinputs/fortitude.toml.

Run these commands from the inside the top directory of the codebase.


.. _auto_fix:

Testing with auto-fix option:
----------------------------------------
Some errors can be fixed automatically by fortitude. This is rule dependent 
and Fortitude will let you know if the specific failure has this option under 
each error listed.

fortitude  check --select rule_code --fix ./path_to_file_with_lint_error
e.g. fortitude check --select S101 --fix ./applications/lfricinputs
