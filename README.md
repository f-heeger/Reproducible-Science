Reproducible Science Template
=============================


Kickoff-meeting
---------------

> More than 70% of researchers have tried and failed to reproduce another scientist's experiments, and more than half have failed to reproduce their own experiments. [[1]]

In an attempt to overcome this _reproducibility crisis_ in the field of modeling and simulation, everyone should aim for a fully automated workflow [[2]] from the input scripts to a finished document.
To not only provide _theoretical_ reproducibility, but a _practical_ one, everyone -- given the required computational power -- should be able to easily recreate those documents.

We would like to establish a working group within BAM that develops a wiki/handbook of possible approaches to tackle these challenges. 
Everyone should be able to access these documents and will be able to use these as a basis for future projects.
The competence center modeling and simulation will coordinate the efforts towards 
this goal, provide guidance and the infrastructure (e.g. a wiki, repositories). 
For completing the tasks itself, however, we mainly rely on the work of the interested participants.

Depending on the scientific field, the challenges everyone faces may differ, but we also expect many common proedures and methods to solve these issues. 
In a first kickoff meeting, we therefore want to collect requirements and existing solutions within BAM.
If you are interested in participating in the kickoff, please register by sending an email to simulation@bam.de.

[1]: https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970
[2]: https://www.practicereproducibleresearch.org/core-chapters/2-assessment.html


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




