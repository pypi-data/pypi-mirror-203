import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EMPOL_GUI",
    version="2.2.8",
    author="Aastha Gupta",
    author_email="aastha.gupta1208@gmail.com",
    description="Astronomial Large Data Reduction GUI - EMPOL",
    package_data= {'EMPOL_GUI':['EMPOL_GUI/sources/*.conv','EMPOL_GUI/sources/*.nnw','EMPOL_GUI/sources/*.param','EMPOL_GUI/sources/*.sex','EMPOL_GUI/sources/*.cat','EMPOL_GUI/sources/*.desktop']},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aasthagupta128/EMPOL_GUI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

