from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="whappy",
    version="0.2.1",
    author="Harsh Raj",
    author_email="saketharshraj@gmail.com",
    description="A Python wrapper for WhatsApp API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saketharshraj/whappy",
    packages=find_packages(),
    package_dir={"whappy": "whappy"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    python_requires=">=3.6",
)
