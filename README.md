# mlfun
Machine learning practice

## Setup instructions for Cloud 9, including virtualenv 
Thanks to Amy Bearman (@abearman) for guidance

**Note: Choose a *blank* C9 instance. Do not use a Python instance.**

### Prerequisites
1. `cd ~`
2. `sudo pip install virtualenv`

### Python 2 stuff:
1. `virtualenv .p2`
2. `source .p2/bin/activate`
3. `sudo pip install numpy`
4. `sudo pip install scipy` 
5. `sudo pip install pandas`
6. `sudo pip install scikit-learn`

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

### TensorFlow (deactivate first, if necessary)
1. Follow TensorFlow installation instructions for Ubuntu: https://www.tensorflow.org/install/install_linux#InstallingVirtualenv
2. source tensorflow/bin/activate

#### TensorBoard
```
tensorboard --logdir=output --host $IP --port $PORT
```
Then view through the Apache root URL