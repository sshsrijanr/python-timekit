from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='timekit',
    version='0.0.1',
    description='A package to integrate Timekit APIs with your project',
    py_modules=['timekit'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests==2.24.0",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
        ],
    },
)