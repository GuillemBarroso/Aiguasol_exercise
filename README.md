# ***Aiguasol_exercise***

# Python version used 3.7.4

# Recommended depency management
I have used a virtual environment with pipenv in order to run the code. To download, see https://medium.com/@mahmudahsan/how-to-use-python-pipenv-in-mac-and-windows-1c6dc87b403e. 

It should also work with pip.

## Install required libraries
Libraries required are stated in requirements.txt. To install use

```pipenv install -r requirements.txt```

# Help command for arguments of main.py
```pipenv run python main.py -h```
```
usage: main.py [-h] [--apiToken APITOKEN] [--force]

Read data from ree API and compute FFT

optional arguments:
  -h, --help           show this help message and exit
  --apiToken APITOKEN  API personal_token
  --force              Force download
```
# Code strucutre

The entrypoint is ```main.py```. To execute in pipenv environment use 

```pipenv run python main.py --apiToken personal_token --force```

The code is sctructured as follows:

## Inputs

* Config inputs
  * ```apiToken```: valid personal token. Send an email to consultasios@ree.es to request one.
  * ```force```: if existing, forces to download data from ree API regardless of file system cache, see cache section in ReeIndicatorAPI.

* Hardcoded inputs
  * indicatorID: indicator ID of interest from ree API
  * start_date: begining of the time series
  * end_date: end of the time series
  
## Input validation
  1. ```start_date```: check correct format ('YYYY-MM-DD')
  2. ```end_date```: check correct format ('YYYY-MM-DD')
  3. ```variableID```: check is integer
  
## Ree API request

  * ```ReeIndicatorAPI```: first checks if there is cached data. If so, loads it. If not calls ree API, downloads and writes file. 
  * ```Cache```: manages the cache calls.
  
## FFT computation
  * ```FFT```: Computes fast fourier transform (FFT) of a certain signal. 
    * ```FFT().compute```: Three inputs are required, ```x``` and ```y``` data plus the total time of the time-series ```totalDays```.
    * ```FFT().plot```: Plots time-domain data (```x```,```y```) and frequency-domain data (```xf```,```yf```).
    
# Testing of FFT computation
A test of the FFT computation is available as




# Example

```pipenv run python main.py --apiToken 652647858608a4559e7016t3168644efb1b70880313257d4a3ac6cd93e2ad611```

```pipenv run python main.py --apiToken 652647858608a4559e7016t3168644efb1b70880313257d4a3ac6cd93e2ad611 --force```
