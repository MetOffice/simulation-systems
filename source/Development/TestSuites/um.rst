.. _um_testing:

Testing the UM
==============

UM testing is run with the following command from a working copy:

.. code-block:: shell

    rose stem --group=developer --new

-----

The UM rose stem testing includes a range of builds using a variety of
compilers, both reconfiguration and atmosphere tests, and rose-ana tasks to
check the output. As well as testing the UM, there are also tests for
createBC, mule, Shumlib and a variety of other utilities.

The output is checked for correctness both by comparing the output to a set of
stored :ref:`KGO files <kgo>`, but also by running different processor
decompositions and comparing the results, and by looking at the outputs of
runs that have stared from a cold start and those that have had their state
saved and restarted.

.. tip::

    The UM rose-stem suite can take a long time to run. When in the initial
    stages of developing a change choosing a single compile and run task to
    test with may be helpful. e.g.

    .. code-block:: shell

        rose stem --group=xc40_gnu_um_rigorous_omp-n48

.. note::

    Changes to code in src/atmosphere may require
    :ref:`testing with LFRic Apps<lfric_apps_test>`.If you have access to LFRic, the
    :ref:`traclog` will state whether LFRic testing is required based on the
    branch diff. If you do not have LFRic access, this testing will need to
    be completed by your Met Office contact.

    See :ref:`multirepo` for details on how to carry out this testing.

Below is a (by no means comprehensive) set of groups that you may wish to use
on Met Office systems. Note that there is a lot of overlap between these
groups, and that you can specify more than one at once, e.g.
``--group=developer,jules,ukca``.

+--------------------+----------------------------------------------------------+
| Group              | Description                                              |
+====================+==========================================================+
| developer          | Standard group of tests that every change is expected    |
|                    | to pass before commit. It is a useful checkpoint during  |
|                    | development.                                             |
+--------------------+----------------------------------------------------------+
| nightly            | More thorough testing group. This includes everything in |
|                    | developer plus some longer and more complex tests. It is |
|                    | run automatically every night and monitored by the SSD   |
|                    | team.                                                    |
+--------------------+----------------------------------------------------------+
| all                | The complete test suite, including all longer runs and   |
|                    | less commonly used utilites. This is run automatically   |
|                    | every week and monitored by the SSD team. All            |
|                    | :ref:`KGO <kgo>` changing tickets need to run this group.|
+--------------------+----------------------------------------------------------+
+--------------------+----------------------------------------------------------+
| rigorous_compile   | A build-only group that will sense-check the code for a  |
|                    | wider range of compile errors than the usual builds.     |
+--------------------+----------------------------------------------------------+
| jules              | A set of tests that exercise the UM/JULES interface.     |
+--------------------+----------------------------------------------------------+
| casim              | A set of tests that exercise the UM/CASIM interface.     |
+--------------------+----------------------------------------------------------+
| ukca               | A set of tests that exercise the UM/UKCA interface.      |
+--------------------+----------------------------------------------------------+
| recon              | A set of tests that exercise the reconfiguration system. |
+--------------------+----------------------------------------------------------+
| coupled            | A set of tests that exercise the coupled and hybrid code.|
+--------------------+----------------------------------------------------------+
| uk_lams            | Testing for the limited area models                      |
+--------------------+----------------------------------------------------------+
| xc40/spice         | All tests designed to run on the named platform.         |
+--------------------+----------------------------------------------------------+
| scripts            | All of the auxillary scripts that are designed to check  |
|                    | the code standards in ways that aren't tested by the     |
|                    | compiler.                                                |
+--------------------+----------------------------------------------------------+

.. tip::

    The `standard jobs
    <https://code.metoffice.gov.uk/trac/um/wiki/StandardJobs>`__ page for each
    release includes details of which of ``developer``, ``nightly`` and
    ``all`` a configuration is tested at.


Monsoon
-------

As of UM vn13.9, the UM is able to run on Monsoon3, the latest version hosted
by the Meto EX machines. To run on here, users should follow the process laid
out in the Monsoon User Guide. This involves logging onto the ``cazccylc1``
server to launch jobs.

The UM test suite is set up to run on Monsoon with Cylc 8 by running,

.. code-block:: shell

    rose stem --group=ex1a
    cylc play <name-of-suite>

This will launch all ex1a jobs that are available to run on Monsoon.

For running suites on Monsoon, a few environment variables must be set for the
builds to complete:

* ``EX_UMDIR_OVERRIDE`` - this needs to be set to ``/projects/metoff/umdir``
* ``ECCODES_VERSION`` - this needs to be set to ``eccodes-2.34.0``

