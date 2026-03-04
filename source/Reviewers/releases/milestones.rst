.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _milestones:

Milestones and Projects
=======================

#. In the `Review <https://github.com/orgs/MetOffice/projects/376/archive>`_ and
   `Issue <https://github.com/orgs/MetOffice/projects/418/archive>`_ Archive
   pages, delete all existing archived items from the project.

   .. image:: images/gh_screenshots/delete_archive_light.png
      :class: only-light border

   .. image:: images/gh_screenshots/delete_archive_dark.png
      :class: only-dark border

   repeating as many times as required.

#. Tidy up all pull requests and issues for the completed milestone in the
   Simulation Systems Review and Issues Trackers.

   .. code-block:: shell

      python SimSys_Scripts/gh_review_project/finish_milestone.py --milestone="<milestone title>"

      with optional argument ``--dry`` to dry run the changes.

   The script will prompt for you to continue after checking all PRs and issues
   are in a suitable state. If it flags items that need correcting then go to
   `Simulation Systems Review Tracker`_ and
   `Simulation Systems Issue Tracker`_ to manually sort them.

   .. note::

      The github review project page can take a
      `long time <https://github.com/orgs/community/discussions/186349>`_ (> 30
      minutes) to update after running this script. Check that a given PR has
      been archived on the PR page, then feel free to carry on if this is the
      case.

#. As prompted by the above script, close the current milestone using:

   .. code-block:: shell

      ./SimSys_Scripts/sbin/gh_manage_milestones -t <title of milestone> -m close

#. Open the next new milestone so that there are the same number of open milestones:

   .. code-block:: shell

      ./SimSyS_Scripts/sbin/gh_manage_milestones -t <title> -d YYYY-MM-DDT00:00:01Z -p <description>

   * the title is ``Spring YYYY``, ``Summer YYYY`` or ``Autumn YYYY``
   * the date is the first Wednesday in March, July or November
   * the description is ``Code Review deadline is <date> (SciTech review to be completed by this date)``
     selecting a Friday at the end of January/May/September for the deadline.

.. _Simulation Systems Review Tracker: https://github.com/orgs/MetOffice/projects/376
.. _Simulation Systems Issue Tracker: https://github.com/orgs/MetOffice/projects/418
