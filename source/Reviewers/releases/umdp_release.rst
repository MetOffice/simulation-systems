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
* Ensure the action to publish the documentation has successfully completed and
  the `new documentation is available <https://metoffice.github.io/um_doc/>`_.
