from setuptools import setup, find_packages

with open("README.md", "r") as fs:
    long_description = fs.read()

setup(
    name="netzeus_core_config",
    version="0.0.3",
    description="NetZeus Core Config module for managing configuration data across all microservices/plugins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Brandon Spendlove",
    author_email="brandon.spendlove@netzeus.io",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "python-dotenv==0.21.0",
        "loguru==0.6.0",
        "pydantic==1.10.2",
    ],
)
