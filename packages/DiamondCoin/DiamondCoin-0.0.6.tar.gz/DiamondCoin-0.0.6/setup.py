from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["bottle>=0.12"]

setup(
    name="DiamondCoin",
    version="0.0.6",
    author="Jeam Marn",
    author_email="jeammarn@gmail.com",
    description="A package to easy use API Diamond Coin API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/JeamDev/DiamondCoin",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)   