# Simulation Systems

[![Docs](https://github.com/MetOffice/simulation-systems/actions/workflows/publish_wps.yaml/badge.svg)](https://github.com/MetOffice/simulation-systems/actions/workflows/publish_wps.yaml)

This repository contains the working practices documentation common to the
various
[simulation and modelling repositories](https://github.com/MetOffice/simulation-systems/wiki)
owned by the Met Office.

The documentation in the repository can be compiled in different ways.

> [!NOTE]
> Optional system dependencies for PDF generation may require LaTeX
> distributions and other third-party libraries.

## Setup environment

You can set up the environment ro build and deploy the documentation using any
of the following methods:

### 1. Using uv

A quick and clean way to get the package dependencies is via the
[uv](https://docs.astral.sh/uv/) package manager.

```shell
git clone https://github.com/MetOffice/simulation-systems
cd simulation-systems

# Install dependencies (see pyproject.toml) in project .venv
uv sync
```

### 2. Using pip

If you have Python 3.11 or higher installed (`sphinx==8.2.3` required), you can
use pip:

```shell
git clone https://github.com/MetOffice/simulation-systems
cd simulation-systems

<path/to/python3.11+> -m venv .venv
source .venv/bin/activate
pip install .
```

### 3. Using conda

```shell
git clone https://github.com/MetOffice/simulation-systems
cd simulation-systems

conda env create -f env.yml
conda activate sphinx_doc_env
```

## Build documentation

```shell
# For uv environment
uv run make clean html

# For pip or conda environments
make clean html
```

After building, the HTML documentation can be found in the `build/html/`
directory of your local repository. You can open the documentation in any web
browser.

**Met Office users** can skip build step above and deploy the documentation
directly to a predefined location:
`~/public_html/simulation-systems/<branch-name>/html/`

```shell
uv run make clean deploy  # uv env
# OR
make clean deploy  # pip or conda env
```

## Contributing

Please follow the project's [Code of Conduct](CONTRIBUTING.md)

The documentation is written in Sphinx markup. To propose changes:

1. Create an issue detailing the required changes.
2. Create a branch in your clone of this repository, linking it to your issue.
3. Regularly build your changes as described above.

Once satisfied, create a pull request and request a review from
[MetOffice/ssdteam](https://github.com/orgs/MetOffice/teams/ssdteam).
