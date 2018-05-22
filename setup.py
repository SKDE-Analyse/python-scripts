import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skde",
    version="1.0.1",
    author="Arnfinn Hykkerud Steindal",
    author_email="arnfinn.steindal@gmail.com",
    description="SKDE python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SKDE-Analyse/python-scripts",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: LGPL-3.0 License",
        "Operating System :: OS Independent",
    ),
)
