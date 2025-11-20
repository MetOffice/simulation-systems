.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _umdp_release:

UMDP Release
============

* Ensure you have a :ref:`fork <forking>` of both ``um_doc`` repository, and
  that the ``main`` branch is up to date with the upstream repository.
* In a clone of this fork, :ref:`create a branch <create_branch>` using the
  ``main`` branch as the parent.

.. important::

    Ensure you create branches from main, otherwise you will not include the
    changes from the past release.

* You will need to update a few files:

  * For ``web/js/um-version.js`` update the version number, release name, and
    standard suite hashes.
  * For ``template/UMDP.cls``, update the version number.
  * For the x-series documentation, you will at minimum need to check and
    update:

    * ``source/X04/X4-fcm.tex`` Commit hash and version number
    * ``source/X04/X4-prerequisites.tex`` rose and cylc versions (found in the
      release notes).
    * ``source/X04/X4.tex`` UM, gcom, shumlib and UKCA versions (found in the
      release notes).
    * ``source/X06/X6.tex`` UM version number.
    * ``source/X10/X10.tex`` UM, JULES and UKCA version numbers, gcom branch
      URL.

* It is also worth checking no URLs are out of date.
* With a reviewer, follow the :ref:`release process <github-releases>`.

.. admonition:: todo

    How are we publishing these docs?


.. The old method of publishing the docs to fcm is documented here:

.. * To Publish the docs:

..   * Get a new copy of the head of the docs ``main``
..   * From the top level, run ``build_umdoc.py all`` to build everything
..   * Remove the output logs in ``output/log/*`` - just to save a bit of space.
..   * Checkout a copy of the published documentation - just take the UM part of it as the whole thing is massive! i.e. ``fcm co https://code.metoffice.gov.uk/svn/doc/um published_um``
..   * We keep the 3 most recent UM versions so delete one, ``fcm del vnXX.Y-2``
..   * Edit the ``index.html`` file to remove the oldest version and add a new line for the new one.
..   * Copy the ``output`` directory that was created by the build script earlier into a ``vnXX.Y`` directory and make sure it is added to the version control.
..   * Finally, update the ``latest`` symlink to point to the newest version, ``ln -s vnXX.Y latest``
..   * Finally, commit the changes and check the output at https://code.metoffice.gov.uk/doc/


