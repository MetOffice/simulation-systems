.. _kgo:

Known Good Output (KGO)
=======================

Normally it is to be expected that code changes regress (i.e. all prognostic
variables **and** diagnostics maintain the same answers with your code
included but switched off).

Usually, a code change does not regress when either a bug is a discovered and
fixed, or a science area is introduced or enhanced. Sometimes, a KGO update
may also be required to simply add a new job to the test suite or to port the
rose stem suite to new HPC architecture.

**LFRic** KGO checksums are stored in the repository. As such with LFRic
tickets the expectation is that you, as the developer, will include updated
KGO files as part of your branch.

**UM and JULES** KGO output files are stored outside of the repository. Access
to this area is restricted to members of the Simulation Systems and Deployment
Team and they will update the KGO files to include your new answers as part of
the commit process.


KGO Update Process
------------------

Getting the process right for KGO changing tickets significantly helps get such
changes onto the trunk. When preparing your change for review:

1. Run the ``all`` rose-stem group in order to make sure that all
   changes to answers have been found.

   * Include the :ref:`trac.log <traclog>` output from this testing in your
     ticket summary.

2. Add the ``kgo`` keyword to your ticket.

.. tab-set::

    .. tab-item:: LFRic Apps

        3. Update the checksum files on your branch. To do so run rose stem and
           then the following from the head of your working copy

            .. code-block:: shell

                python3 ./rose-stem/bin/update_branch_kgos.py \
                    -s <suite name/runX> -w <path to working copy>

            .. note::

                This script requires at least python 3.9. This can be achieved
                on Met Office machines by running ``module load scitools``

        4. If you are adding new checksums, ``git add`` the files.

        5. You can check the new kgo updated properly by retiggering tasks in
           the test suite. First retrigger ``export-source``, and then when
           complete ``export-source_ex1a`` if new checksums are present there
           (there is no need to retigger spice). You may need to change the
           maximum window extent of the gui in order to see the succeeded
           tasks. Now you can retrigger the failed checksums - these should now
           pass if the kgo was updated in the working copy correctly.

        6. The changes in answers should be science reviewed by someone
           familiar with the failing tests - if unsure then start with the Code
           Owner for the affected application.


        Once all the above is in place and the science and code reviews have
        been completed then the Code Reviewer will merge your change to the
        head of trunk. If there are merge conflicts in the checksum files then
        the reviewer will repeat step 3 to refresh these files. Your change is
        then committed to trunk.

    .. tab-item:: UM & JULES

        3. Contact the configuration owners of all affected configurations. A
           list is provided in the trac.log . See :ref:`approvals` for details.

           Configuration owners will review the change and will either accept
           the change as it is, or will request the use of a temporary
           variable to switch the change off. See :ref:`templogicals` for
           details of this process.

        Once all of the above is in place and the science and code reviews have
        been completed the Code Reviewer will merge the branch to the head of
        trunk, run the tests that have changed answers and use those results
        to install KGO files to the filesystem. Your change is then committed
        to trunk.

.. tip::

    More details on the KGO update proceedures for all repositories can be
    found on the :ref:`How to Commit page<kgo_instructions>`.

.. toctree::
    :hidden:

    temp_logicals
