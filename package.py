name = "Sphinx_rez"

version = "1.0.0"


description = \
    """
    bdd ORM
    """

requires = [
    "python-3",
    "PyYAML-5.4.1",
    "Sphinx",
    "sphinx_rtd_theme",
    "sphinx_markdown_builder",
]


tools = [
    "doc_md",
    "doc_html",
]


build_command = False
timestamp = 0


def commands():
    env.PATH.append("{root}/src")
    env.PATH.append("{root}")
    env.PYTHONPATH.append("{root}/src")


vcs = "git"