from setuptools import setup, find_packages

VERSION = '1.0.3'
DESCRIPTION = "Python package for managing advanced requests"
LONG_DESCRIPTION = "Python package for managing advanced requests"

# Setting up
setup(
    name="advancedrequests",
    version=VERSION,
    author="GigaAlex",
    author_email="nick.faltermeier@gmx.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)