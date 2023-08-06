from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.3'
DESCRIPTION = 'Fitting and Plotting made simpler'

# Setting up
setup(
    name="FPfits",
    version=VERSION,
    author="FelixDedekind",
    author_email="png.spammail@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['matplotlib','numpy'],
    keywords=['python'],
    classifiers=[]
)
