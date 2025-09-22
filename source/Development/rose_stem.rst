Rose Stem Suite
===============

All new changes are strongly encouraged to come with an update to the rose stem
suite to protect any new functionality. Configuration owners may also wish to
update the suite to ensure that important configurations are protected by the
rose stem suite.

.. warning::

    If you find that you need to update all the apps in the rose stem suite to
    get your change to work then you should use an upgrade macro.
    See :ref:`inputs`.

.. tip::

    Familiarise yourself with the `Rose documentation
    <https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rose-stem.html#>`__
    before continuing with this section.

.. note::

    Migration to cylc8 and rose2 is currently in progress. UM, JULES and UKCA
    suites will work with the latest versions as well as cylc7. The LFRic Apps
    rose-stem has been written for cylc8 and is not backwards compatible.


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

    All ``*.rc`` or ``.cylc`` files mentioned are frequently split into
    platform specific variants depending on the complexity of the sites
    suite.

    e.g. `runtime.rc` may be spread across ``runtime-platform1.rc`` and
    ``runtime-platform2.rc``. If a task should be run on both platform1 and
    platform2 then both of these will need the task definition adding.
