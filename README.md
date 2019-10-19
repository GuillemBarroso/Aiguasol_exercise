# Aiguasol_exercise

# Python version
Python 3.7.4

# Recommended use of the code
I have used a virtual environment with pipenv in order to run the code. It should also work with pip.

# Download pipenv

# install required libraries
pipenv install -r requirements.txt

# help command for arguments of main.py
```pipenv run python main.py -h```
```
usage: main.py [-h] [--apiToken APITOKEN] [--force]

Read data from ree API and compute FFT

optional arguments:
  -h, --help           show this help message and exit
  --apiToken APITOKEN  API personal_token
  --force              Force download
```
# how to run
pipenv run python main.py --apiToken personal_token

# example
pipenv run python main.py --apiToken 652647858608a4559e7016t3168644efb1b70880313257d4a3ac6cd93e2ad611
pipenv run python main.py --apiToken 652647858608a4559e7016t3168644efb1b70880313257d4a3ac6cd93e2ad611 -f # force
