from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

install_requires = ["termcolor == 1.1.0"]

setup(
    name="py_oneliner",
    version="0.0.1",
    author="Fuzail Palnak",
    author_email="fuzailpalnak@gmail.com",
    url="https://github.com/fuzailpalnak/py_oneliner",
    description="Dynamic print statements for Python Projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires="~=3.6",
    install_requires=install_requires,
    keywords=["Python", "Print", "OneLine Print"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)