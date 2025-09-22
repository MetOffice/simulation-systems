.. _lfric_diag:

LFRic Atmosphere Diagnostics
============================

This section describes changes required to add a new diagnostic to the LFRic
atmosphere model. If a diagnostic is being added to an existing science
scheme, it may be possible to copy and adapt code for an existing diagnostic.
Excluding code to compute the new diagnostic, adding a diagnostic amounts to
just three small changes.

.. topic:: Checklist for experienced developers

   For experienced or confident users adding a diagnostic to an existing
   science section, follow these steps:

   #. Add a new record to the field definition file. Most diagnostic fields are
      defined in the ``lfric_atm/metadata/field_def_diags.xml`` file. It can
      be based on an existing diagnostic if a similar one is available.
   #. Add lines to initialise the field holding the diagnostic in the
      appropriate diagnostics initialisation module. Add the field to the
      procedure argument list. Typically, the modules are named after the
      science section with the suffix ``_diags_mod.f90``.
   #. Add lines to write out the diagnostic field in the output procedure held
      in the same module.
   #. In the algorithm that calls the initialise and write routines, add the
      code to compute the new diagnostic, including passing the field down to
      any algorithms or kernels involved in the computation.
   #. If the diagnostic has not been requested, then the field will not be
      fully initialised. Therefore, include checks to ensure such diagnostics
      are not computed.

Overview
--------

The diagnostic system for the LFRic atmosphere model uses the XIOS library.
XIOS inputs and outputs are configured using an ``iodef.xml`` file. An
``iodef.xml`` file for a given LFRic atmosphere model setup includes
definitions of all possible prognostics and diagnostics and, separately, a set
of diagnostic output requests.

Field definitions are held in various files found in the ``lfric_atm/metadata``
directory. Diagnostic requests are separate as they are part of a particular
application configuration. The ``iodef.xml`` file includes all these files by
specifying links to them.

Any field defined in the XML file can be selected for output to a diagnostic
file. XIOS supports various post-processing operations that can be specified
in the diagnostic request to generate, for example, a daily mean of a field.
Field requests can be grouped to be output to different file streams.

.. topic:: Comparing with the Unified Model STASH system

   Users familiar with the Unified Model STASH system will know that for each
   available diagnostic, multiple output requests can be made, each of which
   can undergo different time or spatial processing and can be sent to a
   different file. Further, the UM system supports a graphical user interface
   that can edit the lists of requests for a given application.

   XIOS has similar and more extensive processing capabilities, but at the
   moment, no user interface support has been provided for users of the LFRic
   atmosphere model. Requests have to be constructed by editing the XML files
   included in the ``iodef.xml`` file for a given application configuration.

XIOS is a highly complex and flexible parallel IO system with post-processing
capabilites, including the ability to apply time and spatial processing as
well as combine multiple fields. It is developed at IPSL.

.. caution::

   While it would be possible to write a set of complex diagnostic requests
   using all the features of XIOS, people should be cautious because future
   developments of the LFRic atmosphere user environment may not support all
   the flexibility required to reconstruct the request. Furthermore, the
   underlying XIOS software is complex, and it is possible to create a complex
   diagnostic request that is unreliable or that imposes high computation
   costs on the application.

Permitted diagnostic fields
---------------------------

Diagnostic fields can only be created for the following types of LFRic
atmosphere fields:

* A :math:`\mathbb{W}_{3}` field representing data, typically scalar
  quantities, at the centre of each 3D model cell.
* A :math:`\mathbb{W}_{theta}` or :math:`\mathbb{W}_{2v}` field both
  representing data at the centre of the bottom and top face of each 3D model
  cell (noting that a cell shares the data point on its top face with the cell
  above). The :math:`\mathbb{W}_{3}` fields represent scalar quantities, and
  the :math:`\mathbb{W}_{2v}` represent vectors or fluxes.
* A :math:`\mathbb{W}_{2h}` field representing data, typically vectors or
  fluxes, at the centre of the faces around the side of each cell(noting that
  neighbouring cells share these faces and data points).
* A single-level field.
* A "multidata" field. Some types of single level
  :math:`\mathbb{W}_{3}` field store more than one quantity, such as a data
  point for each vegetation type or for different radiation bands. Supported
  multidata fields are defined in the ``metadata/axis_def_main.xml`` file.

Detailed steps for adding a new diagnostic
------------------------------------------

To add a diagnostic for potential output from the LFRic atmosphere model,
follow these steps:

#. Create a ``field`` record in the relevant XML file that is used to create
   the XIOS ``iodef.xml`` file.
#. Add code to initialise a model field to hold the diagnostic. For existing
   science schemes it may be possible to add the field initialisation code to
   an existing module. This step is not required if the diagnostic is obtained
   from an existing field such as from a prognostic field passed into the
   algorithm.
#. Add code to write out the field.

Once the above steps are complete, code can be added to compute the diagnostic.
It is possible to check whether a diagnostic has been requested for output. If
a diagnostic has not been requested, and if it is not required for other
purposes, then the model must avoid computing its value.

