from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="db_simple",
    version="0.1",
    author="Danyamutit23",
    author_email="duaneskalanak@gmail.com",
    description="Данный модуль , заменяет другие database если вам не удобно их использовать!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "db_simple=db_simple:main"
        ]
    }
)

