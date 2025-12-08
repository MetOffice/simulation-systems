.. _git_faq:

Git Migration FAQ's
===================

How do I access the repositories?
  All of the migrated Simulation Systems repositories are found in the Met
  Office organisation. Certain repositories, where licencing allows, have been
  made public, so can be viewed by anyone. Other repositories (eg. UM) are
  internal to the Met Office organisation. These can be seen if you have access
  to the organisation.

Where are my branches and tickets?
  Migration of individual branches and tickets is being left to each developer
  to be done on a case by case basis. Please see the :ref:`branch migration
  guide <branch_migration>` for advice on migrating an fcm branch to git.

Why can't I push or create a branch in the repository?
  We are managing our repositories using a :ref:`forking <forking>` model,
  therefore creating of branches in the central repository is tightly
  controlled. Please create your own fork and develop your changes on branches
  in there.

Why won't the rose-stem command work?
  The syntax to launch the test suite has changed with the move to git. Please
  see our :ref:`testing pages <testing>`.

How do I run with an older version?
  The entire history of each trunk branch from the MOSRS repository has been
  migrated (for the UM this is from vn9.2). If you need a specific release, then
  you can checkout the tag of that release, eg. ``git checkout <TAG>``. If you
  require a specific commit, you will need to find the relevant hash from the
  history of the main branch.

Why can't I see the full history of Jules and MONC?
  Due to licencing issues we were unable to make the history of these
  repositories public. We have a copy of the repository with all the previous
  releases internal to the MetOffice. Please ask if you need help accessing
  that.
