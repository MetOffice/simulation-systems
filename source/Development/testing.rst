.. _testing:

Testing Your Change
===================

Every change should be thoroughly tested, using your judgement as to what this
involves based on the complexity of your change. There are three main methods
for you to choose from:

Rose-stem:
    Every repository has a rose-stem test suite that provides integration and
    regression testing - and in some cases unit tests as well. Committing
    changes to the trunk of each repository is dependant on these tests
    passing; they are there to ensure the integrity of the codebase.

Standard suites:
    As well as the rose-stem tests you should also consider how best to prove
    that your change does what it says it does, and not what it doesn't. There
    may be other standard suites that will exercise your change in a
    scientific or technical way. If you're unsure on what that is then talk to
    the code owners involved for advice.

Bespoke:
    If the above hasn't satisfied you (or your SciTech reviewer) then you may
    wish to consider further evaluation by creating your own tests.


.. toctree::
   :maxdepth: 1
   :caption: Test Suites

   TestSuites/um
   TestSuites/lfric_apps
   TestSuites/lfric_core
   TestSuites/jules
   TestSuites/ukca
   TestSuites/multi-repo_testing

.. todo:
   TestSuites/casim
   TestSuites/shumlib

Test branches & Upgrade Macros
------------------------------

There are a few cases where testing your change will require you to make
changes to your branch that don't want committing to trunk. To do this you can
create a test branch. This is a branch-of-branch from your development branch
and allows you to make those changes in an isolated environment while leaving
your original development clean.

To create one:

.. code-block:: shell

    fcm bc -t test --bob testbranchname \
    fcm:project.x_br/dev/yourname/devbranchname

Then check this out and use it for running any tests you'd like to carry out.

If using a test branch then do list this on your ticket and include the results
of this testing alongside those from your dev branch.

.. Note::

    If your tests fail then you will need to make and commit the fixes to the
    development branch and create a new test branch from that latest revision
    to test them.

Macros
^^^^^^

If you have updated the model inputs and included an upgrade macro with your
change then this macro will be run by your code reviewer as part of the commit
process. In order to prove that the upgrade macro will be successful, and to
make those new model inputs available to your tests, you should create a test
branch as described above and run the upgrade macro with one of the following
commands, noting that ``--jules-path`` is only required if you have
**jules-shared** metadata changes. Please see the shared metadata
:ref:`guidance<shared-namelists>`.

+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UM    | ``./admin/rose-stem/update_all.py --path=/path/to/working/copy/of/test/branch --um=vnX.X_tXXXX [--jules-path=/path/to/jules/working/copy/of/branch]``                        |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| JULES | ``./bin/upgrade_jules_test_apps vnX.X_tXXXX``                                                                                                                                |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| LFRic | ``apply_macros.py vnX.Y_tZZZZ [--apps=/path/to/apps] [--core=/path/to/core] [--jules=/path/to/jules]``                                                                       |
+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. tip::

    The ``apply_macros.py`` script is located in the `SimSys_Scripts github
    repo <https://github.com/MetOffice/SimSys_Scripts>`__ (at meto an up to
    date clone is available in $UMDIR/SimSys_Scripts).

.. warning::

    Please ensure that Cylc7 is used with ``update_all.py`` @vn13.5. This is
    fixed at HoT and either Cylc7 or Cylc8 can be used.

.. Note::

    The update_all.py script suppresses warnings produced by upgrade macros.
    You can test these separately by upgrading a single app. A single app can
    be upgraded for testing using:

    .. code-block:: shell

        rose app-upgrade -M /path/to/rose-meta \
            -C /path/to/rose-stem/app/<app_name> -a <trunk_metadata_version>

   where the ``-C`` option can be omitted if inside the app's directory.

    .. Important::

        If there are **jules-shared** metadata changes these will need to be
        added to the metadata path. Please see the :ref:`rose config-edit
        example<metadata_changes>`.

        Please refer to `rose app-upgrade
        <https://metomi.github.io/rose/doc/html/api/command-reference.html#rose-app-upgrade>`__
        command reference for more details.

.. _traclog:

trac.log
--------

The output of rose-stem from each repository includes a trac.log. This is a
wiki formatted file that can be copied into the ticket summary as a record of
testing run. Please make sure that the results of your latest testing are
included when passing a ticket for review.

.. code-block:: shell

    ~/cylc-run/<suite_name>/trac.log


.. tip::

    If your suite has finished and no trac.log has been generated then it is
    possible to do so manually using `suite_report.py
    <https://github.com/MetOffice/SimSys_Scripts/blob/main/suite_report.py>`__

    On Met Office desktops a copy is stored locally allowing this to be done
    with:

    .. code-block:: shell

        python3 $UMDIR/SimSys_Scripts/suite_report.py -S <workflow path>

    If this is a regular problem then get in touch with the :ref:`SSD team
    <ssd>` so we can investigate. Thanks.
