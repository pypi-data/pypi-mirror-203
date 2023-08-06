# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = "Visualization of a Correlation Matrix using 'plotnine'"
LONG_DESCRIPTION = """The 'ggcorrplot' package can be used to visualize easily a
    correlation matrix using 'plotnine'. It provides a function for computing a matrix of
    correlation p-values."""

# Setting up
setup(
        name="ggcorrplot", 
        version=VERSION,
        author="Duvérier DJIFACK ZEBAZE",
        author_email="duverierdjifack@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["numpy>=1.24.2",
                          "pandas>=2.0.0",
                          "plotnine>=0.10.1",
                          "scipy>=1.10.1",
                          "plydata>=0.4.3"],
        python_requires=">=3",
        package_data={"": ["*.txt"]},
        classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    )
)