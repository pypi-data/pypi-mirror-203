from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="magyar",
    version="2.8.0",
    author="Nagy Béla",
    author_email="nagy.belabudapest@gmail.com",
    description="Hungarian names...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kobanya/nevek",
    py_modules=["magyar"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
