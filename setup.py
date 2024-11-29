# setup.py
from setuptools import setup, find_packages

setup(
    name="global_variables",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["psutil"],  # Make sure psutil is listed as a dependency
    author="ErFosi",
    author_email="alvarodhbo@gmail.com",
    description="A module for managing global system resources and statuses",
    url="https://github.com/erfosi/global_variables",  # Change to your GitLab URL
)