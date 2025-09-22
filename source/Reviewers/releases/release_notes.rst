.. _release_notes:

Release Notes
=============

The below shows the trac release notes template previously used. This will want editing and the exact location needs deciding for the move to github. However it can be used as an initial guide to the sort of information included.

.. code-block::

    [[PageOutline]]
    -----
    = UM vnXX.Y User Release Notes =

    == Summary ==

    * Release date:
    * Number of tickets:

    === Science highlights ===

    === Technical highlights ===

    === Optimisation highlights ===

    == Known Issues ==

    None

    == Revisions and Keywords ==

    || Repository || !Keyword/Revision ||
    || [browser:main UM]                                                    || vnXX.Y = NNNN ||
    || [https://code.metoffice.gov.uk/trac/jules/browser/main JULES]        || vnA.B = umXX.y = NNNN ||
    || [https://code.metoffice.gov.uk/trac/monc/browser/casim CASIM]        || etc ||
    || [https://code.metoffice.gov.uk/trac/socrates/browser/main SOCRATES]  ||     ||
    || [https://code.metoffice.gov.uk/trac/ukca/browser/main UKCA]          ||     ||
    || [browser:aux Aux]                                                    ||     ||

    GCOM and SHUMlib installations should be built using revisions:

    || Repository || !Keyword/Revision ||
    || [https://code.metoffice.gov.uk/trac/gcom/browser/main GCOM]          || vnXX.Y = NNNN ||
    || [https://code.metoffice.gov.uk/trac/utils/browser/shumlib SHUMlib]   || YYYY.MM.N = NNNN ||

    Note that SHUMlib may not be released at every UM release.

    For testing purposes, the LFRic Apps and MOCI repositories:

    || Repository || Revision ||
    || [browser:main/trunk/rose-stem/rose-suite.conf MOCI]           ||  NNNN  ||
    || [https://code.metoffice.gov.uk/trac/lfric_apps/browser/main LFRic Apps] ||  vnA.B = umXX.Y = NNNN ||

    Required for rose-stem:

    {{{#!comment
    Obtain these by grepping, for example:
    grep -r CYLC_VERSION ~frzz/cylc-run/um_heads_nightly_YYYY-MM-DD/log/job
    }}}

    * Rose vn YYYY.MM.N
    * Cylc vn YYYY.MM.N

    == Ticket Overview ==

    * Tickets marked as closed/fixed below may not be associated with a [log:main/trunk trunk commit]
    * Only tickets with a UM element are displayed below. Sub-repositories may contain additional standalone tickets that will have been implicitly tested and included in the release.

    [[TicketQuery(milestone^=UMXX.Y (MMM-YY),status=closed,resolution=fixed,format=table,col=summary|reporter|keywords)]]

    == Platforms ==

    Testing:
    * Met Office SPICE: [wiki:ReleaseNotesXX.Y/ReleaseTestingAZSPICE]
    * Met Office EX1A: [wiki:ReleaseNotesXX.Y/ReleaseTestingEX1A]


For the highlights section:

* Contact HPC Optimisation team (usually AM) to request details for the optimisation section
* Take some time to think about the 'big picture' relevance of tickets for the science and technical highlights
* Copy the 'head of trunk' section and paste underneath, changing the section title to the release.
* Paste trac.logs into the relevant sub-pages. You'll likely be able to use some nightly testing runs.