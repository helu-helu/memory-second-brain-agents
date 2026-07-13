from setuptools import setup, find_packages

setup(
    name="specify-cli",
    version="0.1.0",
    description="Specify CLI for Spec Kit",
    packages=find_packages(where="src") if False else find_packages(),
    include_package_data=True,
)