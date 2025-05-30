Curating a Release
==================

.. toctree::
    :maxdepth: 1

    releases/um_test_release
    releases/jules_release
    releases/um_main_release
    releases/lfric_apps_release

.. _reference-tagging:

Tagging FCM Trunks
------------------

Tagging fcm trunks with new release keywords is done in lots of places throughout these instructions. This section is a guide for doing this, using the UM as an example.

The keywords need to be added to the base directory of the project, i.e. in the directory that contains trunk and branches.

.. code-block::

    # Note the -q means quiet checkout, nothing is printed to std out. The -N means
    # only the top level directory is extracted, otherwise it would extract the
    # entire repository (and take many hours!)
    # The 'fcm log' command gives you the most recent log message for the
    # respective trunk, and more importantly, the revision number.

    fcm co -q -N fcm:um.x um
    fcm log -l1 fcm:um.x/trunk
    cd um
    fcm pe fcm:revision .

In the editor that comes up (you may need to specify the editor using ``--editor-cmd vi``) add the new keyword, e.g. ``vn11.5 = 810`` (noting the format may change away from the UM). Once completed save the changes and close the editor. Finally commit the change, ``fcm ci``.


Release Ticket
--------------

Open a UM X.Y release Curation Ticket, and assign tasks as a team,

.. code-block::

    The following tickets are required to deliver UM vnX.Y:

    ||= Led by... =||= Description                                                                   =||= Ticket # =||
    ||||||'''Pre release'''||
    ||  || Test release                                                                               ||  ||
    ||  || Partner testing                                                                            ||  ||
    ||  || Scientific Software Stack Update                                                           ||  ||
    ||||||'''Release'''||
    ||  || JULES umX.Y release - [jules:wiki:CuratingARelease]                                        ||  ||
    ||  || Shumlib + Mule releases                                                                    ||  ||
    ||  || Build and install the main release                                                         ||  ||
    ||  || LFRic Apps Release                                                                         ||  ||
    ||||||'''Post Release'''||
    ||  || Release notes                                                                              ||  ||
    ||  || Update standard suites & finalise std jobs page                                            ||  ||
    ||  || Update $UMDIR scripts                                                                      ||  ||
    ||  || Check resource monitoring scripts still work                                               ||  ||
    ||  || Install Code and Stash browsers                                                            ||  ||
    ||  || UMDP3 Release                                                                              ||  ||
    ||  || Update wikis, working practices, and create bit comp table                                 ||  ||
    ||  || Review and update trunk and shared account permissions                                     ||  ||

    [wiki:CuratingARelease Curating a release Page]


Pre-Release
-----------

:ref:`UM Test Release<um_test_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
The point of the test release is to test the release system/process works before we have to do it for real. Typically aim for 1-2 weeks before release day. However, before a test release can be done, all changes to fcm-make config files, major rose-stem changes (things like basic upgrade macro or KGO updates don't necessarily need to be included) and modifications to the release_new_version.py script need to be on trunk, so this will cause some variation as to when the test release is done from release to release.


`Partner Testing <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#PartnerTesting-72hourfreeze>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All source code changes must be on trunk along with any rose-stem changes that affect multiple sites before partner testing can start. Ideally the test release will also have been completed.


`Scientific Software Stack Update <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#ScientificSoftwareStackUpdate>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Any potential changes to platform software stacks


Main Release
------------

:ref:`Jules Release <jules_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Partner Testing, All Jules tickets committed


`Mule and Shumlib Releases <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#ShumlibMulereleases>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All tickets affecting Shumlib or Mule should have been committed.


:ref:`UM Main Release<um_main_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All UM Tickets, Test Release, Partner Testing, Jules Release


:ref:`LFRic Apps Release<lfric_apps_release>`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
All LFRic Tickets (Apps + Core), Jules Release


Post Release Tasks
------------------

`Release Notes <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#ReleaseNotes>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
Most of this can be done pre-release but some details of revision numbers will be dependent on the main release being done.


`Upgrading Standalone Suites <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#UpgradingStandaloneSuites>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release (for UM suites), Apps Release (for Apps suites)


`Standard Jobs Page <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#FinalizeTheStandardJobspage>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release


`Code and Stash Browsers <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#InstallCodeandStashbrowsers>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release


`UMDP Release <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#UMDPrelease>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release, Standard Suites Upgrade


`Wikis Update <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Updatewikisworkingpracticesandcreatebitcomptable>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
UM Release


`Shared Account Permissions <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Reviewandupdatetrunkandsharedaccountpermissions>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Dependencies**
None


Mid-Release Tasks
-----------------

`Creating an Interim Release <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Creatinganinterimrelease>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


`Installing New Prebuilds <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Installingnewprebuilds>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
