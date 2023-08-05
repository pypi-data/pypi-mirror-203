from setuptools import setup, find_packages
from os import path

# read the contents of the README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pyquotegen",
    version="0.0.4",
    author="Arman Idrisi",
    author_email="idrisiarman19@gmail.com",
    description="A Random Quote Generator Python Package",
    long_description=long_description,
long_description_content_type='text/markdown',
  

    url="https://github.com/Armanidrisi/pyquotegen",
    project_urls={
        "Bug Tracker": "https://github.com/Armanidrisi/pyquotegen/issues",
        "Documentation": "https://github.com/Armanidrisi/pyquotegen/blob/main/README.md",
        "Source Code": "https://github.com/Armanidrisi/pyquotegen",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.0",
)
