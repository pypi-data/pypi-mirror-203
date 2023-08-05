from setuptools import find_packages, setup

VERSION = "0.1.1"
AUTHOR = "Andrew Mueller"
EMAIL = "uhlittlelessdumb@gmail.com"

setup(
    name="UlldConfig",
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    description="ULLD Config Classes",
    long_description_content_type="text/markdown",
    long_description="Config classes and parsing for the Uh Little Less Dumb note taking framework.",
    packages=find_packages(
        # exclude=['mypackage.tests'],  # empty by default
    ),
    keywords=["ULLD", "config", "Uh Little Less Dumb", "markdown", "note"],
    # entry_points={
    #     'console_scripts': [
    #         'cli-name = mypkg.mymodule:some_func',
    #     ]
    # }
)
