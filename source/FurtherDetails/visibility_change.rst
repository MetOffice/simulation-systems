.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

.. _visibility_change:
Changing fork visibility
========================

Technical Guide: Re-linking to a Public Repository
--------------------------------------------------

Once the repository is public, contributors must re-establish their forks to continue submitting pull requests.

**Step 1: Create a new public fork (you will need to delete or rename existing private fork)**
    1. Navigate to the now public repository
    2. Click the Fork button int the top-right corner to create a new fork under your account

**Step 2: Update Local Remotes**
In your existing local clone, you must update your remote URLs to point to
the new public upstream and your new fork. Use the following commands:

.. code-block::sh

   # 1. Update the 'upstream' remote to point to the new public repository
   git remote set-url upstream git@github.com:MetOffice/<repo>
   # 2. Update your 'origin' remote to point to your NEW public fork
   git remote set-url origin git@github.com:<user>/<repo>
   # 3. Verify the changes
   git remote -v

**Step 3: Migrating unfinished work**
If you have work in progress on a branch from your old private fork, you can push it to your new public fork easily:

code-block::sh
   # Switch to your working branch
   git checkout feature-branch-name
   # Push the branch to your new public fork (origin)
   git push -u origin feature-branch-name

**Step 4: Re-submit Pull Requests**
As existing PRs will be closed or disconnected,
you will need to `re-submit any open PRs <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork>`_
from your new public fork.
