# Simulation Systems

This repository contains documentation that is common across the many simulation and modelling codes owned by the Met Office.

To build this documentation from the top level of the project run:
```
conda env create -f env.yml
conda activate sphinx_doc_env
make clean html
firefox build/html/index.html
```

The documentation is written in sphinx markup. To develop changes to this 
documentation first create an issue detailing the changes that are required.
Then create a branch in a clone of this repository, linking it to your issue and
regularly building your changes as described above. 

Once happy with your development create a pull request and request a review
from MetOffice/ssdteam. 