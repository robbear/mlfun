# mlfun
Machine learning practice

## Setup instructions for Cloud 9, including virtualenv 
Thanks to Amy Bearman (@abearman) for guidance

**Note: Choose a *blank* C9 instance. Do not use a Python instance.**

### Prerequisites
1. `cd ~`
2. `sudo pip install virtualenv`

### Python 2 stuff:
2. `virtualenv .p2`
3. `source .p2/bin/activate`
4. `sudo pip install numpy`
5. `sudo pip install scipy` 
6. `sudo pip install pandas`
7. `sudo pip install scikit-learn`

Then you can do:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```

### Python 3 stuff: (deactivate first, if necessary)
1. `virtualenv -p /usr/bin/python3 .p3`
2. `source .p3/bin/activate`
3. `sudo apt-get install python3-pip`
4. `sudo pip install numpy`
5. `sudo pip install scipy`
6. `sudo pip install pandas`
7. `sudo pip install scikit-learn`

Then you can do:
```
python
>>> import numpy
>>> import scipy
>>> import sklearn
>>> import pandas
```

### Install GDAL globally
See https://gist.github.com/cspanring/5680334 for guidance
1. `sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable`
2. `sudo apt-get update`
3. `sudo apt-get install libgdal-dev`
4. `sudo pip install gdal --global-option=build_ext --global-option="-I/usr/include/gdal/"`
5. `sudo apt-get install gdal-bin`
6. `sudo apt-get install python-gdal`

Test by running `gdalinfo --version`

### TensorFlow (deactivate first, if necessary)
1. Follow TensorFlow installation instructions for Ubuntu
2. source tensorflow/bin/activate

#### TensorBoard
```
tensorboard --logdir=output --host $IP --port $PORT
```
Then view through the Apache root URL