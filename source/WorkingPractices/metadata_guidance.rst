.. _metadata_guidance:

..
  This section will need some thought and revisiting after CA2 is completed.

Some basic guidance on Rose metadata
====================================

It is important that the appearance of inputs across the GUI panels conform to the same standards.
This ensures that users of each model become familiar with how the panels work and are present
with a consistent set of information, such as follows:

.. code-block::

    [namelist:<namelist>=<variable>]
    description=<what is the variable for?>
    help=<detailed information about the variable>
    sort-key=<XY>
    etc

then each input is presented as:

.. code-block::

    variable name
    short description of the variable name

Help text is displayed when one clicks the variable name.

..
 We need to check if this is all still the case with cylc 8.

The following sections provide some general guidance as to how to structure your metadata.

..
  This is largely based on how the UM does everything, so should be revisited after the CA2
  activity is finished. The following sections have been

Number of panels
----------------
If you have a particularly long namelist, consider diving up the number of panels to ensure
that the user doesn't have to deal with a particularly long panel with lots of switches.
However, switches which relate to each other should always be on the same panel.


Sort Keys and triggers
----------------------
Please use sort-keys to order the appearance of items in your panels, otherwise they will appear
in alphabetical order. This means that sometimesitems that are triggered on and off will appear
far away from the item that triggered them.

Please provide triggers for all variables where possible. It is much better and cleaner to only
see inputs that need to be set rather than everything.

.. tip::
  The GUI provides an option to un-hide triggered variables if one wants to see them all.

Please set ``compulsory=true`` for items and use triggers for when it is not required.The settings
of all variables will then be present, in all apps to aid configuration management. When a variable
is triggered off, it will be commented out in the apps e.g. ``!!variable``.

..
  I think from memory that JULES doesn't do the compulsory=true, which is something for CA2 to look at.

.. important::
  If any variable (new or existing) has received a new compulsory=true setting please use an upgrade macro to
  add that variable to apps with a valid value.

.. note::
  While it is possible to trigger a variable based on ``AND`` logic (e.g. where some condition on ``variable1``
  and another condition on ``variable2`` trigger ``variable3``), cumbersome triggering of this nature is best
  avoided.

  It is not possible to trigger a variable based on ``OR`` logic.

STASH diagnostics (UM metadata only)
------------------------------------

If you are adding a new UM STASH diagnostic you must also add help text to the STASHmaster-meta.conf.
This will provide others with help on your diagnostic. You will need to identify the stash entry with
a ``[stashmaster:code(xyz)]`` section header, where the xyz is the stash code in the form
``section number * 1000 + item number``.

Include a full name, any units and explanatory text. You should also add a description field that matches
the full name of the diagnostic. For example:

.. code-block::

    [stashmaster:code(1050)]
    description=NO2 Dry Deposition Rate (3D)
    help=NO2 Dry Deposition Rate (3D)
        =moles/s
        =
        =This is the total dry deposition flux of NO2 in each gridbox
        =
        =The sum of this deposition flux over all model gridboxes gives the total
        =number of moles of NO2 removed by this process per second in the
        =whole model.

This assists the model user in being able to find useful help text on their diagnostic.

Viewing meta-data changes as you go along
-----------------------------------------

One can easily review their meta-data changes with the rose config editor, opening up an example app file. For example

.. code-block::

  cd <path of working copy of branch>/rose-stem/app/um_n48_eg
  rose config-edit -M <path of working copy of branch/rose-meta/>

then once the app opens click on the LHS appname to being up the app meta panel. Update this to HEAD rather than the version number and apply.

Please note that if you have used an upgrade macro on the app then the meta line at the top of the app file will have changed (i.e. meta=um-atmos/vn11.0_t46). Since no meta-data exists at this version rose edit will produce an error saying that it cannot find it, instead it will use the meta-data in um-atmos/HEAD. Please click OK and continue.

Your updates should now appear. 
