from setuptools import setup, find_packages

from codecs import open
from os import path

HERE  =  path.abspath(path.dirname(__file__))

with open(path.join(HERE,'README.md'), encoding='UTF-8') as f:
    long_description = f.read()

    setup(
        name="sboxU",
        version="1.1.0",
        description="",
        long_description="",
        long_description_content_type="text/markdown",
        authors="Aurélien Boeuf,Mathias Joly,Léo Perrin",
        license="",
        classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent"
        ],
        packages=["sboxU"],
        include_package_data=False
    )