.. _stash_browser:

Stash Browser
=============

* Checkout a copy of the UM at release, ``fcm co fcm:um.xm_tr@vnXX.Y``. Move into the top directory and run,

  .. code-block::

    ./admin/stashbrowser/stashweb -i rose-meta/um-atmos/HEAD/etc/stash/STASHmaster/STASHmaster_A -o UMXXY_STASHweb

  substituting for ``XXY``.
* Login as the UM shared account
* Copy the ``UMXXY_STASHweb`` directory created earlier to ``$UMDIR/public_html/frozen/XX.Y/stash_browse``
* Check everything looks right at https://wwwspice/~umadmin/stashtech.html


