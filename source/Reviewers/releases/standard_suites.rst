.. _standard_suites:

Standard Suites
===============

UM Standard Suites
------------------

For the UM the following Suites must be updated:

* UM Azspice - `u-aa003 <https://code.metoffice.gov.uk/trac/roses-u/browser/a/a/0/0/3/trunk>`_
* UM EX1A - `u-ci752 <https://code.metoffice.gov.uk/trac/roses-u/browser/c/i/7/5/2/trunk>`_
* SCM - `u-aa741 <https://code.metoffice.gov.uk/trac/roses-u/browser/a/a/7/4/1/trunk>`_
* CreateBC - `u-aa258 <https://code.metoffice.gov.uk/trac/roses-u/browser/a/a/2/5/8/trunk>`_

First get a copy of the UM meta trunk, ``fcm co fcm:um_meta.x_tr /path/to/meta/trunk``. Similarly, get a copy of Jules at the most recent release. Then upgrade each suite by doing the following,

* Checkout the suite. ``rosie checkout u-xxNNN`` will put a copy in ``~/roses``.
* Check whether the ``access-list`` in the ``rose-suite.conf`` needs updating - if you are not on it, ask someone to add you now and update your copy once done.
* Move into the suite and edit the ``rose-suite.conf`` file,

  * If it has a ``VN`` setting, update it to the new version.
  * If it has a ``prebuild`` path, update that now. If there are prebuilds, check the ``flow.cylc`` for any prebuild path overrides. These exist particularly on the EXs.

* Validate the existing apps by running,

  .. code-block::

    rose macro --fix -C app/APP

  where ``APP`` should be replaced by each available app in turn. It should report that 0 changes were made.
* Now upgrade the apps to the new version, using the metadata trunk checked out earlier. Again, replace ``APP`` with each app in turn. This will prompt you to confirm while running.

  .. code-block::

    rose app-upgrade -C app/APP -M /path/to/the/meta/trunk vnX.Y

* Finally run the validator macros. If everything is fine the command will report nothing, however the SCM suite will raise some warnings about Openmp and "global rows" - these can be ignored.

  .. code-block::

    rose macro metomi.rose.macros.DefaultValidators -M /path/to/the/meta/trunk:/path/to/the/jules/hot/rose-meta

* Check that the changes look sensible and then run the suite,

  .. code-block::

    fcm diff -g
    cylc vip

.. _suite_commit:

* Once the suite has succeeded, commit the changes (``fcm ci``) with a suitable message and note the revision it was committed at. Then tag the suite and commit the tag,

  .. code-block::

    fcm pe fcm:revision .
    <add tag to resulting editor>
    fcm ci


LFRic Apps Standard Suites
--------------------------

For LFRic Apps the following Suites must be updated:

* LFRic Apps Azspice - `u-dn674 <https://code.metoffice.gov.uk/trac/roses-u/browser/d/n/6/7/4/trunk>`_
* LFRic Apps EX1A - `u-dn704 <https://code.metoffice.gov.uk/trac/roses-u/browser/d/n/7/0/4/trunk>`_


For each suite, do the following:

* Get a copy of each of these suites and move into the working copy.

    .. code-block::

        rosie co u-dn704
        cd ~/roses/u-dn704

* In ``rose-suite.conf`` update the version number
* Upgrade the metadata for the mesh and lfric_atm apps

    .. code-block::


        rose app-upgrade -a -y -C app/lfric_atm vnX.Y
        rose app-upgrade -a -y -C app/mesh vnX.Y

* Check the modules loaded in the ``flow.cylc`` for any changes vs. the Apps trunk.

    * See ``rose-stem/site/meto/common/suite_config_PLATFORM.cylc``
    * The lfric software stack moves more quickly than the UM, so it is more likely these have changed.

* Test - ``cylc vip``
* :ref:`Commit and Tag <suite_commit>` the suite once the test suite has succeeded.

