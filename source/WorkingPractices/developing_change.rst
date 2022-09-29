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

Commits to your branch should take the following form in their log messages:

.. code-block::

  #<ticket_number> - A useful message of what the commit entails

..
  Anyone know how to display the '#' symbol in Sphinx properly?

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
 * :ref:`kgo`
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

.. tip ::
  Searching the relevant documentation for words related to your change is often useful when
  deciding whether to update the documentation.

..
  Link to page here for updating UMDPs
  Link to page here for updating JULES docs.
  (JW: These can be added later if required, but I will leave it for now to get the rest of
  the change development section done. We can open an issue if required.)

.. _develop_metadata:

Input Variables, Rose metadata and upgrade macros
-------------------------------------------------

Sometimes the developer needs to alter model namelists and input variables.
A common reason is for the inclusion of a new piece of code which has to be
turned off by default.

If a developer changes the namelist inputs they are also expected to alter the
following areas of the code:

 * The inclusion of appropriate defensive checks.
 * Changes to Rose metadata.
 * Upgrade macros.

Defensive checks abort the model run if the user sets variables outside of
their expected range or a combination of variables that will lead to an error.
Most namelist modules contain a subroutine which performs this checking and
which can be modified.

The UM metadata can be found in the following location:

.. code-block::

  vnXX.Y_<_branch_name>/rose-meta/um-atmos/HEAD/rose-meta.conf

..
  Location of LFRic metadata needs adding and possibly centralization.

All new namelist variables need a new entry so that the metadata loads into the
Rose GUI for users to switch it on. Additionally, sometimes the metadata needs
to be modified without changing a namelist variable. Guidance for updating the
UM's metdata :ref:`is available <metadata_guidance>`.

.. important::
  All changes which alter namelists require an upgrade macro for them to
  work with the model.

Changes to the metadata which don't involve namelist changes may or may not
require an upgrade macro. If you are unsure whether a UM change needs an
upgrade macro, then run the following command on your branch:

.. code-block::

  rose stem --group=scripts

If all of the tests pass then there is no requirement to add an upgrade macro.
If any of the tests fail, then the developer should add a blank upgrade macro
which contains no upgrade commands but simply points the rose stem suite to
the new metadata.

..
  The above should probably be extended to LFRic eventually.

.. tip::
  When developing a change that updates the input and/or user interface,
  then repeatedly running/reverting the upgrade macro on the dev branch,
  or creating many test branches can be tiresome. Consider working up your
  change with the new options hard-coded in until such time as you are ready
  to connect up to the input for real.

.. important::
  If your development includes am upgrade macro, you **must** add the
  ``macro`` keyword to your ticket.

.. _develop_rosestem:

Rose stem suite changes
-----------------------

Periodically, the developer may wish to update the rose stem suite to add
a new change to protect their code. Configuration owners may also wish
to update the suite to ensure that important configurations are protected
by the rose stem suite.

.. warning::
  If you find that you need to update all the apps in the rose stem suite
  purely to get your change to work, you are probably doing something wrong.
  Most likey, you need an upgrade macro. See :ref:`develop_metadata` above.

.. _kgo:

Changes to answers/known good output (KGO)
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

.. _develop_diagnostics:

Diagnostic systems
------------------

The diagnostic systems vary between projects. Please follow the guidance
for whichever system you are developing.

**UM:** See :ref:`stash`.

**LFRic:** The LFRic diagnostic system is currently in development.
Please follow `the guidance here <https://code.metoffice.gov.uk/trac/lfric/wiki/GhaspSupport/Diagnostics_porting>`_
to make changes to the diagnostic system.

..
  JW: I guess once the system is finalised, then this should be included in this page?

..
  Do UKCA/SOCRATES/JULES have their own diagnostic systems and are they worth mentioning here?
  CASIM does not, but the MONC model which builds CASIM does; code is shared between them both.
