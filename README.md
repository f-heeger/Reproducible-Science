 https://travis-ci.org/nutofem/Reproducible-Science-Template.svg?branch=master 

Reproducible Science Template
=============================

> More than 70% of researchers have tried and failed to reproduce another scientist's experiments, and more than half have failed to reproduce their own experiments. [[1]]

In an attempt to overcome this _reproducibility crisis_ in the field of modeling and simulation, everyone should aim for a fully automated workflow [[2]] from the input scripts to a finished document.
To not only provide _theoretical_ reproducibility, but a _practical_ one, everyone -- given the required computational power -- should be able to easily recreate those documents.

We would like to establish a working group within BAM that develops a wiki/handbook of possible approaches to tackle these challenges. 
Everyone should be able to access these documents and will be able to use these as a basis for future projects.
The competence center modeling and simulation will coordinate the efforts towards 
this goal, provide guidance and the infrastructure (e.g. a wiki, repositories). 
For completing the tasks itself, however, we mainly rely on the work of the interested participants.

[1]: https://www.nature.com/news/1-500-scientists-lift-the-lid-on-reproducibility-1.19970
[2]: https://www.practicereproducibleresearch.org/core-chapters/2-assessment.html


# Website with further information

Run `make html` to build the sphinx-based website with further content.

# Run the example

To run the example, you can first start our docker container

~~~sh
<host> cd <root of this git repository>
<host> sudo docker run -ti -v $(pwd):/repro christophpohl/reproducible
~~~

in an interactive terminal (`-ti`) and with the current directory (`$(pwd)` - use `${PWD}` (curly brackets!) on windows powershell) available at `/repro` within the container. You are now in the `christophpohl/reprodicble` docker container. To start the pydoit script, run

~~~sh
<docker> cd repro/example
<docker> doit
~~~

---

Alternatively, you can combine all the steps above into one command
~~~sh
<host> sudo docker run -v "$(pwd)":/repro christophpohl/reproducible /bin/bash -c "cd repro/example && doit"
~~~

