# mlfun
Machine learning practice

## Setup instructions for Cloud 9, including virtualenv 
Thank you to Amy Bearman (@abearman) for these instructions

**Note: Choose an HTML5 C9 instance. Do not use a Python instance.**

### Python 2 stuff:
1. sudo pip install virtualenv
2. virtualenv .p2
3. source .p2/bin/activate
4. pip install numpy
5. pip install scikit-learn
6. pip install scipy 
7. pip install pandas

Then you can do:
```
python
>>> import numpy
>>> import sklearn
>>> import pandas
```

### Python 3 stuff:
1. virtualenv .p3
2. source .p3/bin/activate
3. sudo apt-get install python3-pip
4. sudo pip3 install numpy

Install Linux version of conda for python3:
1. wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
2. bash Miniconda3-latest-Linux-x86_64.sh

Open a new terminal window
1. source .env/bin/activate
2. conda install scipy
3. conda install scikit-learn
4. sudo pip3 install pandas


Then you can do:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```