Several science schemes have dedicated modules to initialise and output
diagnostics (steps 2 and 3 of the above list). See the modules in
``um_physics_interface/source/diagnostics/``.

The following sections describe each of the steps in more detail.

Creating a field record
~~~~~~~~~~~~~~~~~~~~~~~

Diagnostics that are computed every time-step should normally be defined in the
``field_def_diags.xml`` file.

.. topic:: Other field definition files

   Other field definition files include the ``lfric_dictionary.xml`` file which
   lists prognostic fields (some of which may also be output as diagnostic
   fields); the ``field_def_initial_diags.xml`` file holding definitions of
   diagnostics that optionally can be output before the first time-step has
   run; and the ``field_def_lbc_diags.xml`` file that supports reading and
   writing of Lateral Boundary Conditions fields.

A field definition looks like this:

.. code-block:: xml

  <field id="convection__shallow_dt" name="shallow_dt"
  long_name="temperature_increment_from_shallow_convection" unit="K
  s-1" grid_ref="full_level_face_grid" />

The components of this definition are:

   * The ``id`` string is used in the model code to identify the diagnostic.
     The naming convention used by the LFRic atmosphere is the section name
     followed by a double-understroke followed by a descriptive name.
   * The name and long name are only seen in the diagnostic output. The names
     may be formally assigned such as by the CF naming convention. In this
     case, the name is the same as the suffix of the ID, but it is not always
     so.
   * The units should be SI units. Again, these are only seen in the diagnostic
     output file.
   * The ``grid_ref`` attribute of this definition describes the domain of the
     field. The example field above is represented in the model as
     a :math:`\mathbb{W}_{theta}` field. Other field types have different
     attributes as shown in the following table.

+-----------------------------------+----------------------------------------+
|  Model field type                 |  Domain attributes                     |
+===================================+========================================+
|  :math:`\mathbb{W}_{3}`           |  ``grid_ref="half_level_face_grid"``   |
+-----------------------------------+----------------------------------------+
|  :math:`\mathbb{W}_{theta}`       |  ``grid_ref="full_level_face_grid"``   |
+-----------------------------------+----------------------------------------+
|  :math:`\mathbb{W}_{2v}`          |  ``grid_ref="full_level_face_grid"``   |
+-----------------------------------+----------------------------------------+
|  :math:`\mathbb{W}_{2h}`          |  ``grid_ref="half_level_edge_grid"``   |
+-----------------------------------+----------------------------------------+
|  Single-level field               |  ``domain_ref="face"``                 |
+-----------------------------------+----------------------------------------+
|  Multi-data field                 |  ``domain_ref="face"``                 |
|                                   |  ``axis_ref="<multidata type>"``       |
+-----------------------------------+----------------------------------------+

A multi-data field is often called a tiled field, and contains more than one
related quantity. For multi-data fields, the ``<multidata type>`` text would
be replaced by one of the multidata field types used in the model and defined
in the ``axis_def_main.xml`` file in the ``lfric_atm/metadata`` directory. For
example the following field is on surface tiles.

.. code-block:: xml

    <field id="surface__throughfall" name="throughfall_rate"
    long_name="canopy_throughfall_flux" unit="kg m-2 s-1"
    domain_ref="face" axis_ref="surface_tiles" />

The number of quantities in each type of multi-data field is defined within the
application.

Initialising the field
~~~~~~~~~~~~~~~~~~~~~~

Initialising the field relates to defining the LFRic function space that the
field lives on rather than initialising the values held in the field.

If a field is not available to hold the diagnostic data, then one must be
declared local to the diagnostic routine and initialised to be the correct
field type.

The following code is from an existing science scheme algorithm. It declares
some fields and passes them to the scheme's diagnostic initialisation
procedure.

.. code-block:: fortran

    type( field_type ) :: soil_moisture_content
    type( field_type ) :: grid_canopy_water
    type( field_type ) :: throughfall
    type( field_type ) :: grid_throughfall

    call initialise_diags_for_jules_soil(soil_moisture_content,  &
                                         grid_canopy_water,      &
                                         throughfall,            &
                                         grid_throughfall)

The ``initialise_diags_for_jules_soil`` procedure calls the LFRic atmosphere
``init_diag`` function:

.. code-block:: fortran

    soil_moisture_content_flag = init_diag(soil_moisture_content,        &
                                           'soil__soil_moisture_content')
    grid_canopy_water_flag     = init_diag(grid_canopy_water,            &
                                           'surface__grid_canopy_water')
    grid_throughfall_flag      = init_diag(grid_throughfall,             &
                                           'surface__grid_throughfall')

The ``init_diag`` function does the following steps:

#. Checks if the diagnostic needs to be computed this time-step.
#. If the diagnostic needs to be computed, the field is initialised to the
   right function space type. The function space type is determined from the
   domain information in the field record that was added to the ``iodef.xml``
   file according to the table above. The name of the field is set to the
   string value passed into the function.
