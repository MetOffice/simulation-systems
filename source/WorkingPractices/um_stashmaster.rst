.. _stash:

Changes to the UM's STASH system
================================

The UM outputs diagnostics using an old, but reliable and flexible
system named STASH [#f1]_ . Information on every diagnostic available to the
model is stored in a single file named ``STASHmaster_A``, which is read into
the model at the start of the run.

The UM's ``STASHmaster_A`` and associated help text file ``STASHmaster-meta.conf``
are available in your branch at
``vnXX.Y_<branch_name>/rose-meta/um-atmos/HEAD/etc/stash/STASHmaster/``.

.. note::
  When running the UM rose stem suite, the suite will automatically use the
  ``STASHmaster_A file`` from your branch when testing your code.

The following principles apply when altering the STASHmaster:

..
  JW suggest need to include STASH entry guidance here. Maybe an issue for this would be useful?

* If you add a new diagnostic to the ``STASHmaster_A`` file then you **must** also add to the stash master help text in ``STASHmaster-meta.conf``.
* If you are altering the stashmaster, this may be referred to the FFPP governance board by the sci/tech or code reviewers - see the STASH entry guidelines.
* If your change has new stash items or changed/added attributes as an option code, versions mask etc., then first you have to get them reserved and recorded (published) on the reservation web page STASH/ReservedCodes 
* Note that every reservation should be linked to a ticket with the correct explanation and a milestone. This rule applies to all stash related tables placed on this page.
* Although reservations could be some kind of self-service, contact the section owner first nevertheless. This could help to organise new items (when possible) in some logical groups.
* For new option code numbers contact the STASH code owner.

.. note::
  Complete details of the STASH system (including the syntax used in the
  ``STASHmaster_A`` file) can be found in
  `UMDP C04 <https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_C04.pdf>`_


.. rubric:: Footnotes

.. [#f1] This is an acronym for 'Spatial and Temporal Averaging and Storage Handling'.
