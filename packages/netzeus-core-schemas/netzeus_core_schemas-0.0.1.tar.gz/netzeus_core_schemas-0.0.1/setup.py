from setuptools import setup, find_packages

with open("README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="netzeus_core_schemas",
    version="0.0.1",
    description="NetZeus Core Schemas module for managing shared pydantic schemas across all microservices/plugins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brandon Spendlove",
    author_email="brandon.spendlove@netzeus.io",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["pydantic>=1.10.2"],
)
