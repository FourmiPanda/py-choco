import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="py-choco",
    version="1.0.0",
    description="A python adapter for choco-solver",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/FourmiPanda/py-choco",
    author="FourmiPanda;PauluxDelux;tigerIonic",
    author_email="example@email.example",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    #   packages=["reader"],
    packages=find_packages(exclude=("tests",)),
    #   include_package_data=True,
    #   install_requires=["feedparser", "html2text"],
    entry_points={
        "console_scripts": [
            "pychoco=choco.__main__:main",
        ]
    },
)
