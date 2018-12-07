import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Daniel Qin",
    author_email="k17dq01@kzoo.edu",
    description="Dragon King Statistical Analysis package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcqin17/dragonking",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
