from __future__ import print_function, unicode_literals

from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))
with open('README.md', 'r') as fh:
    long_description = fh.read()


def read(file_paths, default=""):
    # intentionally *not* adding an encoding option to open
    try:
        with codecs.open(os.path.join(here, *file_paths), "r") as fh:
            return fh.read()
    except Exception:
        return default


def find_version(file_paths):
    version_file = read(file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='python_timekit',
    version=find_version(["timekit", "__init__.py"]),
    url='https://github.com/Srijan-Ramavat/python-timekit',
    author="Srijan Ramavat",
    author_email="srijan.ramavat@gmail.com",
    description=
    'An un-official package to integrate Timekit APIs with your project',
    packages=['timekit', 'timekit.components'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Internet",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests==2.24.0",
    ],
)