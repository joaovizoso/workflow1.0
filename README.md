# workflow1.0

1. Save TIFF files in `docs/` folder
2. Activate virtual environment and install requiements
3. `$ cd exec/`
2. `$ python workflow.py`

# Pre-requirements

`libtesseract (>=3.04)`
`libleptonica (>=1.71)`

To install them (on debian): `$ apt-get install tesseract-ocr libtesseract-dev libleptonica-dev pkg-config`

# Virtual Environment
- To create an virtual environment: `$ python3 -m venv env`. (Only need to do once)
- To activate it: `$ source env/bin/activate`. (Every new terminal needs to activate)
- To install requirements: `$ pip install -r requirements` (Only need to do once)
- To save requirements: `$ pip freeze -r requirements` (To add new requirements)
