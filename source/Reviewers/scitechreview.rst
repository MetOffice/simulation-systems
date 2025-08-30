.. _scitech_review:

Science and Technical Review
============================

Purpose of the review
---------------------
The purpose of code review is to ensure that the code does the job it says it
performs, is standards compliant and well documented.

Reviewer responsibilities and checkpoints
-----------------------------------------
The Sci/Tech review template exists to help you think through all the following
areas. A completed :ref:`review template <template>` should be appended to the
ticket once you are finished.

The Science / Technical reviewer should

* Understand the area of code and check that the changeset satisfies the purpose
  of the change.

* Ensure that the code has no unwanted side-effects

* Ensure that the code is written to the standards laid out in `UMDP3 <https://code.metoffice.gov.uk/doc/um/latest/papers/umdp_003.pdf>`_
  or `LFRic Coding Styles <https://code.metoffice.gov.uk/trac/lfric/wiki/LFRicTechnical/CodingStandards>`_.

* Make sure that the in-line documentation is accurate and sufficient.

* Ensure that any related :ref:`external documentation <docs>` is updated as
  necessary.

* Check that the Trac ticket has been completed fully and accurately with
  sufficient detail for others to understand the impact of the change.

* Ensure that testing has been carried out satisfactorily (and recorded on the
  Trac ticket), and that there is no impact for configurations outside the
  required scope of the changeset.

Final decision points and actions
---------------------------------
The science/technical reviewer must demand that non-compliance is corrected
before a change is passed onto the next level of review.

The ticket will likely iterate between the reviewer and the developer during the
review process while retaining it's sci/tech review status. However, the
reviewer has the option to "reject and assign" back to the code author should
the documentation or code not meet the required standards and major
alterations/improvements are required.

Once you are happy that the change is appropriate and correct, complete the
approval section of the Sci/Tech review template and re-assign the ticket to the
system/code reviewer. If need be ask the code author for the agreed system/code
reviewer's name.
