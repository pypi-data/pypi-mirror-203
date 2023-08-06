# Sample setup.py for python package to publish to pypi

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blitzactions",
    version="0.0.1",
    author="Rudra",
    author_email="blitz04.dev@gmailc.com",
    description="A package to test openai",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BlitzJB/blitzactions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'openai',
        'python-dotenv',
    ],
)
