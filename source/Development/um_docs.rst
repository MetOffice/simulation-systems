.. _umdp:

Unified Model Documentation Papers (UMDPs)
==========================================

The UM documentation papers and online training are maintained in the
MetOffice/um_doc repository, separate from the UM code. Changes to the
documentation will therefore require their own pull request.

The latest documentation gets automatically built by CI.
The same action will run when a pull request is opened to ensure that the
requested changes builds correctly. The build script is available in the
repository and should be used to test that the finished documentation looks as
you intend before submitting it for review.

Standards
---------

As there are standards for coding, similarly there are a few rules for the
UM Document Papers.

#. Latex is the default file format.

#. A pair of UMDP document classes are supplied in the um_doc repository for
   use with all UMDPs to maintain a consistent style.

   * You must use one of these two document classes, no exceptions.

   * Unlike some other in-built Latex document classes the UMDP classes do not
     support pass-through of options to their parent class, this is intentional
     and will not be changed.

   * The preamble requires the following setup commands to be present:

     *  **\\title** The title of the UMDP (Please avoid very long titles - use the
        optional subtitle command instead)

     *  **\\paperno** The UMDP identification number (3 characters, should match
        the directory name), if creating a new UMDP please request a new
        number (see below)

     *  **\\umversion** The version of the UM the document is valid for (e.g. "9.2"
        - This should ideally be the same as the documentation release as even
        UMDPs with no changes should be reviewed each release-cycle)

     *  **\\owner** The official owner and point of contact for the UMDP (This
        might be different to the contributing authors who may be listed by the
        optional command below)

   * The preamble also supports the following optional commands:

     * **\\subtitle** May be used to provide elaboration on the title (or a way of
       shortening it if required)

     * **\\author** The list of contributing authors (which may or may not include
        the UMDP owner)

     * **\\titlecontent** This is a flexible space which appears on the title page
        and is left to the author's discretion - it could be used to place a
        short abstract-style paragraph on the cover, to contain footnote
        references to the list of authors or any other purpose.


#. Any package available in an unmodified TexLive (version 2018) installation
   is permitted, provided it doesn't alter the page layout and other
   presentational elements of the UMDP document class, or require source
   commands that are too complex/difficult to maintain or for other authors to
   understand (at the discretion of the Code Reviewer / UMDP Librarian/s).

#. Make sure all files required for build are in the repository. No dependency
   shall be stored outside the repository.

   * To ensure the integrity of the UMDP repository it is essential that all
     the required files, source and diagrams to create the documentation are
     included.

   * It is not acceptable to only provide a pdf or html link.

   * It should be possible for our partners to build UMDPs and modify them l
     locally if we are to expect them to contribute to UM development.

   * There is no need to write a Makefile or other code to build each UMDP,
     this is all handled by the build_umdoc.py script. However it identifies
     the top-level document by the presence of the \documentclass command, so
     you should never allow more than one file to contain this command. (See
     other UMDPs for examples; these should be standard across UMDPs.)


Making Changes
--------------

Making changes to the UMDPs follows the same process for setting up a fork,
developing on a branch and reviewing through pull requests as outlined in the
:ref:`working_practices_index`.

The source for the UMDP documents is in the ``source`` folder, in sub-directories
named after the UMDP number of the each document. You should not need to edit
anything outside of the ``source`` directory.

When changing a document the ``Last Updated`` version number must be updated
to reflect the *upcoming* release. This is done by changing `\\umversion{}` in
the documents pre-amble.

To test build the documentation:

.. code-block::

    ./build_umdoc.py XYZ

* XYZ is the UMDP number of your modified document (more that one can
  be specified if you wish)

* The PDF output will be in `output/papers/umdp_XYZ.pdf`

* Build stdout and stderr will be in `output/logs/umdp_XYX_stdout.log`.


.. tip::
    Further details on the build script can by found by directing a browser
    to `web/build.html`
