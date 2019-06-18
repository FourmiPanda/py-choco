import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
# doesn't works with python 2.7 -> inntroduces in py 3.5 -> see : https://github.com/aio-libs/aiohttp/issues/2741
# README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="PyChoco",
    version="1.0.5",
    description="A python adapter for choco-solver",
    long_description="README",
    long_description_content_type="text/markdown",
    url="https://github.com/FourmiPanda/py-choco",
    author="FourmiPanda;PauluxDelux;tigerIonic",
    author_email="paul.bavazzano@imt-atlantique.net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
    packages=["PyChoco/core"],
    # packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["pyjnius", "Cython"],
    entry_points={
        "console_scripts": [
            "realpython=choco.__main__:main",
        ]
    },
)
