# setup.py

from setuptools import setup, find_packages

# Read the contents of README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ome-schema",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add any package dependencies here
    ],
    author="Jason L Weirather",
    author_email="JasonL_Weirather@dfci.harvard.edu",
    description="A Python package for accessing local OME schema files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jason-weirather/ome-schema",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Creative Commons Attribution 3.0 Unported License (CC BY 3.0)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

)
