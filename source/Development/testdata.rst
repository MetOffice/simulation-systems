.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _testdata:

Adding Test Data
================

.. note::

    This page is a placeholder for information about test data. It is not yet
    complete and will be updated in due course.

    *The instructions here are Met Office specific, other sites may manage their
    test data differently.*

.. important:: **Attribution Metadata Policy**

    If the change requires a new or updated file in ``LFRIC_DATA_DIR`` then you
    will need to work with the Information Asset Owner (IAO) to ensure that data
    in ``LFRIC_DATA_DIR`` includes clear attribution and licence metadata.
    Where possible, this should follow existing UM ``ANCILDIR`` conventions (`see
    below <prerequisites-section_>`_), with ``.attribution`` and ``.license``
    files or equivalent NetCDF **global attributes** (at least, ``references``,
    ``license``, ``source``, and ``history``). Attribution must reflect the
    original data source and be provided by the data creators before deployment,
    share, or distribution.

    It is treated as an **Information Asset / licensing requirement**, not just
    a best practice.


For UM related datasets, please Email the `MIAO team <mailto:miao@metoffice.gov.uk>`_
to discuss the best way to share the data.

.. _prerequisites-section:

Prerequisites
-------------

Before adding test data, you should have a good understanding of the change you
are making and the tests you will be adding. You should also have a good
understanding of the codebase and the testing framework you will be using.

Licenses
~~~~~~~~

All files require a licence and a record of where they have come from, both
for legal and auditing purposes. In your request please describe where and how the
data was generated, and the terms and conditions of its licence.

Before any files can be deployed, they must be approved by an IAO and this cannot be done
without information about the licencing terms.

Metadata
~~~~~~~~

Any file requirements should be recorded in or alongside the files being
deployed.

Note that if a source file has a licence that imposes requirements on derived
works, then an ancillary file (or an intermediate file used to generate an
ancillary) does count as a derived work for the purpose of recording metadata.

In cases where a file has been generated from multiple sources, it should be
made clear where each licence/attribution/acknowledgement has come from.

NetCDF Files
^^^^^^^^^^^^

NetCDF files should have the relevant metadata included in the file itself.
The metadata should include the following information:

* If there is a licence, it should be in a ``license`` global attribute as per
  `ESIP Attribute Convention for Data Discovery <https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3#Recommended>`_.

* If there is a paper attribution requirement, the relevant paper(s) should be
  cited in the ``references`` global attribute as per
  `CF conventions <https://cfconventions.org/Data/cf-conventions/cf-conventions-1.11/cf-conventions.html#description-of-file-contents/>`_.

* If there is an organisation attribution requirement, it should be in the
  ``institution`` global attribute (again, as per CF).

* If there is any other attribution requirement (e.g. for an individual), it
  should be in the ``acknowledgement`` global attribute (again, as per ACCD).

* If there are restrictions on usage (e.g. "research only"), these should be in
  a ``restrictions`` global attribute.

Other Files
^^^^^^^^^^^

* Licence should be in an accompanying plain text file with the same name as the
  data file, but with a ``.license`` suffix.

* Attribution should be in an accompanying plain text file with the same name as
  the data file, but with a ``.attribution`` suffix.

* Restrictions on usage (e.g. "research only") should be in an accompanying
  plain text file with the same name as the data file, but with a
  ``.restrictions`` suffix.

If you have questions about the process or concerns about the provenance of the
data you want to include, please engage with the IAO as early as possible to
prevent delays to your change later on.
