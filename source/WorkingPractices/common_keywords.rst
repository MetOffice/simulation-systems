.. _keywords:

Commonly-Used Keywords
======================

The following table lists some common keywords you may sometimes
see:

+--------------+------------------------------------------------+-----------------------------------------------+
| Keyword      | Usage                                          | Notes                                         |
+==============+================================================+===============================================+
| collab:      | Indicates that the ticket has been authored    | Use form ``collab:<orgname>``                 |
|              | by someone who is not 100% employed            | e.g. ``collab:niwa``, ``collab:oxford``       |
|              | by the Met Office                              |                                               |
+--------------+------------------------------------------------+-----------------------------------------------+
| blocks:      | Code change is blocking the numbered ticket    | e.g. blocks:#1234                             |
|              | from going on to the project's trunk           | Not used by LFRic Core as they have a         |
|              |                                                | "blocked by" item in their ticket options.    |
+--------------+------------------------------------------------+-----------------------------------------------+
| blockedby:   | Code change is blocked by the numbered ticket  | e.g. blockedby:#6789                          |
|              | from going on to the project's trunk           | Not used by LFRic Core as they have a         |
|              |                                                | "blocked by" item in their ticket options.    |
+--------------+------------------------------------------------+-----------------------------------------------+
| kgo          | Indicates the change requires new kgo          | Includes when a new job is added to the       |
|              | installing (change in answers);                | project's rose stem suite                     |
|              | See :ref:`KGO <kgo>`.                          |                                               |
+--------------+------------------------------------------------+-----------------------------------------------+
| macro        | Indicates the change includes an               |                                               |
|              | upgrade macro                                  |                                               |
+--------------+------------------------------------------------+-----------------------------------------------+
| doc          | Indicates that the change includes             |                                               |
|              | documentation updates                          |                                               |
+--------------+------------------------------------------------+-----------------------------------------------+
| SR:<name>    | Denotes person who will SciTech                | Optional for reviews outside of the SSD       |
|              | review the change                              | team; Added later in development              |
+--------------+------------------------------------------------+-----------------------------------------------+
| CR:<name>    | Denotes person who will CodeSys                | Added when the reviewer is assigned.          |
|              | review the change                              |                                               |
+--------------+------------------------------------------------+-----------------------------------------------+
| linked:um    | Indicates that the change has a linked         |                                               |
|              | ticket with the code base specified by         |                                               |
| linked:jules | the keyword. These are just examples - all     |                                               |
|              | linked repositories should be included.        |                                               |
| linked:core  |                                                |                                               |
|              |                                                |                                               |
| linked:apps  |                                                |                                               |
|              |                                                |                                               |
| linked:ukca  |                                                |                                               |
+--------------+------------------------------------------------+-----------------------------------------------+
