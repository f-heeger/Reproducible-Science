
targets = ["scripts/excel.rst"]

def task_website():
    return {
            "file_dep": targets + ["conf.py", "index.rst"],
            "actions": ["sphinx-build . .build"],
            "verbosity": 2
            }


def task_to_rst():
    """
    In an attempt of "literate programming", we directly use a documented,
    runnable(!) python file that we convert to *.rst for the website.
    """
    return {
            "file_dep": ["scripts/excel.py", "scripts/to_rst.py"],
            "actions": ["python3 scripts/to_rst.py scripts/excel.py > scripts/excel.rst"],
            "targets": ["scripts/excel.rst"],
            "verbosity": 2
            }
