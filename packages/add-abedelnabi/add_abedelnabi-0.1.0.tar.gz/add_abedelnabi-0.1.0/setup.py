# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="Mohammad Usama",
    description="A package for adding two numbers together",
    name="add_abedelnabi",
    packages= find_packages(include=['add_abedelnabi', 'add_abedelnabi.*']),
    version="0.1.0",
)