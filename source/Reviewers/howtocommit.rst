.. _howtocommit:

How To Commit
=============

.. div:: sd-fs-5

    **1.** Linked Tickets?

If this ticket has linked tickets in JULES (and/or SOCRATES, AUX etc.), commit those first then update the “HOST_SOURCE_JULES” or “HOST_SOURCE_SOCRATES” etc variables in the UM rose-stem/rose-suite.conf file to include JULES/Socrates etc revision number.

.. dropdown:: More details

    Link to "reviewing linked tickets page".
    :ref:`committinglinkedtickets`


.. div:: sd-fs-5

    **2.** Checkout the trunk, merge with the ticket, check for conflicts:

.. tab-set::

    .. tab-item:: UM

        .. code-block:: RST

            fcm co fcm:um.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:um.x_br/dev/dev_name/branch_name
            fcm cf

    .. tab-item:: UM docs

        .. code-block:: RST

            fcm co fcm:um_doc.x_tr chosen_name
            cd chosen_name
            fcm merge fcm:um_doc.x_br/dev/dev_name/branch_name
            fcm cf


.. div:: sd-fs-5

    **3.** Test:

.. tab-set::

    .. tab-item:: UM

        Run any necessary testing; at the very least run this group:

        .. code-block:: RST

            rose stem --group=debug_compile

    .. tab-item:: UM docs

        Check the documentation builds correctly:

        .. code-block:: RST

            module load scitools
            make clean html
            firefox build/html/index.html

            make clean latexpdf
            evince build/latex/JULES_User_Guide.pdf &


.. div:: sd-fs-5

    **4.** If any changes need to be tested with **LFRic** as well, checkout LFRic trunk, change UM parameters and test:

.. dropdown::    **See LFRic steps**

    .. code-block:: RST

        fcm co fcm:lfric.x_tr chosen_name

    Navigate into: *chosen_name/lfric_atm/fcm-make/parameters.sh* and set the um_source:

    .. code-block:: RST

        um_sources=fcm:um.xm_br/dev/dev_name/branch_name

    From inside *chosen_name/lfric_atm* run:

    .. code-block:: RST

        module use /data/users/lfric/modules/modulefiles.rhel7
        module load environment/lfric/intel
        make test-suite


.. div:: sd-fs-5

    **5.** Do the changes: include any **meta-data** or upgrade **macro** changes, a new **rose stem app**, a new **temporary logical**, need a new **KGO** (if the change alters answers), add a **namelist** to an app, or change **build configs**? If so, follow these extra steps:

.. dropdown:: See steps

    extra steps here


.. div:: sd-fs-5

    **6.** Review the changes:

.. code-block:: RST

    fcm diff -g

.. div:: sd-fs-5

    **7.** Commit:

.. code-block:: RST

    fcm commit

.. dropdown:: More details

    **Commit message:** ``#ticket_number: Author : Reason for the change : ticket_type : code_area : regression : severity``

    E.g. ``#80 : lukeabraham : ticket name : task : technical : regression : minor``

    “Author” should be in the format e.g. ``andymalcolm`` - see list of authors here: `UserList <https://code.metoffice.gov.uk/trac/home/wiki/UserList/>`_

    If you mess up the commit log message, run this command and save to update the message:

    .. code-block:: RST

        fcm propedit --revprop svn:log -r xxxxxx fcm:um.x_tr

:ref:`code_review`

:ref:`committinglinkedtickets`
