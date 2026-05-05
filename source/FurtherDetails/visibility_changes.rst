.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _visibility_changes:

Changing fork visibility
========================

Technical Guide: Re-linking to a Public Repository
--------------------------------------------------

Once the repository is public, contributors must re-establish their forks to continue submitting pull requests.

#. Create a new public fork (you will need to delete or rename existing private fork)**
    1. Navigate to the now public repository
    2. Click the Fork button int the top-right corner to create a new fork under your account

#. Update Local Remotes
    In your existing local clone, you must update your remote URLs to point to
    the new public upstream and your new fork. Use the following commands:

    .. code-block::sh

    # 1. Update the 'upstream' remote to point to the new public repository
    git remote set-url upstream git@github.com:MetOffice/<repo>
    # 2. Update your 'origin' remote to point to your NEW public fork
    git remote set-url origin git@github.com:<user>/<repo>
    # 3. Verify the changes
    git remote -v

#.  Migrating unfinished work
    As existing PRs will be closed or disconnected,
    you will need to re-submit any open PRs from your new public fork.

    The "detached" state is a security feature to isolate private forks when the
    upstream parent becomes public. Only GitHub staff have the administrative
    privileges required to manually re-link the repository network while
    preserving existing PR data and history.

    One option is to make sure any work you wish to preserve is in a clone of your
    fork. Then recreate the fork from upstream using the same name as before.
    Pushing from your clone will connect to the new fork. However this will delete
    any pull requests you had open from the previous fork.

    If you already have a lots of develop branches/PRs, its probably best to
    contact `GitHub Support and Submit a ticket
    <https://support.github.com/contact?legacy&subject=Attach%20Fork&tags=rr-forks>`_
    to reattach your fork. Select your personal account from the drop down menu
    (as that is where your fork is, not the enterprise account) and use the
    following message:

    My upstream private repo became public, which detached my fork. I have open
    PRs I need to preserve. Please reattach my fork to the original network.

    Upstream URL: https://github.com/MetOffice/{repo-name}

    Fork URL: https://github.com/{user}/{repo-name}

    This process should usually get resolved within a day.
