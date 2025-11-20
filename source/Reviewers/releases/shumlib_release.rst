.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _shumlib_release:

Shumlib Release
===============

.. note::

    Additional details for the shumlib/mule releases can be seen `here
    <https://github.com/MetOffice/git_playground/wiki/Shumlib-and-Mule-Additional-Install-Details>`__


Releasing Shumlib
-----------------

There's no hard rule on whether a shumlib release is required - it comes down
to whether there have been any notable changes to shumlib since the last
release. If there haven't, then a release isn't necessary. In this case, the
shumlib ``main`` will get a ``umX.Y`` tag during the UM release but that is all.

If you are doing a release then do the following,

* Ensure you have a :ref:`fork <forking>` of ``shumlib`` and that the ``main``
  branch is up to date with the upstream repository.
* In a clone of the fork, :ref:`create a branch <create_branch>` using the
  ``main`` branch as the parent.

.. important::

    Ensure you create branches from main, otherwise you will not include the
    changes from the past release.

* Update the shumlib version number in ``common/src/shumlib_version.h``
* Update the shumlib version number (in a comment) in
  ``meto_install_shumlib.sh``.
* Test the branch against the UM
* With a reviewer, follow the :ref:`release process <github-releases>`


Installing Shumlib
------------------

Shumlib is installed with a build script, at ``scripts/meto_install_mule.sh``.
This takes a single compulsory argument to set the ``platform`` of the
install. Generally, this is a platform at the Met Office, currently ``ex1a``
or ``azspice``, which will install shumlib for all defined builds on that
platform. Alternatively, you can use a specific build, eg.
``azspice_gnu_12.2``, to install just for that build.

By default, shumlib will be installed in a ``build`` directory in the working
copy. This can be controlled using the ``BUILD_DESTINATION`` environment
variable.

To install at the Met Office, login as ``umadmin`` and get a clone of the new
version. Use https to get this as the shared account doesn't have ssh access.
First install on azspice,

.. code-block:: shell

    export SPACKDIR= # Set this as the Spackadmin Data Directory (no trailing slash)
    BUILD_DESTINATION=$UMDIR/shumlib/shumlib-YYYY.MM.V scripts/meto_install_shumlib.sh azspice

Then ssh to each of EXAB, EXCD and EXZ and install there,

.. code-block:: shell

    BUILD_DESTINATION=$UMDIR/shumlib/shumlib-YYYY.MM.V scripts/meto_install_shumlib.sh ex1a

Finally do the install on Monsoon (using ``umadmin.mon`` shared user).
