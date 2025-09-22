.. _stash:

STASH [#f1]_
============

Information on every diagnostic available to the model is stored in a single
file named ``STASHmaster_A``, which is read into the model at the start of the
run.

The UM's ``STASHmaster_A`` and associated help text file
``STASHmaster-meta.conf`` are available in your branch at
``vnXX.Y_<branch_name>/rose-meta/um-atmos/HEAD/etc/stash/STASHmaster/``.

.. note::

    When running the UM rose stem suite, the suite will automatically use the
    ``STASHmaster_A file`` from your branch when testing your code.

The following principles apply when altering the STASHmaster:

..
  JW suggest need to include STASH entry guidance here. Maybe an issue for this would be useful?

* If you add a new diagnostic to the ``STASHmaster_A`` file then you **must**
  also add to the stash master help text in :ref:`stashmaster-meta`.
* If you are altering the stashmaster, this may be referred to the FFPP
  governance board by the sci/tech or code reviewers - see the STASH entry
  guidelines.
* If your change has new stash items or changed/added attributes as an option
  code, versions mask etc., then first you have to get them reserved and
  recorded (published) on the reservation web page STASH/ReservedCodes
* Note that every reservation should be linked to a ticket with the correct
  explanation and a milestone. This rule applies to all stash related tables
  placed on this page.
* Although reservations could be some kind of self-service, contact the section
  owner first nevertheless. This could help to organise new items
  (when possible) in some logical groups.
* For new option code numbers contact the STASH code owner.

.. note::

    Complete details of the STASH system (including the syntax used in the
    ``STASHmaster_A`` file) can be found in `UMDP C04
    <https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_C04.pdf>`__

.. _stashmaster-meta:

STASHmaster-meta.conf
---------------------

If you are adding a new UM STASH diagnostic you must also add help text to the
STASHmaster-meta.conf. This will provide others with help on your diagnostic.
You will need to identify the stash entry with a ``[stashmaster:code
(xyz)]`` section header, where the xyz is the stash code in the form ``section
number * 1000 + item number``.

Include a full name, any units and explanatory text. You should also add a
description field that matches the full name of the diagnostic. For example:

.. code-block::

    [stashmaster:code(1050)]
    description=NO2 Dry Deposition Rate (3D)
    help=NO2 Dry Deposition Rate (3D)
        =moles/s
        =
        =This is the total dry deposition flux of NO2 in each gridbox
        =
        =The sum of this deposition flux over all model gridboxes gives the total
        =number of moles of NO2 removed by this process per second in the
        =whole model.

This assists the model user in being able to find useful help text on their
diagnostic.


.. rubric:: Footnotes

.. [#f1] This is an acronym for 'Spatial and Temporal Averaging and Storage Handling'.
