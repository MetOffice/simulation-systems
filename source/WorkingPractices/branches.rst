Create a branch
===============
The source management tool is `FCM <http://metomi.github.io/fcm/doc/>`_, which is based on subversion
but with some subtle differences, both of which are very different from git.

.. Important::

    All projects now use a version branching approach because it exhibits attributes that are well
    aligned to how the models are used.

By exception, head-of-trunk developments will be accepted.
The prime reason for this is to pick up and build on a specific development that
has already been committed since the last version. Needless head of trunk branches may be rejected.

Branch Management using FCM
---------------------------

To create a branch using fcm, use the following command, replacing ``NNN`` with your ticket number,
``project`` with your project identifier (e.g. ``um``, ``jules``, ``lfric``), ``XX.Y`` with your
version number (e.g. ``11.1``) and ``branchname`` with a suitable branch name (not including
the version number):

.. code-block::

    fcm bc -k NNN -t dev branchname fcm:project.x_tr@vnXX.Y

.. tip::

    Choose a sensible, descriptive and preferably unique name for your branch, while being relatively
    short (less than 50 characters).

    Branches named ``vn1.0_fix_bug`` or ``vn12.3_my_test`` aren't especially helpful.

    If you have to create a new branch at a different version to include the same feature, it is a good
    idea to keep the branch names the same; that way it is easier for someone to know that the branches
    are related in the trac repository.

Upon running the ``fcm bc`` command, the user is provided with a text editor window in which to make
comments about their change. The first comment is usually one indicating that a branch has been
created and a brief summary of what it will do:

.. code-block::

   #NNN: Creates a branch to <insert description of change you intend to make>

Where ``NNN`` should be replaced by the ticket number. Saving and exiting the text editor
will produce a message in the terminal asking whether the user really wants to create the branch.
Enter ``y`` to continue.

Checking out a branch to a working copy
---------------------------------------

To check out your branch immediately after creating it, look for the line in the terminal
which starts with ``[info] Created: https://code.metoffice.gov.uk/``. Copy the full URL and
it can then be checked out with

.. code-block::

    fcm co <full branch URL>

Alternatively, or to check out your branch at a later date, use the following command:

.. code-block::

    fcm co fcm:project.x_br/dev/mosrsuser/vnXX.Y_branchname

Here, in addition to the project and version numbers, the user should include their Met Office
SRS user name (e.g. ``joebloggs``) in place of ``mosrsuser``.

.. Note::

   FCM allows the creation of branches in one of three types: development (abbreviated to dev),
   test and package (abbreviated to pkg). Branches which contain code intended for the
   trunk of a project should be of the dev type. Package branches are intended for grouping
   multiple code changes together into a single package, while the use of test branches will
   be covered later in :ref:`testing`.

