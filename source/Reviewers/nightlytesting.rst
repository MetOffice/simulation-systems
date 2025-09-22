.. _nightlytesting:

Nightly Testing
===============

.. important::

    These instructions are intended for Met Office reviewers with access to the
    nightly testing user only.

Modifying and Installing Testing
--------------------------------

Nightly testing is controlled by 2 cronfiles, ``auto-gen_testing.cron`` and
``manual.cron`` both located in ``~/Crontabs/``. The first is automatically
generated the script ``generate_test_suite_cron.py`` which is stored in the
SimSys_Scripts github repo and controls the launching and clean up of the
nightly rose-stem suites. The second is intended for manually adding tasks
which don't fit the pattern of the regular rose-stem suites.

Rose-stem testing is controlled by a config file located at
``~/testing_configs.yaml``. This contains entries for each of the suites that
will be regularly launched. The following options are available when defining
a suite:

* ``repo``: Required, The fcm repo being run. This string should be match the
  fcm repo name such that ``fcm:REPO.xm_tr`` is a valid url.

* ``period``: Required, The period with which the job repeats. Options are:

    * ``weekly``: Runs on Mondays, cleans on Sundays.
    * ``nightly``: Runs Tue-Fri, cleans Wed-Sat.
    * ``nightly_all``: Runs Mon-Fri, cleans Tue-Sat.

* ``time_launch``: Required, 24 hour time format for the time to launch the
  suite.

* ``time_clean``: Required, 24 hour time format for the time to clean the
  previous iteration of this suite. If the period is weekly, the cleanup
  occurs on a Sunday, otherwise it occurs 1 day later than the suite was run.

* ``groups``: Required, the rose-stem groups to run.

* ``revisions``: Optional, Defines what revisions of dependency repos to use.
  Either ``set`` to use the revisions defined in the repo or ``heads`` to do
  HoT testing. Defaults to use Set Revisions.

* ``vars``: Optional, This is a list format of strings to be added to the
  rose-stem command with the ``-S`` prefix.

* ``monitoring``: Controls whether to launch the monitoring script on this
  suite. If true, the monitoring script will be launched at 06:00.

* ``cylc_version``: Controls which cylc_version to use. The suite is now set up
  to use primarily cylc8 with some suites being launched at Cylc7 for the UM
  and Jules. Can be any string beginning "7" or "8" that is a valid cylc
  install at the site, such that ``export CYLC_VERSION=<cylc_version>``
  works.

The cronjobs are installed by running the ``generate_test_suite_cron.py``
script with the ``--install`` command line option. This script is stored in
the SimSys_Scripts github repo. It will read a config file, generate a cron
file and then install the cronjobs from all files with extension .cron in a
specified location. The script has the following command line arguments:

* ``-c --config``: Required, the path to a yaml file with the testing
  configurations. For the meto testing user this file is located at
  ``~/ccc.yaml``.

* ``-f --cron_file``: The file the cronjobs will be written to. Defaults to
  ``~/Crontabs/auto-gen_testing.cron``.

* ``-l --cron_log``: The file cron task output will be piped to. Defaults to
  ``~/cron.log``.

* ``-p --cylc_path``: The location of the Cylc Installations. Required if
  testing with ``cylc-next``.

* ``--install``: If included will install the cronjobs from files with
  extension .cron in the location defined by the cron_file argument.

To update and install at meto:

.. code-block:: shell

    python3 generate_test_suite_cron.py \
        -c ~/Crontabs/nightly_testing_configs.yaml --install

Retriggering Nightlies
----------------------

TLDR Instructions
^^^^^^^^^^^^^^^^^

.. code-block:: shell

    #  As the testing user
    rs8
    # Wait for retrigger script to run - answer questions as required
    cylc_url
    # Select the 2nd url that appears

Full Explanation
^^^^^^^^^^^^^^^^

To retrigger the nightlies a script is available at
``$UMDIR/SimSys_Scripts/nightly_testing/retrigger_nightlies.py``. To run this
use the alias ``rs8`` which will load the required modules and set the cylc
version to 8. The script will detect any suites from the previous night with
failed tasks and ask whether to retrigger them. It will restart requested
suites, sleep, and then individually retrigger any failed tasks. Running ``rs8
PATTERN`` will only launch suites which match that pattern (no wildcard
matching is currently setup), eg. ``rs8 lfric_apps`` will restart suites
with "lfric_apps" in their name.

To interact with the nightlies open a cylc8 gui by:

.. code-block:: shell

    export CYLC_VERSION=8
    cylc gui --ip=0.0.0.0 --no-browser --debug --Application.log_level=WARN

or the meto user has an alias defined as ``cylc_url``. Copy the 2nd url that
appears into your browser.

Suites can also be triggered without using the script. In the gui, select the
suite on the left and then click the play triangle at the top. This can also
be done on the command line by:

.. code-block:: shell

    cylc play <NAME-OF-SUITE>


Tasks can be retriggered individually or in groups. Eg, to retrigger all failed
tasks, click the menu icon at the top of the page, and then select "Trigger".
In the resulting dialogue box, append the "Tasks" section with ``:failed``
then click submit. To retrigger individually is similar but click the menu
icon next to the task.

To alter a tasks runtime settings, eg. bump the wallclock, select the jobs menu
and then choose ``Edit Runtime``. This will open a dialog box where runtime
items can be added/edited. When done click ``submit`` and then ``Trigger``
(unlike cylc7 it won't ask you to do this).

.. important::

    When finished Keyboard terminate the cylc url command and choose y when
    prompted. This shutsdown the cylc server and prevents multiple connections
    opening.

