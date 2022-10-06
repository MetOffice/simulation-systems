.. _kgo:

Known Good Output
------------------------------------------

Normally it is to be expected that code changes regress (i.e. all prognostic
variables **and** diagnostics maintain the same answers with your code included
but switched off).

The most common reason why a code change does not regress is when a bug is
discovered and fixed.

.. important::
  Where a change in answers occurs, the developer must contact the configuration
  owners of all affected configurations. See :ref:`approvals` for details.

Configuration owners will review the change and will either accept the change
as it is, or will request the use of a temporary variable to switch the
change off. See :ref:`templogicals` for details of this process.

Sometimes, a KGO update may also be required to simply add a new job to the
test suite or to port the rose stem suite to new HPC architecture.

.. important::
  If your development includes updates to the KGO, you **must** add the
  ``kgo`` keyword to your ticket so that your CodeSys reviewer knows to
  install the new KGO. Failure to do so may lead to delays in your
  ticket making the project's trunk.

.. toctree::
    :hidden:

    temp_logicals