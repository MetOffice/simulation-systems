.. _mule_release:

Mule Release
============

.. note::

    Additional details for the shumlib/mule releases can be seen `here
    <https://code.metoffice.gov.uk/trac/um/wiki/mule_shumlib_install_details>`__


Releasing Mule
--------------

.. tip::

    See `PR#2 <https://github.com/MetOffice/mule/pull/2>`__ for an example mule
    release PR.

There's no hard rule on whether a mule release is required - it comes down to
whether there have been any notable changes to mule since the last release. If
you are doing a release then do the following,

* Ensure you have a :ref:`fork <forking>` of ``mule`` and that the ``main``
  branch is up to date with the upstream repository.
* In a clone of the fork, :ref:`create a branch <create_branch>` using the
  ``main`` branch as the parent.

.. important::

    Ensure you create branches from main, otherwise you will not include the
    changes from the past release.

* Update ``admin/meto_install_mule.sh`` to update the mule version number as
  well as the UM and Shumlib releases intended for this mule release. There's no
  requirement for a link between mule and UM releases.
* Update all occurrences of the mule version number to the new version. This
  occurs in multiple places - see the above example PR or grep for the old
  version.
* Test the branch against the UM
* With a reviewer, follow the :ref:`release process <github-releases>`
* Once done, announce the release on simulation-systems discussions as well as
  VE, possibly in the Scientific Software Tools community.

.. note::

    Check that the mule and um_utils docs have built and deployed correctly to
    github pages.

Installing Mule
---------------

.. important::

    This must come after the targeted UM and Shumlib releases have been
    installed.

Installing mule has complexities as it depends on libraries installed by the UM
and shumlib and is also dependent on the python stack. It is possible to
install without the UM/Shumlib libraries, however functionality will be
missing and so this isn't done on Met Office platforms.

Mule is loaded into a user's environment by adding the install directories to
``$PATH`` and ``$PYTHONPATH`` when loading the ``um_tools`` module. To ensure
mule works with the current environment, it is installed for all different
combinations of python and numpy available. At the Met Office, these are
provided by the scitools software stacks in addition to the default
environment.

Installation at the Met Office is done by ``admin/meto_install_mule.sh`` which
will detect the current python environment and install to a directory named
for that.

To install at the Met Office

* Login as umadmin
* Move to or create ``$UMDIR/mule/mule-YYYY.MM.V``
* Get a clone of the mule repo. Use the https source for this as the shared
  account doesn't have ssh access to github.
* Run the install script without any modules loaded (this will install for the
  system python), ``./mule/admin/meto_install_mule.sh``
* For all desired scitools modules, load the module and then rerun the install
  script. Try and do this for all production/preproduction stacks as well as
  the current default previous, current and next modules.
* Repeat these steps on the EXAB, EXCD, and EXZ. As of ``2025.10.1`` this will
  no longer install for the system python on the EXs.

Once mule has been installed, we also need to add the modulefiles to their
location in ``$UMDIR/modules/modulefiles/um_tools/YYYY.MM.V``. This is most
easily done by copying an existing one and modifying the scitools modules and
python versions to match what has just been installed. These modules need to
be done for both ``openmp`` and ``no-openmp`` - the only differences between
them are the ``THREADING`` and ``module-whatis`` variables.

Once done, check the modules are setup correctly by,

.. code-block:: shell

    module load um_tools/YYYY.MM.V/openmp
    python -c "import mule"

Again, repeat this on the EXAB, EXCD, and EXZ. The module files should be
identical for both EXAB and EXCD, so you can ``scp`` one set to the other.
Again, these files can be found via the same $UMDIR path as above.

Finally, it is a good idea to update the default mule module by editing
``$UMDIR/modules/modulefiles/um_tools/.version``. It may be worth posting an
announcement a few days before changing this to give advance notice.
