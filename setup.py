from setuptools import setup

setup(
    name="sb-journal",
    packages=[
        "sb_journal",
        "sb_journal.db",
        "sb_journal.db.crud",
        "sb_journal.cli",
        "sb_journal.cli.actions"
    ],
    author="Jerrys9",
    description=(
        "This command-line application provides information"
        " about Super Bowl teams and seasons when they played."
    ),
    install_requires=[
        "pymongo",
    ],
)
