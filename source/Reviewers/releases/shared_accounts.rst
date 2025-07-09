.. _shared_accounts:

Trunk and Shared Accounts Permissions
=====================================

.. warning::

    Incorrectly editing the svnperms.conf file can break all access to a repo

To update fcm repositories trunk access list (using UM as an example),

* First checkout the top level of the repo,

  .. code-block::

    fcm co --depth=files https://code.metoffice.gov.uk/svn/um

* Move into the working copy and make the required changes in the ``svnperms.conf`` file.
* Commit the change.

The above process needs doing for all of,

* UM
* LFRic Apps
* Jules
* UKCA
* Casim
* Shumlib
* MOCI

Modify SSD Team Github Permissions:

* https://github.com/orgs/jules-lsm/teams/system-managers
* ​https://github.com/orgs/MetOffice/teams/ssdteam

Review account permissions in Active Directory for the following Shared Users:

* umadmin
* umtest
* julesadmin
* lfricadmin
* spackadmin
