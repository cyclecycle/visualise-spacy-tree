import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="visualise-spacy-tree",
    version="0.0.3",
    author="Nicholas Morley",
    author_email="nick.morley111@gmail.com",
    description="Create dependency tree plots from SpaCy Doc objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyclecycle/visualise-spacy-tree",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
