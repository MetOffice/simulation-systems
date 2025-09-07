.. _partner_testing:

Partner Testing
===============

This is intended to allow partners to determine if there are any undetected
problems with the head of the UM trunk (and its dependencies) before the
release process gets started in earnest.

The partner testing period should be 72 hours (3 working days). All tickets
affecting the main source code should be committed (to all repos) but limited
scope changes, eg. to just the Met Office site, can still go on.

* Open a pre-release testing ticket to record responses, issues etc (eg. see
  `UM:#7795 <https://code.metoffice.gov.uk/trac/um/ticket/7795>`__.)
* Add the latest UM, Jules, UKCA, Casim, Socrates revisions to the ticket.
* Email the representatives at each UM partner site to them to test. A list of
  emails can be found at, `UM Partner Testing Emails
  <https://code.metoffice.gov.uk/trac/um/wiki/UMPartnerTesting>`__ (note, that
  page should remain private to the Met Office).

  * You may need to set the international options in advanced email sending
    options to use Unicode (UTF-8) as the preferred encoding for outgoing
    messages to ensure that all international partners receive the email.
    Change this setting if you receive bounced emails during partner testing.

