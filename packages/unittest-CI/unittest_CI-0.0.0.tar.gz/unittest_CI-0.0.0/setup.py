# Source: https://github.com/hmeine/qimage2ndarray/blob/master/setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pathlib import Path

install_requires: list[str] = [
    "setuptools",
]
"""All required (i.e., for functionality) dependencies that are installed when running `pip install NeuroRuler`.

Non-functional (e.g., formatting, documentation) dependencies listed in requirements.txt."""



setup(
    name="unittest_CI",
    version="0.0.0",
    description="",
    # Cannot use multiple authors
    # https://stackoverflow.com/questions/9999829/how-to-specify-multiple-authors-emails-in-setup-py
    author="Jesse Wei",
    author_email="jesse@cs.unc.edu",
    url="https://github.com/COMP523TeamD/HeadCircumferenceTool",
    download_url="https://github.com/COMP523TeamD/HeadCircumferenceTool/releases",
    keywords=[
    ],
    install_requires=install_requires,
    # We don't need extras_require
    # See https://stackoverflow.com/questions/41268863/what-is-the-difference-between-extras-require-and-install-requires-in-se
    # extras_require=dict(),
    tests_require="pytest",
    # TODO: Change after refactoring
    packages=["src"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
