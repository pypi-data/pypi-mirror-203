
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="widget-picture-generator",
    version="0.0.1",
    author="Massimo Moffa",
    author_email="massimo.moffa@sensesquare.eu",
    description="This library can be used to generate high-quality images of any type of widget, such as charts, maps, and leaderboards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sense-Square/widget-picture-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)