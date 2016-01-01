import os

from setuptools import find_packages, setup


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: Implementation :: PyPy",
]

setup(
    name="inevitable",
    packages=find_packages(),
    install_requires=["characteristic"],
    setup_requires=["vcversioner"],
    vcversioner={"version_module_paths": ["inevitable/_version.py"]},
    author="Jullian Berman",
    author_email="Julian+Inevitable@GrayVines.com",
    classifiers=classifiers,
    description="A reactor for STM",
    license="MIT",
    long_description=long_description,
    url="https://github.com/Julian/Inevitable",
)
