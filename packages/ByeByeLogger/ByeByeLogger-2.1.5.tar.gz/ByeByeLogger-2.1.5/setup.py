from setuptools import find_packages, setup
with open("src/README.md", "r") as f:
    long_description = f.read()

setup(
    name="ByeByeLogger",
    version = "2.1.5",
    description="A simple, yet powerful Python logging library that makes you say goodbye to your standard logger.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Aleksa Lukic",
    classifiers=["License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "Programming Language :: Python :: 3.9",
                 "Programming Language :: Python :: 3.10",
                 "Programming Language :: Python :: 3.11",
                ],
    install_requires=["colorama==0.4.6"],)
