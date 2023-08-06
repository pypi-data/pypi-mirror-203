from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent

VERSION = '0.0.27'
DESCRIPTION = 'Redact message using spacy NER'
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

setup(
    name="py_spacy_redact_message",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author="Alex Ilin",
    author_email="ilin.alex.mail@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=['typer', 'spacy'],
    classifiers= [
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        "console_scripts": ["py_spacy_redact_message = py_spacy_redact_message.main:run"],
    },
)
