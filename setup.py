import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mcl",
    version="0.0.5",
    author="Piotr Szyma",
    author_email="thompson2908@gmail.com",
    description="Python wrapper for mcl library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/piotrszyma/mcl-python",
    packages=["mcl", "mcl.structures"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
