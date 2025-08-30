# Simulation Systems

This repository contains documentation that is common across the many simulation
and modelling codes owned by the Met Office.

```mermaid
---
config:
  theme: neutral
---
flowchart

subgraph ss["Simulation Systems Repositories<br>--"]
direction TB
  subgraph Other[**Other**]
  direction TB
    moci@{shape: rect, label: MOCI}
    monc@{shape: rect, label: MONC}
  end
  subgraph Common[**Common**]
  direction TB
    jules
    ukca
    casim
    socrates
    shumlib
  end
  subgraph UM[**Unified Model**]
  direction TB
    um@{shape: rect, label: um}
    gcom[gcom]
    aux@{shape: bow-rect , label: um_aux}
    meta@{shape: procs, label: um_meta}
    mule[mule]
    doc@{shape: doc, label: um_doc}
  end
  subgraph Momentum[**Momentum&reg;**]
  direction TB
    apps[lfric_apps]
    core[lfric_core]
    rose_picker
  end
end
%% Style
style ss font-size:1.3em
style Momentum fill: #abfaabff
style Common fill: #aee3f8ff
style UM fill: #facdcdff
style mule fill: #1de01da9
style shumlib fill: #1de01da9
style rose_picker fill: #1de01da9
style apps fill: #1de01da9
style core fill: #1de01da9
style casim fill: #1de01da9
style ukca fill: #1de01da9
style socrates fill: #1de01da9
style moci fill: #1de01da9
style monc fill: #1de01da9
style um fill: #f7351b9f
style gcom fill: #f7351b9f
style aux fill: #f7351b9f
style meta fill: #f7351b9f
style doc fill: #f7351b9f
style jules fill: #cfcf62ff
%% Links
click jules "https://github.com/MetOffice/jules"
click ukca "https://github.com/MetOffice/ukca"
click casim "https://github.com/MetOffice/casim"
click moci "https://github.com/MetOffice/moci"
click monc "https://github.com/MetOffice/monc"
click socrates "https://github.com/MetOffice/socrates"
click shumlib "https://github.com/MetOffice/shumlib"
click um "https://github.com/MetOffice/um"
click gcom "https://github.com/MetOffice/gcom"
click aux "https://github.com/MetOffice/um_aux"
click meta "https://github.com/MetOffice/um_meta"
click doc "https://github.com/MetOffice/um_doc"
click mule "https://github.com/MetOffice/mule"
click apps "https://github.com/MetOffice/lfric_apps"
click core "https://github.com/MetOffice/lfric_core"
click rose_picker "https://github.com/MetOffice/rose_picker"

%% Dependencies
Momentum ==> Common
UM ==> Common
um ==> gcom & aux & meta & mule
apps ==> core ==> rose_picker
```

Expected visibility by late 2025 - early 2026:
$$\textsf{\color{#1de01d}public (Open Source) \space \color{#f7351b}private (Closed Source) \space \color{#cfcf62}public (TBC)}$$

<!-- <code style="background:#1de01da9">public (Open Source)</code> <code style="background:#f7351b9f">private (Closed Source)</code> <code style="background:#cfcf62ff">public (TBC)</code> -->

## Building the documentation

A quick and clean way to get the package dependencies is via
[uv](https://docs.astral.sh/uv/) package manager.

```sh
git clone https://github.com/MetOffice/simulation-systems
cd simulation-systems

# Install dependencies (see pyproject.toml) in project .venv
uv sync
uv run make clean html

# Verify documentation
firefox build/html/index.html
```

Alternatively, if your have Python-3.11 or higher installed (sphinx==8.2.3
requirement), you can install the dependencies in a virtual environment via
`pip`, and build the documentation like:

```sh
cd simulation-systems

</path/to/python3.11+> -m venv .venv
source .venv/bin/activate
pip install .
make clean html
```

## Contributing to the documentation

The documentation is written in sphinx markup. To develop changes to this
documentation first create an issue detailing the changes that are required.
Then create a branch in a clone of this repository, linking it to your issue and
regularly building your changes as described above.

Once happy with your development create a pull request and request a review from
[MetOffice/ssdteam](https://github.com/orgs/MetOffice/teams/ssdteam).
