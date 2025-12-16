# GitHub Copilot Instructions for simulation-systems

Welcome to the `simulation-systems` project! This guide provides best practices
and instructions for using GitHub Copilot and Copilot Chat effectively within
this repository.

## General Guidelines

- **Use Copilot for:**
  - Writing and editing documentation (reStructuredText `.rst` files)
  - Generating code snippets or templates for documentation
  - Refactoring or improving documentation structure
  - Answering questions about Sphinx, reStructuredText, and documentation
    workflows
- **Do NOT use Copilot for:**
  - Generating legal, licensing, or policy documents without review
  - Adding or modifying files outside the documentation scope unless explicitly
    requested
  - Committing changes directly to `main` without review

## Documentation Structure

- All documentation is located in the `source/` directory.
- Use `.rst` (reStructuredText) format for all documentation files.
- Custom templates and static assets are in `source/_templates/` and
  `source/_static/`.
- Follow the style and structure of existing documentation when adding new
  content.

## Writing and Editing Documentation

- When creating new documentation, use clear section headings and follow the
  Sphinx/reStructuredText conventions.
- For technical documentation, include code blocks, examples, and
  cross-references where appropriate.
- Use Copilot Chat to:
  - Generate outlines for new documentation
  - Suggest improvements to existing docs
  - Answer questions about Sphinx directives and configuration

## Code of Conduct and Contribution

- Review the `CONTRIBUTING.md` and `source/FurtherDetails/code_of_conduct.rst`
  before making contributions.
- All contributions should be made via pull requests and reviewed by a project
  maintainer.

## Copilot Chat Prompts

- Be specific in your prompts (e.g., "Add a section on running tests in
  `source/Development/testing.rst`").
- Request code or documentation examples as needed.
- Ask for explanations of Sphinx or reStructuredText features if unsure.

## Coding Standards

- Follow the existing documentation style and formatting.
- Use consistent terminology and phrasing throughout the documentation.
- Follow PEP 8 guidelines for any Python code snippets included in the
  documentation.
- Use `ruff` for linting any Python code snippets.
- Use `sphinx-lint` for checking reStructuredText documentation quality.
- Use `doc8` for spell checking and line lengths in documentation files.
- Ensure proper formatting of reStructuredText files.

## Limitations

- Copilot suggestions are not always correct-review and edit as needed.
- Do not use Copilot to generate sensitive, proprietary, or confidential
  information.

## Getting Help

- For questions about Copilot usage, ask in Copilot Chat or consult the
  [GitHub Copilot documentation](https://docs.github.com/en/copilot).
- For project-specific questions, refer to the `README.md` or open an issue.

---

_This file provides guidance for using GitHub Copilot in the
`simulation-systems` project. Please keep it up to date as project practices
evolve._
