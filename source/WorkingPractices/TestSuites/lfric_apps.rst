.. _lfric_apps_test:

Testing LFRic Apps
==================

LFRic Apps testing is run with the following commands from a working copy:

    .. code-block::

        export CYLC_VERSION=8
        rose stem --group=developer
        cylc play <working copy name>

-----

The LFRic Apps rose stem includes a range of tests to exercise all the applications
stored in this repository, using multiple compilers, and checksum and plot tasks to
confirm the outputs.

.. tip::

    For LFRic Apps it is possible to update the checksum files on your branch to
    aid with testing and development. To do so run the rose-stem suite as described
    to cover all failing tests, then run the following from your working copy

    .. code-block::

        python3 ./rose-stem/bin/update_branch_kgos.py -s <suite name> -w <path to working copy>

    More details on the KGO update proceedures for all repositories can be found
    :ref:`here <kgo_instructions>`.

Below is a (by no means comprehensive) set of groups that you may wish to use on
Met Office systems. Note that there is a lot of overlap between these groups,
and that you can specify more than one at once, e.g. ``--group=developer,gungho_model``.



+--------------------+----------------------------------------------------------+
| Group              | Description                                              |
+====================+==========================================================+
| developer          | Standard group of tests that every change is expected    |
|                    |                                                          |
|                    | to pass before commit. It is a useful checkpoint during  |
|                    |                                                          |
|                    | development.                                             |
+--------------------+----------------------------------------------------------+
| nightly            | More thorough testing group. This includes everything in |
|                    |                                                          |
|                    | developer plus some longer and more complex tests. It is |
|                    |                                                          |
|                    | run automatically every night and monitored by the SSD   |
|                    |                                                          |
|                    | team.                                                    |
+--------------------+----------------------------------------------------------+
| all                | The complete test suite, including all longer runs and   |
|                    |                                                          |
|                    | less commonly used utilites. This is run automatically   |
|                    |                                                          |
|                    | every week and monitored by the SSD team. All            |
|                    |                                                          |
|                    | :ref:`KGO <kgo>` changing tickets need to run this group.|
+--------------------+----------------------------------------------------------+
+--------------------+----------------------------------------------------------+
| build              | Compile tasks for all applications and science areas     |
+--------------------+----------------------------------------------------------+
| unit_tests         | Unit tests for all applications and science areas        |
+--------------------+----------------------------------------------------------+
| integration_tests  | Integration tests for all applications and science areas |
+--------------------+----------------------------------------------------------+
| xc40/spice/monsoon | All tests designed to run on the named platform.         |
+--------------------+----------------------------------------------------------+
| scripts            | All of the auxillary scripts that are designed to check  |
|                    |                                                          |
|                    | the code standards in ways that aren't tested by the     |
|                    |                                                          |
|                    | compiler.                                                |
+--------------------+----------------------------------------------------------+

As well as these general groups, each area in ``<lfric_apps>/applications`` and
``<lfric_apps>/science`` have a set of specific groups that are structured as below,
with ``name`` matching the directory name of the area.

+--------------------+----------------------------------------------------------+
| Group              | Description                                              |
+====================+==========================================================+
| <name>             | Full set of tests for this area                          |
+--------------------+----------------------------------------------------------+
| <name>_<group>     | Tests for this area that are part of this group          |
|                    |                                                          |
|                    | e.g. gungho_developer or lfric_atm_spice                 |
+--------------------+----------------------------------------------------------+

