.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _stash_browser:

Stash Browser
=============

* Get a copy of the UM at release and from the top level run,

  .. code-block::

    ./admin/stashbrowser/stashweb -i rose-meta/um-atmos/HEAD/etc/stash/STASHmaster/STASHmaster_A -o UMXXY_STASHweb

  substituting the version for ``XXY``.
* Login as the UM shared account
* Copy the ``UMXXY_STASHweb`` directory created earlier to
  ``$UMDIR/public_html/frozen/XX.Y/stash_browse``
* Check everything looks right at https://wwwspice/~umadmin/stashtech.html


