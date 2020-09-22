files = ["scripts/modify_files", "scripts/excel", "scripts/word"]

sources = [f + ".py" for f in files]
targets = [f + ".rst" for f in files]


def task_website():
    return {
        "file_dep": targets + ["conf.py", "index.rst"],
        "actions": ["sphinx-build . .build"],
        "verbosity": 2,
    }


def task_to_rst():
    """
    In an attempt of "literate programming", we directly use a documented,
    runnable(!) python file that we convert to *.rst for the website.
    """
    for source, target in zip(sources, targets):
        yield {
            "basename": "convert via to_rst.py",
            "name": source,
            "targets": [target],
            "file_dep": [source, "scripts/to_rst.py"],
            "actions": [f"python3 scripts/to_rst.py {source} > {target}"],
        }
