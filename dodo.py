def task_simulation():
    """
    Runs the parametrized fenics 'poission' example for a convergence plot
    and a field plot
    """
    return {
        "file_dep": ["poisson.py"],
        "targets": ["poisson_convergence.pdf", "poisson.pvd", "poisson000000.vtu"],
        "actions": ["python3 poisson.py"],
        "clean": True,
    }


def task_poisson_field_plot():
    """
    Use paraview (via python2 script) to convert the fenics output to a picture 
    """
    return {
        "file_dep": ["poisson_paraview_plot.py", "poisson.pvd", "poisson000000.vtu"],
        "targets": ["poisson_field.png"],
        "actions": ["python2 poisson_paraview_plot.py poisson.pvd %(targets)s"],
        "clean": True,
    }


def task_paper():
    return {
        "file_dep": ["paper.tex", "poisson_convergence.pdf", "poisson_field.png"],
        "targets": ["paper.pdf"],
        "actions": ["latexmk -pdf paper"],
    }


def task_show():
    return {"file_dep": ["paper.pdf"], "actions": ["xdg-open paper.pdf"]}
