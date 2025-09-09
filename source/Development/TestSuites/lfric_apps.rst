.. _lfric_apps_test:

Testing LFRic Apps
==================

Rose stem:

    LFRic Apps testing uses rose-stem and is run with the following commands
    from a working copy:

    .. code-block:: shell

        export CYLC_VERSION=8
        rose stem --group=developer
        cylc play <working copy name>
        cylc gui

Local testing:

    Alternatively, a single application can be built and run locally using
    `these instructions
    <https://code.metoffice.gov.uk/trac/lfric_apps/wiki/local_builds>`__

    This test does not use rose or cylc and is particularly useful for checking
    for compile errors while developing.

-----

.. important::

    When specifying the lfric_core source the lfric_core revision **must** be
    updated in ``dependencies.sh``.

    * If setting the source to an fcm URL, the mirror (``.xm_``) needs to be
      used and the revision can either be blank (for latest commit) or any
      valid revision for that branch.
    * If setting the source to a Working Copy, the hostname needs to be
      provided (as Hostname:Path) and the revision must be blank.

    For more details, see :ref:`multi-repo_testing`.


Rose stem
---------

The LFRic Apps rose stem includes a range of tests to exercise all the
applications stored in this repository, using multiple compilers, and checksum
and plot tasks to confirm the outputs.

.. tip::

    For LFRic Apps it is possible to update the checksum files on your branch
    as you progress your development to aid with testing. Details on how to do
    this are on the :ref:`KGO page <kgo>`.

Below is a (by no means comprehensive) set of groups that you may wish to use
on Met Office systems. Note that there is a lot of overlap between these
groups, and that you can specify more than one at once, e.g.
``--group=developer,gungho_model``.

+--------------------+----------------------------------------------------------+
| Group              | Description                                              |
+====================+==========================================================+
| developer          | Standard group of tests that every change is expected    |
|                    | to pass before commit. It is a useful checkpoint during  |
|                    | development.                                             |
+--------------------+----------------------------------------------------------+
| all                | The complete test suite, including all longer runs and   |
|                    | less commonly used configs. This is run automatically    |
|                    | every week and monitored by the SSD team. All            |
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
|                    | the code standards in ways that aren't tested by the     |
|                    | compiler.                                                |
+--------------------+----------------------------------------------------------+

As well as these general groups, each area in ``<lfric_apps>/applications`` and
``<lfric_apps>/science`` have a set of specific groups that are structured as
below, with ``name`` matching the directory name of the area.

+--------------------+----------------------------------------------------------+
| Group              | Description                                              |
+====================+==========================================================+
| <name>             | Full set of tests for this area                          |
+--------------------+----------------------------------------------------------+
| <name>_<group>     | Tests for this area that are part of this group          |
|                    | e.g. gungho_developer or lfric_atm_spice                 |
+--------------------+----------------------------------------------------------+

