.. _kgo:

Known Good Output (KGO)
=======================

Normally it is to be expected that code changes regress (i.e. all prognostic
variables **and** diagnostics maintain the same answers with your code included
but switched off).

Usually, a code change does not regress when either a bug is a
discovered and fixed, or a science area is introduced or enhanced. Sometimes,
a KGO update may also be required to simply add a new job to the
test suite or to port the rose stem suite to new HPC architecture.

**LFRic** KGO checksums are stored in the repository. As such with LFRic tickets
the expectation is that you, as the developer, will include updated KGO files
as part of your branch.

**UM and JULES** KGO output files are stored outside of the repository. Access
to this area is restricted to members of the Simulation Systems and Deployment
Team and they will update the KGO files to include your new answers as part of
the commit process.

.. important::
  Getting the process right for KGG changing tickets significantly
  helps get such changes onto the trunk. Notably:

  * You must contact the configuration owners of all affected configurations.
    See :ref:`approvals` for details.

  * You must add the ``kgo`` keyword to your ticket.

  * You mush run the ``all`` rose-stem group in
    order to make sure that all changes to answers have been found. Include
    the :ref:`trac.log <traclog>` output from this testing in your ticket summary.


Configuration owners will review the change and will either accept the change
as it is, or will request the use of a temporary variable to switch the
change off. See :ref:`templogicals` for details of this process.




.. tip::
    For LFRic Apps it is possible to update the checksum files on your branch to
    aid with testing and development. To do so run the rose-stem suite as described
    to cover all failing tests, then run the following from your working copy

    .. code-block::

        python3 ./rose-stem/bin/update_branch_kgos.py -s <suite name> -w <path to working copy>

    .. note::
        This script requires at least python 3.9. This can be achieved on
        Met Office machines by running ``module load scitools``

    More details on the KGO update proceedures for all repositories can be found
    :ref:`here <kgo_instructions>`.

.. toctree::
    :hidden:

    temp_logicals