#. If the diagnostic does not need to be computed, it still initialises the
   field with metadata. But to save memory, instead of the field holding its
   own data array, its data array pointer is pointed to a dummy
   ``empty_real_data`` field provided by the application. Fields cannot be
   left uninitialised as they would cause model failures if passed through the
   PSy layer as the PSy layer will try to extract their metadata.
#. The ``init_diag`` function returns ``.true.`` if the diagnostic is needs to
   be output, and ``.false.`` otherwise.

Sometimes a diagnostic needs to be computed even when it is not required for
output because of dependencies on other diagnostics that `are` required. An
optional argument to ``init_diag`` can be used to ensure a field is properly
initialised even if there is no requirement to output the diagnostic. The
following code initialises the ``throughfall`` field if the diagnostic itself
is required `or` if the ``grid_throughfall`` diagnostic is required.

.. code-block:: fortran

    throughfall_flag = init_diag(throughfall, 'surface__throughfall', &
                                 activate = grid_throughfall_flag)

although the ``throughfall`` field will be properly initialised if the
``grid_throughfall`` diagnostic is required, the ``init_diag`` function will
still return ``.false.`` if the ``throughfall`` diagnostic is not requested.
The return value is used only for deciding whether to write the diagnostic to
the IO system.

Outputting a field
~~~~~~~~~~~~~~~~~~

If the ``init_diag`` function has returned ``.true.`` then the diagnostic needs
to be written to the IO system once it has been computed.

In the LFRic atmosphere model, the output procedure for a set of diagnostics is
usually in the same module as the initialisation procedure. The flag returned
by the ``init_diag`` function is available to both procedures so can be used
to determine whether the diagnostic needs to be written out.

.. code-block:: fortran

    if (throughfall_flag)           call throughfall%write_field()
    if (soil_moisture_content_flag) call soil_moisture_content%write_field()

Note that the ``write_field`` method takes no argument here. The name passed to
XIOS is the field name provided at initialisation time.

Computing a field
-----------------

Between calling the function to initialise fields and outputting the
diagnostics they hold, the diagnostics are computed.

Typically, diagnostics are computed by passing them to PSyclone built-ins and
kernels.

When using built-ins to compute a diagnostic, it is important to avoid calling
the built-in if the ``init_diag`` routine has not fully initialised the
field.

As noted above, the ``init_diag`` routine used by the LFRic atmosphere
associates the data in a field with an ``empty_real_data`` array if the
diagnostic is not required; all such fields are pointed to the same array held
in the application's ``empty_data_mod`` module. Within a kernel, the data
array can be checked to ensure it is `not` associated with this dummy array
prior to attempting to compute the diagnostic:

.. code-block:: fortran

    use empty_data_mod,          only : empty_real_data

    ! <snip>

    if (.not. associated(throughfall, empty_real_data) ) then
      do n = 1, n_land_tile
        do l = 1, land_pts
          throughfall(map_tile(1,ainfo%land_index(l))+n-1) = &
                                           fluxes%tot_tfall_surft(l,n)
        end do
      end do
    end if

Diagnostics from existing fields
--------------------------------

Sometimes, a science scheme will output a diagnostic from a field passed into
the science algorithm. In this case, there is no need to declare and
initialise a local field, but the field still needs to be sent to the
diagnostic system.

Commonly, such fields are prognostics passed into the science scheme within a
field collection. Code like the following will obtain a pointer to the
``canopy_water`` field from the ``surface_fields`` field collection so that
its value can be computed or updated:

.. code-block:: fortran

    type( field_collection_type ), intent(inout) :: surface_fields
    type( field_type ), pointer :: canopy_water

    call surface_fields%get_field('canopy_water', canopy_water)

By default, the ``write_field`` method passes the field name to XIOS which is
matched to the IDs in the ``iodef.xml`` file. For diagnostic output, the
field's name needs to be overridden by passing the name of the diagnostic to
the write method:

.. code-block:: fortran

    ! Prognostic fields
    call canopy_water%write_field('surface__canopy_water')

Passing ``surface__canopy_water`` means the field will be identified as a
diagnostic rather than as the ``canopy_water`` prognostic. It will then be
written to files that include diagnostic requests with that ID.

Note that as there is no call to ``init_diag`` for an existing field, there is
no flag to determine whether or not the field needs to be sent to the IO
system. Calling the write method on a diagnostic that was not requested is not
a problem: the underlying IO system is capable of ignoring the request.

Initial diagnostics
-------------------

The LFRic atmosphere diagnostic definition includes a file called
``field_def_initial_diags.xml`` that defines a set of "initial" diagnostics
which are essentially the prognostic fields before the model has started
running. If requested (by setting ``write_diag=.true`` in the namelist
configuration) these fields are written out as a group at the very start of a
run just after reading the starting conditions into the model prognostic
fields.

The initial diagnostics may be useful to analyse issues where it is believed
one of the fields is wrong just after it is read in.

If a new field is added to the start dump, then a new record can be added to
the XML file which is a copy of the prognostic record(typically included in
the ``lfric_dictionary.xml`` file), but with its ID prefixed with ``init_``.
Explicit code to write the prognostic field as a diagnostic is added to the
``gungho_diagnostics_driver_mod`` module.
