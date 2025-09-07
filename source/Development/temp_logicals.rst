.. _templogicals:

Temporary Logical Variables
===========================

Temporary logical variables are intended to add a layer of protection in
instances where a *bug fix* produces a **significant** change in results in a
scientific configuration. The purpose of the temporary logical is to maintain
results in scientific configurations. However, the bug fix could either be due
to a scientific or a technical issue. Temporary logicals are used primarily
for two reasons:

#. To maintain consistency in an important scientific configuration
   (e.g. global/regional atmosphere/land) when upgrading between model
   versions. If the logical was not used then different model versions may
   lead to very different scientific answers.

#. To give the configuration owner time to assess the impact of a significant
   change in answers on their configuration. The usual release cycle window is
   often too short to fully assess the impact of anything other than a small
   change.

Neither of these statements suggest that the fix shouldn't be included --- in
fact the opposite is true. The decision as to whether to include a temporary
logical normally rests with the configuration owner, but with guidance from
the CodeSys reviewer and the Simulation Systems and Deployment team. In such
cases, the following guidance is followed:

* Essential bug fixes (e.g. something which would on occasions cause the model
  to crash) should be switched on by default and would **not** have a
  temporary logical.

  * This includes any bug fixes which restores bit comparison across different
    processor decomposition where it has been previously broken.

* Any bug fix which does not lead to a change in answers should be switched on
  by default (not with a temporary logical).

* Small changes (within the noise) can usually be included as a :ref:`kgo`
  update and would **not** usually have a temporary logical associated with
  them.

* Anything which has a large impact (especially on key variables used for
  weather and climate) and which extends beyond the 'noise' of the
  model **would be expected to include a temporary logical**.

* There may be a few specific cases, where only certain platforms or builds are
  affected due to a technical bug fix.

.. important::

    There isn't a precise definition of what 'being in the noise' consists of,
    so the configuration owner should always be contacted in the first
    instance to provide guidance of what is or is not important to that
    particular configuration.

.. important::

    Remember that any new piece of science code or new scientific option would
    normally be switched off by default by a variable in the most appropriate
    scientific namelist. A temporary logical would not be used in this
    instance. See :ref:`input variables <inputs>` for further details.

Adding a temporary logical to the code base
-------------------------------------------

When adding a new temporary logical, the developer must protect **only** the
portion of code which changes answers by placing an `IF` statement around it,
e.g.

.. code-block:: fortran

    IF (l_fix_something) THEN

    ... piece of code which changes answers ...

    END IF ! l_fix_something

The new logical should be added in a specified subroutine for short-term fixes
and **not** in a usual scientific or technical namelist. The location of the
temporary logical routine varies by repository, with not all repositories
requiring their own temporary logical subroutine. Details are as follows:

.. tab-set::

    .. tab-item:: UM

        ``src/control/misc/science_fixes_mod.F90``

    .. tab-item:: JULES

        ``src/control/shared/jules_science_fixes_mod.F90``

    .. tab-item:: LFRic Apps

        Currently reads ``science_fixes_mod.F90`` (see UM) into
        ``um_physics/source/support/um_physics_init_mod.f90``

    .. tab-item:: UKCA/CASIM/SOCRATES

        No temporary logical routine currently in place for these projects.
        Consult with Code Owners or check the UM ``science_fixes_mod.F90`` for
        existing temporary logicals.

.. hint::

    By default, the logical should be set to ``.false.``, with the fix
    switched **off**, unless instructed otherwise by the Configuration Owner.

The developer should remember to add the variable to the namelist, including
any namelist printing and reading subroutines present in the module. In
addition, they should also include a warning for when the fix is not included
in a configuration. Examples of the various components can be found by
examining existing variables in the subroutines listed in the table above.

An upgrade macro and Rose metadata will be required to add the temporary
logical into the GUI and make it available to model users. See :ref:`inputs`
for further information. UM developers are also expected to fill in a
`temporary fixes summary template
<https://code.metoffice.gov.uk/trac/um/wiki/PageTemplates/TempFixesSummary>`__
and `the temporary logical table
<https://code.metoffice.gov.uk/trac/um/wiki/TempUMlogicals>`__ prior to the
review process.

..
    Note: Have we got a page on upgrade macros? (i.e. brief instructions on how
    to write one?) I wonder if we need one - I can only see a discussion on
    what they are and how to apply one!

    Should the temporary logical page and the summary wiki page be extended to
    all repositories? I can't see one for JULES at the moment. This is
    something to think about making consistent.


After the release cycle
-----------------------

Normally, configuration owners would be expected to switch on all temporary
logicals present as part of developing their latest configuration. This
includes any which do not impact their configuration, as it allows them to be
retired from the code base. Depending on when the next configuration is being
developed, this could be some time after the code is released.

.. note::

    **Very rarely**, switching on a bug fix may have an undesired impact (e.g.
    it leads to the discovery of a bug elsewhere in the code). In these cases,
    the configuration owner may keep the temporary logical set to ``.false.``
    until the issue is resolved and may consult with the Code Owners and the
    developers of the fix for further guidance. This does not imply that the
    bug fix wasn't sensible in the first place!

Each temporary logical has a review and retention period attached to it. Once
the fix is included within the various configurations it affects, the
temporary logical should be removed from the code base.

.. important::

    Prior to a ticket containing a temporary logical being committed to the
    trunk, the developers is expected to open a new ticket which removes the
    logical after a fixed period. This acts as an memory aid that the logical
    needs to be removed in due course.
