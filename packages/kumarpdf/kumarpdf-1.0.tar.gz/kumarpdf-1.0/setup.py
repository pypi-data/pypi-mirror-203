import setuptools
from pathlib import Path

setuptools.setup(
    name="kumarpdf",
    version=1.0,
    long_description=Path("README.md").open(encoding="utf-8").read(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
)
