.. _umdp_release:

UMDP Release
============

* Create a ticket and a Head of Trunk branch of the UM documentation.
* You will need to update a few files:

  * For ``web/js/um-version.js`` update the version number, release name, and standard suite revision numbers.
  * For ``template/UMDP.cls``, update the version number.
  * For the x-series documentation, you will at minimum need to check and update:

    * ``source/X04/X4-fcm.tex`` Revision number and version number
    * ``source/X04/X4-prerequisites.tex`` rose and cylc versions (found in the release notes).
    * ``source/X04/X4.tex`` UM, gcom, shumlib and UKCA versions (found in the release notes).
    * ``source/X06/X6.tex`` UM version number.
    * ``source/X10/X10.tex`` UM, JULES and UKCA version numbers, gcom branch URL.

* It is also worth checking no URLs are out of date.
* Get ticket reviewed and committed.
* :ref:`Tag <reference-tagging>` the documentation trunk by adding the correct ``vnXX.X`` keyword.
* To Publish the docs:

  * Get a new copy of the head of the docs trunk
  * From the top level, run ``build_umdoc.py all`` to build everything
  * Remove the output logs in ``output/log/*`` - just to save a bit of space.
  * Checkout a copy of the published documentation - just take the UM part of it as the whole thing is massive! i.e. ``fcm co https://code.metoffice.gov.uk/svn/doc/um published_um``
  * We keep the 3 most recent UM versions so delete one, ``fcm del vnXX.Y-2``
  * Edit the ``index.html`` file to remove the oldest version and add a new line for the new one.
  * Copy the ``output`` directory that was created by the build script earlier into a ``vnXX.Y`` directory and make sure it is added to the version control.
  * Finally, update the ``latest`` symlink to point to the newest version, ``ln -s vnXX.Y latest``
  * Finally, commit the changes and check the output at https://code.metoffice.gov.uk/doc/


