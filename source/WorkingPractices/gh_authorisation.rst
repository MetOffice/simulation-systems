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

#TODO - external access to MO org? To access some private repositories (eg. UM)
will require access to the MetOffice github organisation. Internal Met Office
employees can request this through ServiceNow.

.. tip::

    Internal Met Office employees can find additional information on `sharepoint
    <https://metoffice.sharepoint.com/sites/TechnologyCommsSite/SitePages/Tooling/GitHub/GitHub.aspx>`_.

Before starting to use github, you will also need to configure your `user name
<https://docs.github.com/en/get-started/git-basics/setting-your-username-in-git?platform=linux>`_
and `commit email address
<https://docs.github.com/en/account-and-profile/how-tos/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address>`_.

.. code-block::

    git config --global user.name "Mona Lisa"
    git config --global user.email "YOUR_EMAIL"

SSH Key Setup
-------------

You will require a way of `authenticating with github from git
<https://docs.github.com/en/get-started/git-basics/set-up-git#authenticating-with-github-from-git>`_.
One way to do this is via ssh keys. For creating and adding a new ssh key to
github, `see the github documentation
<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent>`_.
In order to use this ssh key with MetOffice organisations, it must be authorised
for single sign on access. First, ensure you are part of the MetOffice
organisation, and then `configure the SSH key for SSO
<https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-single-sign-on/authorizing-an-ssh-key-for-use-with-single-sign-on>`_.







A brief overview of how to set up authorisations to gh for Sim Sys or links to
relevant instructions.

* ssh keys
* verified commits
* gh command line
* Maybe more?
