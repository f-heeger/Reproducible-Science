doit
====

[doit on github](https://github.com/pydoit/doit)

~~~sh
pip3 install doit
~~~

What is it?
-----------

`doit` is a python-based workflow tool on file-level that lets you specify *actions* that connect *dependencies* to *target*, e.g. 
~~~py
def task_paper():
    return {"targets" : ["paper.pdf"],
            "file_dep": ["paper.tex", "img.png"],
            "actions" : ["pdflatex paper.tex"]}

def task_plot():
    return {"targets" : ["img.png"],
            "file_dep": ["plot.py", "simulation.py"],
            "actions" : ["python3 simulation.py --output plot_data.vtu",
                         "python3 plot.py --input plot_data.vtu"]}
~~~

You can define your workflows as chains of independent or connected tasks and calling `doit` in the command line will automatically run them in the correct sequence. So a `doit paper` will first run the `task_plot` to create the `img.png` and call `pdflatex` afterwards. Also, It will only rerun *actions*, if their *dependencies* change. That means that running `doit paper` again, will image in no *action*, as everything is up-to-date.
Modifying only `paper.tex`, will cause `doit` to run `pdflatex` again. Modifying `plot.py` requires all tasks to be run again.

Why should I use it?
--------------------

A single `doit` command will trigger the execution of the whole chain of workflows to produce a desired output (like a paper). Benefits:
* It documents all steps from source files to the output in an objective way.
* It allows you to easily reproduce a publication after a long time.
* Changes to input files automatically propagate you changes in the figures/pdf.
* It proofs to you/colleges/reviewers that no manual manipulations occur.



Working with multiple systems
-----------------------------

Complex workflows may require several machines run the actions. Reasons include:
- Several scientists want to work on the same workflow
- Compute tools or postprocessing tools are not available
    - licensing
    - *just reviewing* the text of a document on a laptop
    - HPC machine

`pydoit` builds a database (in the folder of the `doit.py`) that tracks (via hashes of the *dependencies*) which *actions* need to be rerun. That means that each task has to be executed at least once, even if the *targets* already exist or are up-to-date.
Problems arise, if due to some of the reasons above, the current machine is unable to do so. 

One remedy is to _store_ a *target* in our version control system and tell `doit`: 
*Trust me, the target in the version control is up-to-date.*

### Proposed setup:
~~~py
    /data/dodo.py           # generates input data
    /simulations/dodo.py    # turns input data into results
    /images/dodo.py         # turns results into images
    /paper/dodo.py          # turns images into a paper
    /dodo.py       # optionally connect all tasks
~~~

The idea is to decouple the whole workflow into multiple `dodo` files. Someone, who just wants to build the `paper.pdf`, relies on up-to-date files in `/images/` and can simply run `doit` in the `/paper/` directory. 
If one wants to execute the _full_ workflow, calling the root `doit` in `/`, will trigger the complete workflow.

If you work with _absolute_ paths in your `dodo` files, such as ...
~~~py
# /simulation/dodo.py
from pathlib import Path
def task_simulation_1():
    simulation_dir = Path(__file__).absolute().parent
    script = str(simulation_dir / "simulation_1.py")
    input = str(simulation_dir.parent / "data" / "input_1.dat")
    image = str(simulation_dir.parent / "images" / "graph_1.pdf")
    return {
        "file_dep": [script, input],
        "targets": [image],
        "actions": [f"{python3 {script} {input}]
    }
~~~

... and ...
~~~py
# /paper/dodo.py
from pathlib import Path
def task_simulation_1():
    paper_dir = Path(__file__).absolute().parent
    tex = str(paper_dir / "paper.tex")
    pdf = str(paper_dir / "paper.pdf")
    image = str(paper_dir.parent / "images" / "graph_1.pdf")
    return {
        "file_dep": [tex, image],
        "targets": [pdf],
        "actions": [f"{pdflatex {tex}]
    }
~~~
... that makes it easy to connect the `image` target of the simulation task with the same `image` dependency of the paper task by just importing both into the same _root_ file

~~~py
# (root) /dodo.py
from simulation.dodo import *
from paper.dodo import *
~~~


Skipping huge simulations
-------------------------

If you just want to skip tasks (e.g. if they are too time consuming) you can define a flag and skip the task definition, if that flag is set. The simplest way would be to manually set the flag in the `dodo.py` file like

~~~py
import os
def skip():
    return True # set that to false manually

def task_huge_simulation():
    if skip():
        return
    return {...} # file_dep, actions, dependencies
~~~

It is advantageous to be able to change the flag without modifying the file, e.g. via an environment variable. 

~~~py
def skip():
    """
    return False if "DOIT_SKIP" is empty or does not exist.
    """
    try:
        return os.environ["DOIT_SKIP"] != ""
    except:
        return False
~~~

This allows you to have "DOIT_SKIP=True" on your local machine, but run it with "DOIT_SKIP=" from time to time on a server to ensure full reproducibility.
