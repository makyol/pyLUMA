from setuptools import setup, find_packages

setup(
    name="pyLUMA",
    version="0.0.1",
    author="Mehmet Ali Akyol",
    packages=find_packages(),
    package_data={'pyLUMA': ['examples/*']},
)
