Developing Your Change
======================
How a change is developed generally depends on the nature of the
change and the size of the code change: small code changes of just
a few lines can be written in minutes before being tested.
For anything longer and more complex, it is worth developing the
code in small sections or units, testing that each piece of code works
before committing back to the development branch. By following this
methodology, if one aspect of the code doesn't work, there is
always the option to ``fcm revert`` the local changes and quickly return
to a checkpoint in your development that did work.

.. tip::
  Before embarking on a medium-sized or significant model change,
  it is useful to have an appropriate coding plan in place.
  See :ref:`planning` for further details.

Code changes should conform to the coding standards of the project.
Remember to ensure that your changes are easy to read and follow, using
comments to explain what the code is doing.

The vast majority of changes will be based around a project's source
code. In addition, there are also a number of particular scenarios
which may also require action from the developer. Rarely, the developer
may alter one of these *without* modifying the source code.
These are as follows:

 * :ref:`develop_docs`
 * :ref:`develop_metadata`
 * :ref:`develop_rosestem`
 * :ref:`develop_kgo`
 * :ref:`develop_diagnostics`

.. note::
  **Remember: Develop, Test, Commit**

.. _develop_docs:

Scientific or technical documentation
-------------------------------------
Some projects have their own scientific and technical documentation.
Most notably:

* `The UM has documentation papers <https://code.metoffice.gov.uk/doc/um/latest/umdp.html>`_
* `JULES has a user guide and documentation <https://jules-lsm.github.io/latest/index.html>`_

..
  Any other documentations to be aware of?

Small changes and bug fixes rarely need documentation to be updated, but when new science is
added to a project, the documentation must be updated to ensure that it remains contemporary
with the code.

..
  Link to page here for updating UMDPs
  Link to page here for updating JULES docs.

.. _develop_metadata:

Rose metadata and upgrade macros
--------------------------------

.. tip::
  When developing a change that updates the input and/or user interface,
  then repeatedly running/reverting the upgrade macro on the dev branch,
  or creating many test branches can be tiresome. Consider working up your
  change with the new options hard-coded in until such time as you are ready
  to connect up to the input for real.

.. _develop_rosestem:

Rose stem suite changes
-----------------------

Blah

.. warning::
  If you find that you need to update all the apps in the rose stem suite
  purely to get your change to work, you are probably doing something wrong.
  Most likey, you need an upgrade macro. See :ref:`develop_metadata` above.

.. _develop_kgo:

Changes to answers/known good output (KGO)
------------------------------------------

Sometimes, a KGO update may be required to add a new job to the test suite.

.. important::
  If your development includes updates to the KGO, you **must** add the
  ``kgo`` keyword to your ticket so that your CodeSys reviewer knows to
  install the new KGO. Failure to do so may lead to delays in your
  ticket making the project's trunk.

.. _develop_diagnostics:

Diagnostic systems
------------------

The diagnostic systems vary between projects. Please follow the guidance
for whichever system you are developing.

**UM:** The UM outputs diagnostics using an old, but reliable and flexible
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
  JW suggest need to include STASH entry guidance.

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

**LFRic:** The LFRic diagnostic system is currently in development.
Please follow `the guidance here <https://code.metoffice.gov.uk/trac/lfric/wiki/GhaspSupport/Diagnostics_porting>`_
to make changes to the diagnostic system.

..
  JW: I guess once the system is finalised, then this should be included in this page?

..
  Do UKCA/SOCRATES/JULES have their own diagnostic systems and are they worth mentioning here?
  CASIM does not, but the MONC model which builds CASIM does; code is shared between them both.


.. rubric:: Footnotes

.. [#f1] This is an acronym for 'Spatial and Temporal Averaging and Storage Handling'.
