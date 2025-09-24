.. _gh_authorisation:

Setting Up Github Authorisations
================================

Initial Setup
-------------

.. note::

    The topics on this page are all more completely covered in other
    documentation, which should be used first when finding any issues. Common
    steps required to begin working with simulation systems repositories are
    described here however. We will endeavour to provide links to other
    documentation throughout.

All users looking to interact with the simulation system repositories, will need
to create a `github account
<https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.

`Multi Factor Authentication
<https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication>`_
should also be enabled. This will be a requirement to accesses certain
repositories, but is encouraged for all users.

.. admonition:: todo

    External access to MO org

.. important::

    To access some private repositories (eg.
    UM) will require access to the MetOffice github organisation. Internal Met
    Office employees can request this through ServiceNow.

Before starting to use github, you will also need to configure your `user name
<https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git?platform=linux>`_
and `commit email address
<https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address>`_.

.. code-block::

    git config --global user.name "User Name"
    git config --global user.email "User Email"

SSH Key Setup
-------------

.. important::

    Simulation Systems test suites will by default attempt to clone remote
    sources via ssh. Therefore setting up ssh keys is recommended.

    If ssh isn't available (eg. shared accounts), then it is possible to use the
    option ``-S USE_MIRRORS=true`` which will use local git mirrors if available
    (see :ref:`testing` for more details).

You will require a way of `authenticating with github from git
<https://docs.github.com/en/get-started/git-basics/set-up-git#authenticating-with-github-from-git>`_.
One way to do this is via ssh keys. For creating and adding a new ssh key to
github, `see the github documentation
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_.
In order to use this ssh key with MetOffice organisations, it must be authorised
for single sign on access. First, ensure you are part of the MetOffice
organisation, and then `configure the SSH key for SSO
<https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/authorizing-an-ssh-key-for-use-with-single-sign-on>`_.


Verified Commits
----------------

.. important::

    Ensure you have setup verified commits before beginning work on a branch
    that is targetting being merged to main.

    Any branches with unverified commits will require rebasing before review.

Verified (or signed) commits are a way of ensuring the identity of the committer
by signing the commit with a form of verification key, eg. ssh or gpg.
Simulation Systems repositories will all be set up to enforce verified commits.

For instructions please see the github documentation on `setting up a
verification key
<https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification>`_.
If you have setup an ssh key for authenticating, then this can be reused for
signing.

.. tip::

    Run ``git config --global commit.gpgsign true`` in order to automatically
    sign each commit.


gh command line
---------------

.. tip::

    The gh command line documentation is available at
    `<https://cli.github.com/manual/>`_.

The ``gh`` command line is a useful tool for interacting with remote
repositories. Where appropriate we have given options for performing tasks with
``gh`` as well as other methods.

To authenticate, run ``gh auth login`` and follow the instructions which will
involve logging into github via a web browser. See the gh manual (linked above)
for details of authenticating.
