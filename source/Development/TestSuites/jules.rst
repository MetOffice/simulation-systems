Testing JULES
=============

JULES testing is run with the following command from a working copy:

.. code-block::

    rose stem --group=all --new

-----

The JULES rose stem testing includes a range of builds using a variety of
compilers, several configurations, and rose-ana tasks to check the output.

The output is checked for correctness both by comparing the output to a set of
stored :ref:`KGO files <kgo>`.

.. note::

    If there are JULES changes to shared science code or
    :ref:`jules-shared<shared-namelists>` metadata then these changes
    will need to be tested :ref:`with the UM<um_testing>` and
    :ref:`with LFRic Apps<lfric_apps_test>`. If you have access to LFRic, the
    :ref:`traclog` will state whether LFRic testing is required based on the
    branch diff. If you do not have LFRic access, this testing will need to
    be completed by your Met Office contact.

    See :ref:`multirepo` for details on how to carry out this testing.

    .. important::
        For **jules-shared** changes, when LFRic testing, the
        changes need to be manually synced to the LFRic location. When UM
        testing, this is not required as **jules-shared** is imported from the
        JULES branch.

Below is a (by no means comprehensive) set of groups that you may wish to use
on Met Office systems.

+--------------------+----------------------------------------------------------+
| Group              | Description                                              |
+====================+==========================================================+
+--------------------+----------------------------------------------------------+
| all                | The complete test suite. This is run automatically       |
|                    | every night and monitored by the SSD team. All           |
|                    | :ref:`KGO <kgo>` changing tickets need to run this group.|
+--------------------+----------------------------------------------------------+
+--------------------+----------------------------------------------------------+
| loobos             | A set of tests to exercise these science areas.          |
|                    |                                                          |
| gswp2              |                                                          |
|                    |                                                          |
| eraint             |                                                          |
|                    |                                                          |
| imogen             |                                                          |
+--------------------+----------------------------------------------------------+
| xc40/linux         | All tests designed to run on the named platform.         |
+--------------------+----------------------------------------------------------+
| scripts            | All of the auxillary scripts that are designed to check  |
|                    | the code standards in ways that aren't tested by the     |
|                    | compiler.                                                |
+--------------------+----------------------------------------------------------+
