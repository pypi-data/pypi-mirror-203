from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'Flask Extension for creating and managing shortened URLs.'

# Setting up
setup(
    name="flask-url-shortener",
    version=VERSION,
    author="Mohamed El-Hasnaouy",
    author_email="<elhasnaouymed@proton.me>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['flask'],
    keywords=['python', 'flask', 'url', 'shortener', 'url', 'development'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
