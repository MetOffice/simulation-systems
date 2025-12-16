.. _git_faq:

Git Migration FAQ's
===================

.. rubric:: How do I access the repositories?

All of the migrated Simulation Systems repositories are found in the Met
Office organisation. Certain repositories, where licencing allows, have been
made public, so can be viewed by anyone. Other repositories (eg. UM) are
internal to the Met Office organisation. These can be seen if you have access
to the organisation.

.. rubric:: Where are my branches and tickets?

Migration of individual branches and tickets is being left to each developer
to be done on a case by case basis. Please see the :ref:`branch migration
guide <branch_migration>` for advice on migrating an fcm branch to git.

.. rubric:: Why can't I push or create a branch in the repository?

We are managing our repositories using a :ref:`forking <forking>` model,
therefore creating of branches in the central repository is tightly
controlled. Please create your own fork and develop your changes on branches
in there.

.. rubric:: Why won't the rose-stem command work?

The syntax to launch the test suite has changed with the move to git. Please
see our :ref:`testing pages <testing>`.

.. rubric:: Rose-stem is giving the following error while trying to fetch code
  from other repositories: `git@github.com: Permission denied (publickey).`

This is a sign of SSH setup issues. Please see the :ref:`GitHub setup page for
details<gh_authorisation>`, making sure you've covered the following:
* Generate a new SSH key leaving the passphrase empty
* Add your new key to the ssh-agent
* Add your public key to GitHub (using the GitHub CLI or on the website)
* Add a github entry to your ssh config
* Configure the key on GitHub for SSO access
* Test your key with ``ssh -T git@github.com``

.. rubric:: How do I run with an older version?

The entire history of each trunk branch from the MOSRS repository has been
migrated (for the UM this is from vn9.2). If you need a specific release, then
you can checkout the tag of that release, eg. ``git checkout <TAG>``. If you
require a specific commit, you will need to find the relevant hash from the
history of the main branch.

.. rubric:: Why can't I see the full history of Jules and MONC?

Due to licencing issues we were unable to make the history of these
repositories public. We have a copy of the repository with all the previous
releases internal to the MetOffice. Please ask if you need help accessing
that.

.. rubric:: My forked repository got detached from upstream repository following
  visibility change (private to public) upstream.

The "detached" state is a security feature to isolate private forks when the
upstream parent becomes public. Only GitHub staff have the administrative
privileges required to manually re-link the repository network while
preserving existing PR data and history.

One option is to make sure any work you wish to preserve is in a clone of your
fork. Then recreate the fork from upstream using the same name as before.
Pushing from your clone will connect to the new fork. However this will delete
any pull requests you had open from the previous fork.

If you already have a lots of develop branches/PRs, its probably best to
contact GitHub Support and Submit a ticket to reattach your fork with
upstream with the following message:

  My upstream private repo became public, which detached my fork. I have open
  PRs I need to preserve. Please reattach my fork to the original network.

  Upstream URL: https://github.com/MetOffice/{repo-name}
  Fork URL: https://github.com/{user}/{repo-name}

This process should usually get resolved within a day.
