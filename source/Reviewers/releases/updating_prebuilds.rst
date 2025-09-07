.. _updating_prebuilds:

Mid-Release Prebuilds
=====================

These are instructions for updating UM prebuilds mid-way through a release
cycle. Reasons for doing this include new builds being added, changes that
mean the old prebuilds break (sometimes new/deleted files can do this), or
because the prebuilds are so out of date they don't particularly help. An
example ticket doing this can be seen in `UM:#7903
<https://code.metoffice.gov.uk/trac/um/ticket/7903>`_.

To update prebuilds:

* Open a new UM ticket, create a branch and check it out.
* In ``rose-stem/rose-suite.conf``:

    * Update the ``BASE_UM_REV`` variable to the latest version of the UM
      trunk.
    * Update any other ``BASE_*_REV`` variables if those trunks have more
      recent commits that the revision listed.

* In ``rose-stem/site/meto/variables.rc``:

    * Update the prebuilds paths with the name, ``rXXXXXX_prebuilds`` where
      ``XXXXXX`` should match the ``BASE_UM_REV`` variable from earlier.

* Commit these changes to the branch.
* Login as ``umadmin`` and check out the branch (this will need to be from the
  mirror, so ensure it has updated).
* Install the prebuilds, first on azure spice and EXAB, then on the EXCD and
  finally the EXZ. Ensure the name of the suite matches the path that was set
  in the ``variables.rc`` file.

.. code-block:: shell

    export CYLC_VERSION=7

    # EXAB and Azure Spice
    rose stem --group=prebuilds --source=fcm:um.xm_tr@XXXXXX \
        --name=rXXXXXX_prebuilds --config=./rose-stem -S MAKE_PREBUILDS=true \
        -S USE_EXAB=true

    # EXCD
    rose stem --group=ex1a_fcm_make,ex1a_fcm_make_portio2b \
        --source=fcm:um.xm_tr@XXXXXX --name=rXXXXXX_prebuilds \
        --config=./rose-stem -S MAKE_PREBUILDS=true -S USE_EXCD=true

    # EXZ
    rose stem --group=ex1a_fcm_make,ex1a_fcm_make_portio2b \
        --source=fcm:um.xm_tr@XXXXXX --name=rXXXXXX_prebuilds \
        --config=./rose-stem -S MAKE_PREBUILDS=true -S USE_EXZ=true

* Finally, ensure that prebuilds are enabled in ``rose-stem/rose-suite.conf``
  and have the ticket reviewed and committed.
