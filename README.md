Reproducible Science Template
=============================

Workshop
--------

> More than 70% of researchers have tried and failed to reproduce another scientist's experiments, and more than half have failed to reproduce their own experiments. [[1]]

In an attempt to overcome this _reproducibility crisis_ in the field of modelling and simulation, we aim to introduce a fully automated workflow [[2]] from the input scripts to a publication-ready document.

To not only provide _theoretical_ reproduciblity, but a _practial_ one, everyone -- given the required computational power -- should be able to run the tools e.g. using `docker`. 
We therefore want to collect requirements and existing solutions from scientists at BAM in an upcoming workshop. Depending on the specific input of the participants, this may include:

- automation crash course (`doit`[[3]])
- using compute clusters
- using non-free software?
- simulation data management


[1]: https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970
[2]: https://www.practicereproducibleresearch.org/core-chapters/2-assessment.html
[3]: https://pydoit.org/


Structure of the repository
---------------------------

(currently, do be discussed)

`computation/`

- scripts needed to run the simulations, e.g. via [`docker`](docker.md)
- raw result files

`plots/`

- scripts needed for postprocessing that usually take data from `computation/` 
- publication-ready images (pdfs/pngs/...)

`tex/`

- tex code that usually takes the images from `plots/`

`/`

- the main `dodo.py` file that wires/automates all actions required to display 
  the publication-ready document




