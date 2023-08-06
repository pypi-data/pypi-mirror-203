# csv pii sanitizer

## Installation

### Step 1
If you have git installed, clone this repository. If not then download this folder and unzip it.

### Step 2
Install python 3 if you have not already done so.

### Step 3
Create a Python virtual environment in the directory.
While your terminal is in this directory run:

Linux / macOS / WSL:
```
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (not WSL) run:
```
python -m venv .venv
.venv\Scripts\activate.bat
```

### Step 4

Install the dependencies. Run:
```
pip install -r requirements.txt
```

## Usage

Run:
```
python3 main.py INPUT OUTPUT
```
INPUT - Path to csv file to sanitize.
OUTPUT - Optional output path for result csv file.

## Publishing to pypi

Run to build:
```
pip install build
python -m build
```

Run to publish:

TOKEN should be replaced with pypi.org API TOKEN

```
pip install twine
twine upload dist/* -u __token__ -p TOKEN
```
