.. _lfric_apps_release:

LFRic Apps Release ==================

LFRic Inputs KGO Install
------------------------

* This can be done at any point once all tickets that change lfricinputs kgo
  have been committed.
* It's easiest to use the umtest nightly testing for this and will save having
  to run the suite twice.
* Alternatively, run ``rose stem --group=lfricinputs`` and wait for this to
  finish - all jobs should pass.
* Install the kgo by running
  ``$UMDIR/SimSys_Scripts/kgo_updates/meto_update_kgo.sh --new-release``

    * The script will ask for a working copy path - this can be any lfric apps
      working copy as it will not be modified.
    * The version number and ticket number are not required, although an entry
      is required.
    * The kgo install directory must be updated to vnX.Y


LFRic Release
-------------

* Create a ticket and branch in each of LFRic Apps and Core. Check both of
  these out.
* Move into the lfric apps working copy
* Run the release script,
  ``$UMDIR/SimSys_Scripts/lfric_macros/release_lfric.py -o A.B -v X.Y -t
  TTTT -c /path/to/core``

    * ``A.B`` - the previous version
    * ``X.Y`` - the new version
    * ``TTTT`` - the apps release ticket number
    * ``/path/to/core`` - path to the lfric core working copy

* Check the output looks sensible. It should:

    * Update the version number
    * Revert any changes to ``rose-stem/site/meto/variables_*.cylc``
    * Copy the ``HEAD`` metadata to ``vnX.Y``
    * Add a blank upgrade macro to all ``versions.py`` files
    * Apply the upgrade macro - rose apps should be updated to the new version
    * Add a ``version_ab_xy.py`` upgrade file - a copy of the versions.py file
    * Reset the ``versions.py`` file with no upgrade macros

* Run the test suites

    * ``rose stem --group=all`` for both Apps and Core.
    * Make sure ``dependencies.sh`` is pointing at the core working copy

* Once testing is complete, reset the ``dependencies.sh``

    * LFRic Core should be ``coreX.Y``
    * All others should be ``umC.D``

* Get the tickets reviewed and committed:

    * Commit LFRic Core
    * Ask CCD to :ref:`tag <reference-tagging>` core with ``coreX.Y=revision``
    * Commit LFRic Apps

* :ref:`Tag <reference-tagging>` the LFRic Apps Trunk ``vnX.Y=revision``
