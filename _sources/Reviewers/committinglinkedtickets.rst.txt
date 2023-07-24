.. _committinglinkedtickets:

Committing Linked Tickets
=========================

.. div:: sd-fs-5

    First, checkout, merge and test all branches. Tests for each branch can run simultaneously, but give the Jules-ticket as a source to the UM, and give the UM and Jules tickets as sources to LFRic:

.. div:: sd-fs-5

    **1. Checkout trunks, merge in tickets and test:**

.. tab-set::

    .. tab-item:: Jules

        Check out Jules trunk and merge:

        .. code-block:: RST

            fcm co fcm:jules.x_tr@HEAD your_directory_name
            cd your_directory_name
            fcm merge fcm:jules.x_br/dev/dev_name/branch_name
            fcm conflicts

        The before and after tag always cause conflicts in the versions.py file and need manually adjusting.
        If this is the only conflict, you can edit with the GUI or manually afterwards. To edit manually, accept changes in the pop-up GUI window and put “y” in terminal when prompted.
        Manually go to the “versions.py” file, add the old class back in/edit the file so both the old and new class are in, and change the before tag to be equal to the previous update’s after tag.

       .. dropdown:: Upgrade macros, new rose stem app or KGO update?

            Upgrade macros:

            .. code-block:: RST

                ./bin/upgrade_jules_test_apps vnX.X_txxx

       Test the Jules ticket:

        .. code-block:: RST

            rose stem --group=scripts
            rose stem --group=all


    .. tab-item:: Jules docs

        Checkout Jules doc trunk and merge:

        .. code-block:: RST

            fcm co fcm:jules_doc.x_tr@HEAD jules_doc
            cd jules_doc
            fcm merge fcm:jules_doc.x_br/dev/dev_name/branch_name

        Check the documentation builds correctly:

        .. code-block:: RST

            module load scitools
            cd docs/user_guide
            make clean html
            firefox build/html/index.html &

            make clean latexpdf
            evince build/latex/JULES_User_Guide.pdf &


    .. tab-item:: UM

        Checkout the UM trunk, merge with the ticket, check for conflicts:

        .. code-block:: RST

            fcm co fcm:um.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:um.x_br/dev/dev_name/branch_name
            fcm cf

        The before and after tag always cause conflicts in the versions.py file and need manually adjusting.
        If this is the only conflict, you can edit with the GUI or manually afterwards. To edit manually, accept changes in the pop-up GUI window and put “y” in terminal when prompted.
        Manually go to the “versions.py” file, add the old class back in/edit the file so both the old and new class are in, and change the before tag to be equal to the previous update’s after tag.

        Update the test suite for an upgrade macro, where *xx.x* is the UM version and *xxxxx* is the AFTER_TAG of the upgrade macro:

        .. code-block:: RST

            ~frum/bin/update_all.py /path/to/working/copy/of/trunk --um=xx.x_xxxxx

        Test UM with a source pointing to Jules, to include the Jules updates in the testing:

        .. code-block:: RST

            rose stem --group=developer,jules --source=. --source=/path/to/merged/jules/working/copy

    .. tab-item:: LFRic

        Checkout the UM trunk, merge with the ticket, check for conflicts:

        .. code-block:: RST

            fcm co fcm:lfric.x_tr your_lfric_trunk_name
            cd your_lfric_trunk_name
            fcm merge fcm:lfric.x_br/dev/dev_name/branch_name
            fcm cf

        Navigate into: chosen_name/lfric atm/fcm-make/parameters.sh and temporarily change the UM and Jules sources to:

        .. code-block:: RST

            vldxxx:/path/to/um _ticket
            vldxxx:/path/to/ jules_ticket

        Back in the terminal, test the changes:

        .. code-block:: RST

            cd lfric_atm
            module use /data/users/lfric/modules/modulefiles.rhel7
            module load environment/lfric/intel
            make test-suite


.. div:: sd-fs-5

    **2. Committing tickets**

N.B. Tickets must be committed in the correct order: Jules, then UM, then LFRic:

1) Commit Jules ticket (and then Jules documentation)

.. code-block:: RST

    fcm commit

2) Put JULES revision number into UM rose-stem/rose-suite.conf

.. code-block:: RST

    cd ticket_folder/rose-stem/rose-suite.conf

.. code-block:: RST

    BASE_JULES_REV='xxxxx'

3) Commit UM ticket

.. code-block:: RST

    fcm commit

4) Put JULES and UM revision numbers into LFRic’s lfric_atm/fcm-make/parameters.sh file, and remove paths to working copies in that file.

.. code-block:: RST

    export um_rev=xxxxx
    export jules_rev=xxxxxx

    export um_sources=
    export jules_sources=


5) Commit LFRic ticket

.. code-block:: RST

    fcm commit

Now remember to:  Update the ticket with the revision number the change was merged back into the trunk at, e.g. [500] for revision 500, and comment whether the change is expected to alter results or not and update the ticket status to committed.

