import setuptools
from setuptools import setup

setup(
    name="docbuild",
    version="0.1.0",
    description="A package for building a document from a textract response, for more information see the docstruct package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Moran Nechushtan, Serah Tapia, Shlomo Agishtein",
    author_email="moran.n@trullion.com, serah@trullion.com, shlomo@trullion.com",
    url="https://github.com/smrt-co/docbuild",
    packages=setuptools.find_packages(),
    install_requires=[
        "attrs>=22.0.0",
        "numpy==1.23.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
