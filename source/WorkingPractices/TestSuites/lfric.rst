.. _lfric_test:

Testing LFRic
=============

LFRic testing is run with the following command from a working copy:

    .. code-block::

        make test-suite

-----

The minimum requirement for testing a branch that is to be sent for review is
that the system level developer tests pass on all the applications. These are
launched from make and utilise rose and cylc.

While developing your change, for expediency you may want to run the tests for
only some applications. This can be done by going into the directory of the
application before running the above command.

By default the command will run the develop test; other test groups exist.
In particular, you need to be confident that the nightly tests pass. These can
be run as follows:

    .. code-block::

            make test-suite SUITE_GROUP=nightly


It is also possible to select the platform to run on. Available options include
``meto-spice``, ``meto-xc40`` and ``meto-xcs``.

    .. code-block::

            make test-suite TEST_SUITE_TARGETS="meto-spice meto-xcs"

.. tip::

    For more details on LFRic testing including details of unit tests please
    visit the trac wiki
    `here <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/Testing>`_.

