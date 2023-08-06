from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = """Redact a PHI (personal health
information) data from a CSV file."""
LONG_DESCRIPTION = """## Installation\n\n
```pip install ym_csv_pii_sanitizer```\n\n
```python -m spacy download en_core_web_lg```\n\n
## Usage\n\n```ym_csv_pii_sanitizer PATH_TO_CSV_FILE```"""

setup(
    name="ym_csv_pii_sanitizer",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author="Alex Ilin",
    author_email="alex.ilin@ymeadows.com",
    packages=find_packages(),
    install_requires=[
        'typer',
        'presidio_analyzer',
        'presidio_anonymizer',
        'transformers',
        'torch'
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        "console_scripts":
        ["ym_csv_pii_sanitizer = ym_csv_pii_sanitizer.main:run"],
    },
)
