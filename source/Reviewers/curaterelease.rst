Curating a Release
==================

.. toctree::
    :maxdepth: 1

    releases/um_test_release
    releases/um_main_release
    releases/lfric_apps_release


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
===========

Test Release
------------

**Dependencies**
The point of the test release is to test the release system/process works before we have to do it for real. Typically aim for 1-2 weeks before release day. However, before a test release can be done, all changes to fcm-make config files, major rose-stem changes (things like basic upgrade macro or KGO updates don't necessarily need to be included) and modifications to the release_new_version.py script need to be on trunk, so this will cause some variation as to when the test release is done from release to release.

:ref:`UM Test Release<um_test_release>`


Partner Testing
---------------

**Dependencies**
All source code changes must be on trunk along with any rose-stem changes that affect multiple sites before partner testing can start. Ideally the test release will also have been completed.

`Partner Testing <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#PartnerTesting-72hourfreeze>`_


Scientific Software Stack Update
--------------------------------

**Dependencies**
Any potential changes to platform software stacks

`Scientific Software Stack Update <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#ScientificSoftwareStackUpdate>`_


Main Release
============

Jules Release
-------------

**Dependencies**
Partner Testing, All Jules tickets committed

`Jules Release <https://code.metoffice.gov.uk/trac/jules/intertrac/wiki%3ACuratingARelease>`_


Mule and Shumlib Releases
-------------------------

**Dependencies**
All tickets affecting Shumlib or Mule should have been committed.

`Mule and Shumlib Releases <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#ShumlibMulereleases>`_


Main UM Release
---------------

**Dependencies**
All UM Tickets, Test Release, Partner Testing, Jules Release

:ref:`UM Main Release<um_main_release>`


LFRic Apps Release
------------------

**Dependencies**
All LFRic Tickets (Apps + Core), Jules Release

:ref:`LFRic Apps Release<lfric_apps_release>`


Post Release Tasks
==================

Release Notes
-------------

**Dependencies**
Most of this can be done pre-release but some details of revision numbers will be dependent on the main release being done.

`Release Notes <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#ReleaseNotes>`_


Upgrading Standalone Suites
---------------------------

**Dependencies**
UM Release (for UM suites), Apps Release (for Apps suites)

`Upgrading Standalone Suites <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#UpgradingStandaloneSuites>`_


Standard Jobs Page
------------------

**Dependencies**
UM Release

`Standard Jobs Page <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#FinalizeTheStandardJobspage>`_


Code and Stash Browsers
-----------------------

**Dependencies**
UM Release

`Code and Stash Browsers <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#InstallCodeandStashbrowsers>`_


UMDP Release
------------

**Dependencies**
UM Release, Standard Suites Upgrade

`UMDP Release <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#UMDPrelease>`_


Update Wikis, Working Practices, Create Bit Comp Table
------------------------------------------------------

**Dependencies**
UM Release

`Wikis Update <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Updatewikisworkingpracticesandcreatebitcomptable>`_


Review Shared Account Permissions
---------------------------------

**Dependencies**
None

`Shared Account Permissions <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Reviewandupdatetrunkandsharedaccountpermissions>`_


Creating an Interim Release
---------------------------

`Creating an Interim Release <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Creatinganinterimrelease>`_


Installing New Prebuilds
------------------------

`Installing New Prebuilds <https://code.metoffice.gov.uk/trac/um/wiki/CuratingARelease#Installingnewprebuilds>`_
