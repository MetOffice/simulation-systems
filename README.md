# Simulation Systems

This repository contains documentation that is common across the many
[simulation and modelling repositories](https://github.com/MetOffice/simulation-systems/wiki)
owned by the Met Office.

## Build the documentation

A quick and clean way to get the package dependencies is via
[uv](https://docs.astral.sh/uv/) package manager.

Ps: Optional system dependencies for PDF generation may require LaTeX
distributions and other third-party libraries.

### 1. Using uv

```shell
git clone https://github.com/MetOffice/simulation-systems
cd simulation-systems

# Install dependencies (see pyproject.toml) in project .venv
uv sync
uv run make clean html

# Verify documentation
firefox build/html/index.html
```

#### Clone anywhere, deploy to user `~/public_html/simulation-systems/<branch-name>`

```shell
git clone https://github.com/MetOffice/simulation-systems
cd simulation-systems

uv sync
uv run make clean deploy
```

Verify documentation (replace `<an.user>` and `<branch-name>` as required):
`https://wwwspice/~<an.user>/simulation-systems/<branch-name>/html`

### 2. Using pip

Alternatively, if your have Python-3.11 or higher installed (`sphinx==8.2.3`
requirement), you can install the dependencies in a virtual environment via pip,
and build the documentation like:

```shell
cd simulation-systems

</path/to/python3.11+> -m venv .venv
source .venv/bin/activate
pip install .
make clean html
```

### 3. Using conda

```shell
conda env create -f env.yml
conda activate sphinx_doc_env
make clean html
firefox build/html/index.html
```

## Contributing

The documentation is written in sphinx markup. To develop changes to this
documentation first create an issue detailing the changes that are required.
Then create a branch in a clone of this repository, linking it to your issue and
regularly building your changes as described above.

Once happy with your development create a pull request and request a review from
[MetOffice/ssdteam](https://github.com/orgs/MetOffice/teams/ssdteam).
