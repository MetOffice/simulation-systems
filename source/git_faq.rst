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
