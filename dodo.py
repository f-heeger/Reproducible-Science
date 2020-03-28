def task_simulation():
    """
    Runs the parametrized fenics 'poission' example for a convergence plot
    and a field plot
    """
    return {
        "file_dep": ["computation/poisson.py"],
        "targets": [
            "computation/poisson_convergence_Ns.npy",
            "computation/poisson_convergence_errors.npy",
            "computation/poisson.pvd",
            "computation/poisson000000.vtu",
        ],
        "actions": ["python3 computation/poisson.py"],
        "clean": True,
    }


def task_poisson_field_plot():
    """
    Use paraview (via python2 script) to convert the fenics output to a picture 
    """
    return {
        "file_dep": [
            "plots/poisson_paraview_plot.py",
            "computation/poisson.pvd",
            "computation/poisson000000.vtu",
        ],
        "targets": ["plots/poisson_field.png"],
        "actions": ["pvbatch --force-offscreen-rendering plots/poisson_paraview_plot.py"],
        "clean": True,
    }


def task_poisson_convergence_plot():
    """
    Use python3 matplotlib to convert the poisson data to a line plot
    """
    return {
        "file_dep": [
            "plots/poisson_convergence.py",
            "computation/poisson_convergence_Ns.npy",
            "computation/poisson_convergence_errors.npy",
        ],
        "targets": ["plots/poisson_convergence.pdf"],
        "actions": ["python3 plots/poisson_convergence.py"],
        "clean": True,
    }


def task_paper():
    return {
        "file_dep": [
            "tex/paper.tex",
            "plots/poisson_convergence.pdf",
            "plots/poisson_field.png",
        ],
        "targets": ["tex/paper.pdf"],
        "actions": ["latexmk -pdf -cd tex/paper.tex"],
    }


#def task_show():
#    return {"file_dep": ["tex/paper.pdf"], "actions": ["xdg-open tex/paper.pdf"]}
