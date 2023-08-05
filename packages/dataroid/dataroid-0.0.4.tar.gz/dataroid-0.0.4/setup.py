from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = '0.0.4'
DESCRIPTION = 'A Simple Wrapper For Synthetic Data Generation'
LONG_DESCRIPTION = (this_directory / "dataroid/README.md").read_text()


# Setting up
setup(
    name="dataroid",
    version=VERSION,
    author="torchd3v",
    author_email="<burak96egeli@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pandas==1.5.3', 'ctgan==0.7.1'],
    keywords=['python', 'data', 'generate', 'synthetic', 'deep learning', 'model'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)