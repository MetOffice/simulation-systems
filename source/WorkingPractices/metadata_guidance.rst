.. _metadata_guidance:

Some basic guidance on Rose metadata
====================================

We would like to ensure some conformity to the appearance of UM inputs across the GUI panels and thus request the following is observed:

* Apply the following approach for each UM input the user will be presented with a consistent set of information:

.. code-block::

    [namelist:<namelist>=<variable>]
    description=<what is the variable for?>
    help=<detailed information about the variable>
    sort-key=<XY>
    etc

then each UM input is presented as:
.. code-block::

    variable name
    short description of the variable name - also displayed when hovering on the variable name
                                           - help is displayed when one clicks the variable name.

Please use sort-keys to order the appearance of items in your panels, otherwise they appear in alphabetical order which is
inappropriate for items that are triggered on and off if they appear far away from the item that triggered them.


Please provide triggers for all variables where possible. It is much better and cleaner to only see inputs that need to be set rather than all. 

The gui provides an option to un-hide triggered variables if one wants to see them all. AND logic is possible for triggers but OR is not.

Please set compulsory=true for items and use triggers for when it is not required.

The settings of all variables will then be present, in all UM apps to aid configuration management. When they are triggered off they will be commented out, !!variable, of the UM apps. If any variable (new or existing) has received a new compulsory=true setting please use an upgrade macro to add that variable to apps with a valid value.

As well as sort-keys one could apply hard-wired hierarchical namespaces to detail where an entry should appear in the GUI. 

Rather than making major use of this functionality please consider whether it is actually more appropriate to relocate the variable itself to another namelist or even create a new namelist for it so that it appears in a suitable panel. If one alters the namelist inputs then the change will require upgrade macros to be provided; see the working practices.

Other than the above, we are not imposing an appearance for all panels, deferring that to code owners to take ownership of how they would like the layout to be. 

Even so like all UM changes the meta-data will be reviewed and thus if we see something very different, obscure or fundamentally ugly we will then add further guidance to avoid such usage!

If you are adding a new STASH diagnostic you must also add help text to the STASHmaster-meta.conf. This will provide others with help on your diagnostic. You will need to identify the stash entry with a [stashmaster:code(xyz)] section header, where the xyz is the stash code in the form section number * 1000 + item number. 

Include a full name, any units and explanatory text. You should also add a description field that matches the full name of the diagnostic. For example:

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

Viewing meta-data changes as you go along
-----------------------------------------

One can easily review their meta-data changes with the rose config editor, opening up an example app file. For example

.. code-block::

  cd <path of working copy of branch>/rose-stem/app/um_n48_eg
  rose config-edit -M <path of working copy of branch/rose-meta/>

then once the app opens click on the LHS appname to being up the app meta panel. Update this to HEAD rather than the version number and apply.

Please note that if you have used an upgrade macro on the app then the meta line at the top of the app file will have changed (i.e. meta=um-atmos/vn11.0_t46). Since no meta-data exists at this version rose edit will produce an error saying that it cannot find it, instead it will use the meta-data in um-atmos/HEAD. Please click OK and continue.

Your updates should now appear. 
