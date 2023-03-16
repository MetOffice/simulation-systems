.. _howtocommit:

How To Commit
=============

.. div:: sd-fs-5

    **1. Linked Tickets?**

If this ticket has linked tickets in JULES (and/or SOCRATES, AUX etc.), commit those first then update the “HOST_SOURCE_JULES” or “HOST_SOURCE_SOCRATES” etc variables in the UM rose-stem/rose-suite.conf file to include JULES/Socrates etc revision number.

.. dropdown:: More details

    Link to "reviewing linked tickets page".

.. div:: sd-fs-5

    **2. Checkout the trunk, merge with the ticket, check for conflicts:**

.. tab-set::

    .. tab-item:: UM

        .. code-block:: RST

            fcm co fcm:um.x_tr chosen_name
            fcm merge fcm:um.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: UM docs

        .. code-block:: RST

            fcm co fcm:um_doc.x_tr chosen_name
            fcm merge fcm:um_doc.x_br/dev/dev_name/branch_name
            fcm cf

.. div:: sd-fs-5

    **3. Run any necessary testing including:**

.. tab-set::

    .. tab-item:: UM

        .. code-block:: RST

            rose stem --group=debug_compile

    .. tab-item:: UM docs

        .. code-block:: RST

            module load scitools
            make clean html
            firefox build/html/index.html

            make clean latexpdf
            evince build/latex/JULES_User_Guide.pdf &

