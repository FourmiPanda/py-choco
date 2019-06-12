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
    author_email="paul.bavazzano@imt-atlantique.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    packages=["core"],
    # packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["pyjnius"],
    entry_points={
        "console_scripts": [
            "realpython=choco.__main__:main",
        ]
    },
)
