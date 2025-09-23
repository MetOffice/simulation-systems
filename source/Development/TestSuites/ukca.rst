Testing UKCA
============

Changes in UKCA that touch `src/science` or `src/control/core` must be tested
with both the UM and LFRic by following the :ref:`linked tickets guidance
<multirepo>`.

For further guidance on testing and working with UKCA, including standard
suites and box models see the `UKCA trac wiki
<https://code.metoffice.gov.uk/trac/ukca/wiki/WorkingPractices>`__.

There also exists a small UKCA rose-stem suite, which contains a code styling
check. This can launched from the top directory of a local clone by running,

.. code-block::

    cylc vip -z g=scripts -n <name/of/suite> ./rose-stem
