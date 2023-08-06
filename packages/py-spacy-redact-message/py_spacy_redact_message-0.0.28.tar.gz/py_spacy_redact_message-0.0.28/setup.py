from setuptools import setup, find_packages

VERSION = '0.0.28'
DESCRIPTION = """Redact a PHI (personal health
information) data from a CSV file."""
LONG_DESCRIPTION = """## Installation\n\n
```pip install ym_csv_pii_sanitizer```\n\n
```python -m spacy download en_core_web_sm```\n\n
## Usage\n\n```ym_csv_pii_sanitizer PATH_TO_CSV_FILE```"""
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
        "console_scripts": 
        ["py_spacy_redact_message = py_spacy_redact_message.main:run"],
    },
)
