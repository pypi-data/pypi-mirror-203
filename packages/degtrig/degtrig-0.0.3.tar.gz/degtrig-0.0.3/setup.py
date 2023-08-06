import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    # Here is the module name.
    name="degtrig",
 
    # version of the module
    version="0.0.3",
 
    # Name of Author
    author="Abhinav G",
 
    # your Email address
    author_email="agupta.cam7@gmail.com",
 
    # #Small Description about module
    description="Adds all of the trigonometric functions using degrees instead of radians.",
 
    # long_description=long_description,
 
    # Specifying that we are using markdown file for description
    long_description=long_description,
    long_description_content_type="text/markdown",
 
    # Any link to reach this module, ***if*** you have any webpage or github profile
    url="https://github.com/abhinav-gg/StupidPipPackages/DegTrig",
    packages=setuptools.find_packages(),

    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
    keywords = ["trigonometry", "radians", "degrees", "trig", "convert", "radians to degrees", "degrees to radians", "deg", "rad", "hyperbolic", "hyperbolic functions"],
 
 
    install_requires=[],

    license="MIT",
 
    # classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)