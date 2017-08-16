# mlfun
Machine learning practice

## Setup instructions for Cloud 9, including virtualenv 
Thanks to Amy Bearman (@abearman) for guidance

**Note: Choose an HTML5 C9 instance. Do not use a Python instance.**

### Prerequisites
1. cd ~
2. sudo pip install virtualenv

### Python 2 stuff:
2. virtualenv .p2
3. source .p2/bin/activate
4. sudo pip install numpy
5. sudo pip install scipy 
6. sudo pip install pandas
7. sudo pip install scikit-learn

Then you can do:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```

### Python 3 stuff: (deactivate first, if necessary)
1. virtualenv -p /usr/bin/python3 .p3
2. source .p3/bin/activate
3. sudo apt-get install python3-pip
4. sudo pip install numpy
5. sudo pip install scipy
6. sudo pip install pandas
7. sudo pip install scikit-learn

Then you can do:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```