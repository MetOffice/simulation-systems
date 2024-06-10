.. _lfric_diag:

LFRic Atmosphere Diagnostics
============================

The diagnostic system for the LFRic atmosphere model is dependent on
the XIOS library. Diagnostic outputs are defined in the ``iodef.xml``
required by XIOS to define a lot of the input and output requirements
of an application.

Key aspects of the contents of an ``iodef.xml`` file are as follows:

  #. Each field that an application is capable of output will have a
     ``field`` record that provides a text identity of the field, the
     domain of the field, and various other bits of information such
     as the units of the field.
  #. The domain of the field can relate to the spatial domain, but can
     also relate to non-physical dimensions. For example, multiple
     types of vegetation can be stored in a single field with one of
     the axes of the field relating to each type of vegetation.
  #. Diagnostics are only useful if they are output. The ``iodef.xml``
     file contains lists of diagnostic output requests, typically
     grouped into different files. XIOS supports various
     post-processing operations.

.. topic:: Comparing with the Unified Model STASH system

   Users familiar with the UM's STASH system will know that for each
   available diagnostic, multiple output requests can be made, each of
   which can undergo different time or spatial processing and can be
   sent to a different file. Further, the UM system supports a
   graphical user interface that can edit the lists of requests for a
   given application.

   XIOS has similar and more extensive processing capabilities, but at
   the moment, no user interface support has been provided for users
   of the LFRic atmosphere model. Requests have to be constructed by
   editing the XML files that are used to create the ``iodef.xml``
   file that is read by the application.

XIOS is a highly complex and flexible parallel IO system with
post-processing capabilites. It is developed at IPSL.

.. caution::

   While it would be possible to write a set of complex diagnostic
   requests using all the features of XIOS, people should be cautious
   of the possibility that future developments of the LFRic atmosphere
   user environment may not support all the flexibility
   required. Furthermore, the underlying XIOS software is complex, and
   it is possible to create a simple workflow that turns out to be
   unreliable or that imposes high computation costs on the model.


Adding a new diagnostic
-----------------------

To add a diagnostic for potential output from the LFRic atmosphere
model a developer needs to do the following:

#. Create a ``field`` record in the relevant XML file that is used to
   create the XIOS ``iodef.xml`` file. The record should provide a text
   ID, a name and long name, units and domain information.

   * The ID string is used in the model to identify the diagnostic.
   * The name and long name are only seen in the diagnostic
     output. The names may be formally assigned such as by the CF
     naming convention.
   * The units should be SI units. Again, these are only seen in the
     diagnostic output file.
   * The domain information depends on the type of field. More details
     will be provided later.

#. Add code to initialise the field: the LFRic atmosphere includes a
   routine to support this operation.
#. Add code to compute the diagnostic `if the diagnostic has been
   requested` or if it is needed to compute another diagnostic that
   is requested. There is no point in computing a diagnostic if it is
   not required.
#. Add code to write the diagnostic to the LFRic atmosphere IO interface.
