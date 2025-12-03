.. -----------------------------------------------------------------------------
    (c) Crown copyright Met Office. All rights reserved.
    The file LICENCE, distributed with this code, contains details of the terms
    under which the code may be used.
   -----------------------------------------------------------------------------

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
to create a `GitHub account
<https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_.
Please visit `<https://github.com/signup>`_ to create an account.

`Multi Factor Authentication
<https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication>`_
should also be enabled. This will be a requirement to accesses certain
repositories, but is encouraged for all users. When signed in, account security
settings can be found at `<https://github.com/settings/security>`_.

.. important::

    Certain repositories with more restrictive licencing (eg. UM) will remain
    internal to the Met Office github organisation. To access these you will
    need to be a member of the organisation. Internal employees can request to
    be added via Service Now.

Before starting to use GitHub, you will also need to configure your `user name
<https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git?platform=linux>`_
and `commit email address
<https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address>`_.

.. code-block::

    git config --global user.name "User Name"
    git config --global user.email "User Email"

    # Verify
    git config --global user.name
    git config --global user.email

.. tip::

    Github has functionality that can keep your email address private.

    * Navigate to `<https://github.com/settings/emails>`_
    * Enable the **Keep my email addresses private** setting. This should
      generate a unique noreply email address for you, which will look like
      ``ID+username@users.noreply.github.com``.
    * Use this email address instead in the command above.

SSH Key Setup
-------------

.. important::

    Simulation Systems test suites will by default attempt to clone remote
    sources via ssh. Therefore setting up ssh keys is recommended.

    If ssh isn't available (eg. shared accounts), then it is possible to use the
    option ``-S USE_MIRRORS=true`` which will use local git mirrors if available
    (see :ref:`testing` for more details) or ``-S USE_TOKENS=true`` which will
    use a GitHub Personal Access Token (see :ref:`below <github_pat>`). Access
    from Monsoon will require using a PAT.

You will require a way of `authenticating with GitHub from git
<https://docs.github.com/en/get-started/git-basics/set-up-git#authenticating-with-github-from-git>`_.
One way to do this is via ssh keys. For creating and adding a new ssh key to
GitHub, `see the GitHub documentation
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_.
In order to use this ssh key with MetOffice organisations, it must be authorised
If you are a member of the MetOffice GitHub organisation you will need to
authorise the key for single sign on access. First, ensure you are part of the
MetOffice organisation, and then `configure the SSH key for SSO
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

For instructions please see the GitHub documentation on `setting up a
verification key
<https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification>`_.
If you have setup an ssh key for authenticating, then this can be reused for
signing.

.. tip::

    Run ``git config --global commit.gpgsign true`` in order to automatically
    sign each commit.

There are numerous ways to set up signature verification. To use SSH key for signing, then you can configure your git repositories, either individually, as per this guide, or using `git config --global` if you are happy to have one configuration for all repositories.

It is recommended to use your `ID+username@users.noreply.github.com` email for this.

At https://github.com/settings/keys :
* add `New SSH key`
* Select `signing key` for `Key type`
* Add public key that you are using for authentication.

Then configure git locally at the command line:

.. code-block::

    # create a configuration location for git
    mkdir ~/.config/git`
    # create a configuration for allowed signers - this only needs to be done once.
    # substituting your git no reply email and your own ssh key
    echo "ID+username@users.noreply.github.com $(cat ~/.ssh/{correct-ssh-key.pub})" > ~/.config/git/allowed-signers

    # This assume a by-respoitory configuration, and doesn't use `git config --global`
    cd {aGitRepo}
    git config gpg.format ssh
    git config user.signingkey {/path/to/key}
    git config gpg.ssh.allowedSignersFile ~/.config/git/allowed-signers
    git config commit.gpgsign true

From then on new commits should be signed.
One can retrospectively change commits with a `git rebase -i HEAD~{N}` and some commit editing, if required.

To check this is working locally, then:

.. code-block::

    git log --show-signature

To check that this is working on Github, then push a commit to a branch on Github, then browse to the commit list.
There should be a green `Verified` label beside each commit.

gh Command Line Interface
-------------------------

.. tip::

    The gh command line documentation is available at
    `<https://cli.github.com/manual/>`_.

The ``gh`` command line is a useful tool for interacting with remote
repositories. Where appropriate we have given options for performing tasks with
``gh`` as well as other methods.

To authenticate, run ``gh auth login`` and follow the instructions which will
involve logging into GitHub via a web browser. See the gh manual (linked above)
for details of authenticating.

.. _github_pat:

Github Personal Access Tokens
-----------------------------

Using GitHub tokens is optional for most test suites, as SSH authentication is
used by default. However, Monsoon users must use GitHub tokens because SSH
access to GitHub is unavailable from Monsoon.

To use Personal Access Tokens (PATs), store them in a git credentials file,
typically ``~/.git-credentials``. Restrict access to this file and configure
git to use it:

.. code-block:: shell

    touch ~/.git-credentials
    chmod 0600 ~/.git-credentials
    git config --global credential.helper 'store --file ~/.git-credentials'

Next, `create a Classic Token
<https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic>`_.
To read from or write to a repository, ensure your token has at least the
``repo`` scope. For security reasons, avoid using tokens without an expiry
date. If you are a member of the MetOffice GitHub organisation, authorise your
token for use with the MetOffice Single Sign On. See the GitHub documentation
for details: `Authorizing a personal access token for use with Single Sign-On
<https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/authorizing-a-personal-access-token-for-use-with-single-sign-on>`_.

.. important::

    Make sure to create a Classic Token, rather than a Fine Grained token, as
    these are required for authenticating with the single sign on.

Once created, be sure to copy the generated token as this will not be available
again. Add the token to the git credentials file in the following format,

.. code-block:: shell

    echo "https://<gh-username>:<PAT>@github.com" >> ~/.git-credentials

To use your token to authenticate with GitHub when running the :ref:`rose-stem
suite <github_testing>`, include the command line option ``-S USE_TOKENS=true``.
For Monsoon users, this option is automatically enabled.
