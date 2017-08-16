# mlfun
Machine learning practice

## Setup instructions for Cloud 9 (Thank you to Amy Bearman @abearman)

### General
1. export WORKON_HOME=~/Envs
2. source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

### Python 2
1. `mkvirtualenv my_python2_env`
2. `pip install numpy`
3. `pip install scikit-learn`
4. `pip install scipy`
5. `pip install pandas`

Test with:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```

### Python 3
1. `mkvirtualenv -p /usr/bin/python3 my_python3_env`
2. `sudo pip3 install numpy`
3. `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
4. `bash Miniconda3-latest-Linux-x86_64.sh`
5. `conda install scipy`
6. `conda install scikit-learn`
7. pip3 install pandas

Test with:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```
