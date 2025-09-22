Rose Stem Suite
===============

Change to the Rose Stem Suite in Git
------------------------------------

.. _github_testing:

With the move to git and github, the test suites of the Simulation Systems
repositories will no longer use the rose-stem infrastructure, instead becoming
purely Cylc workflows. The only impact on the end user will be a change to the
commands required to launch the test suite. The contents of the test suite and
the process to add new tests will remain unchanged. The test suite
infrastructure will continue to live in a ``rose-stem`` directory, and we will
continue referring to the test suite as the ``rose-stem`` suite in these working
practices.

Running the rose-stem suite will now directly call cylc commands with the
following syntax,

* ``cylc vip`` - This will install and launch the test suite. If desired, it
  can be replaced with separate ``install`` and ``play`` commands which would
  needto be run separately.
* ``-z g=`` or ``-z groups=`` - This sets the test suite groups to run, and
  takes a comma separated list of groups. For example, ``-z g=developer,
  lfric_atm`` will run the ``developer`` and ``lfric_atm`` groups.
* ``-S VALUE=SETTING`` - these options behave as they did before, and can be
  added to the ``cylc vip`` command. See the table below for some suggestions.
* ``-S USE_MIRRORS=`` - An example of the above settings, this is newly added
  with the git migration. By default this is ``false`` and remote github
  repositories will be accessed via ssh. If set to ``true``, local github
  mirrors will be used instead. This is recommended particularly for shared
  accounts.
* ``-n name_of_suite`` - The new test suites will name themselves after the
  directory containing the test suite. Unfortunately this is always
  ``rose-stem`` so it is recommended to give the suite a name using this option.
* ``/path/to/rose-stem`` - The path to the rose-stem directory must be specified
  if not launching from in that directory.

For example,

.. code-block::

    cylc vip -z g=developer -S USE_MIRRORS=true -n my_rose_stem_suite ./rose-stem

will launch the test suite with the ``developer`` group, using the github
mirrors and naming it ``my_rose_stem_suite``.

``-S`` Options (non-exhaustive):

* ``-S USE_MIRRORS=true`` - Use local github mirrors instead of ssh.
* ``-S USE_HEADS=true`` - Use the head of the default branch for the github
  source, only intended for usage in nightly testing.
* ``-S USE_EX[AB/CD/Z]=true`` - MetOffice only, specify the host machine for
  EX1A jobs.
* ``-S HOUSEKEEPING=true`` - Stop housekeeping tasks from running.

Adding to the Rose Stem Suite
-----------------------------

All new changes are strongly encouraged to come with an update to the rose stem
suite to protect any new functionality. Configuration owners may also wish to
update the suite to ensure that important configurations are protected by the
rose stem suite.

.. warning::

    If you find that you need to update all the apps in the rose stem suite to
    get your change to work then you should use an upgrade macro.
    See :ref:`inputs`.


Adding a new app
----------------

Adding a new app to rose-stem can look daunting, but is actually less difficult
than many other development processes as there are many examples to reference
already in the code.

1. rose-stem/app/
    Start by creating a new app with the details of the test you wish to run.
    This might be an optional configuration for an existing app, or something
    completely new.

    For the UM also create a matching rose-ana app detailing the comparisons
    required.

    Both of these will be easiest to copy an existing app that is similar to
    what you are creating and modify from there. You can use the rose edit GUI
    or manually modify the ``rose-app.conf`` files.

    .. note::

        The app should validate (i.e. be consistent with the Rose metadata, and
        produce no warnings or errors). This can be checked by running ``rose
        macro --validate --no-warn version -M path/to/rose-meta`` from within
        your new app directory, or selecting Metadata -> Check fail-if,
        warn-if from the drop-down menu of the rose edit GUI.

    .. important::

        If you are working in a UM branch and have **jules-shared** changes,
        the JULES metadata path will also need adding. Please see the shared
        metadata :ref:`guidance<shared-namelists>`.

The next steps are site and rose-stem specific, but fall broadly into two
categories - those using a jinja2 templated design which populate runtime and
graph sections for you, such as the UM METO suite, and those which are
manually configured, such as JULES.


.. tab-set::

    .. tab-item:: Templated

        2. Task definitions
            Task definitions should be added to the ``tasks.rc`` for all sites
            who will run this app.

            The tasks are defined in a dictionary format, with one entry per
            configuration and all other details are handled by the templates.
            It is possible to define multiple decomposition and thread options
            in this single entry and comparison details are also defined
            within that same dictionary entry.

            Details of the available options are listed in the template files
            in ``rose-stem/templates`` for each suite and looking at existing
            examples is encouraged.

            .. note::

                LFRic Apps has a `detailed set of wiki pages
                <https://code.metoffice.gov.uk/trac/lfric_apps/wiki/rose-stem>`__
                that document the structure and options available for their
                suite.


    .. tab-item:: Manual

        2. Task definitions
            Task definitions for the following tasks should be added to the
            ``runtime.rc`` for all sites who will run this app.

            * run the app
            * perform a KGO comparison
            * perform housekeeping

        3. Graph definitions
            Graph definitions should be added to the graph.rc for all sites who
            will run this app. These should connect together your new tasks
            created above with an appropriate build task.

.. tip::

    The site specific information is held in:
        * JULES: rose-stem/include
        * LFRic Apps & UM: rose-stem/site

.. tip::

    All ``.cylc`` files mentioned are frequently split into
    platform specific variants depending on the complexity of the sites
    suite.

    e.g. `runtime.cylc` may be spread across ``runtime-platform1.cylc`` and
    ``runtime-platform2.cylc``. If a task should be run on both platform1 and
    platform2 then both of these will need the task definition adding.
