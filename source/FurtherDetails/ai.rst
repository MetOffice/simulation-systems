.. _ai:

AI Policy
=========

Please ensure that when using Generative AI tools, appropriate guardrails are
in place and contributions have correct attribution. For Met Office
contributors, this includes adhering to the ​Use of Generative AI policy.
Contributors from other institutions should check if their institution has
similar policies, and follow the local policy.

Code where Generative AI tools have been used needs to have clear attribution to
meet the Met Office Generative AI policy. This includes attribution in the
​commit message and in each modified file. Any file where a modification has been
made with Generative AI assistance must have a comment immediately before the
module level docstring, containing:

.. code-block::

    # Some of the content of this file has been produced with the assistance of
    <Generative AI tool name>."

where ``<Generative AI tool name>`` should be replaced with the specific name of
the tool such as ``<Institution Name> Github Copilot Enterprise`` (e.g. Met
Office Github Copilot Enterprise), ``Github Copilot Personal``,
``ChatGPT GPT-4``, etc. For Met Office contributors, Met Office Github Copilot
Enterprise is the only approved Generative AI tool.
