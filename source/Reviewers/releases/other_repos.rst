.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _small_repo_release:

Other Repositories
==================

.. note::

  "Simulations Systems release tag" below refers to a tag of ``YYYY.MM.X``
  format.

1. Apply a Simulation Systems release tag to SimSys_Scripts.

2. Create a UKCA branch updating the SimSys_Scripts tag in the dependencies.yaml
   and get this reviewed and committed.

3. Follow the process of updating :ref:`Stable and Main<github-releases>` for
   these repositories:

   * ukca
   * casim
   * socrates
   * moci
   * mule (if not already done as part of a release)
   * shumlib (if not already done as part of a release)

4. Apply a Simulation Systems release tag to each of:

   * ukca
   * casim
   * socrates
   * moci
   * um_aux
   * socrates-spectral
   * gcom
   * rose_picker
   * mule (if not already done as part of a release)
   * shumlib (if not already done as part of a release)

5. Send an email to all repository owners to let them know that the repository has
been tagged.


