.. _lfric_core_test:

Testing LFRic Core
==================

.. note::

    At the LFRic Apps vn2.0 release, the cylc7 LFRic Core suite was deprecated
    and the make test-suite functionality removed. Only the cylc8 suite is now
    maintained.

LFRic testing is launched with Cylc8 rose-stem commands (as in eg. LFRic
Apps):

.. code-block:: shell

    export CYLC_VERSION=8
    rose stem --group=developer
    cylc play <NAME-OF-SUITE>

-----

The minimum requirement for testing a branch that is to be sent for review is
that the system level developer tests pass on all the applications. These are
launched from make and utilise rose and cylc.

While developing your change, for expediency you may want to run the tests for
only some applications. This can be done by changing the group you run, eg
``--group=simple_diffusion``.

The command above will launch the developer suite. You can include slightly
more testing if required by running ``--group=all`` instead (this includes the
developer suite).

It is also possible to run on a single platform, eg. ``--group=ex1a``. To
select which meto EX machine is used, add ``-S USE_EX<AB/CD/Z>``.

.. tip::

    For more details on LFRic testing including details of unit tests please
    visit the `LFRic testing trac wiki page
    <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/Testing>`__.

