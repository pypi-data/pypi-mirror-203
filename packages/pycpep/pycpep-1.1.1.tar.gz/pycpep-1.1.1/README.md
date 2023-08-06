# [PyCpep](https://pypi.org/project/pycpep/)
[PyCpep](https://pypi.org/project/pycpep/) package predicts the deviation in the isobaric heat capacity measurement (at 298~K) due to the improper amount of the sample or/and calibration standard in Tian-Calvet microDSC. PyCpep package works on the well-trained artificial neural network (ANN) model.

> Estimated PyCpep prediction accuracy over the test data is 99.83[%] and R2-score 99.4

# Direction
1. Open terminal and install the [PyCpep](https://pypi.org/project/pycpep/) package by the following pip command.
```
pip install pycpep
```
2. To check the pkg download and importing the pkg in python. Python 3.8 or higher version is required.
```
$ python

## DeviationPredictor
DeviationPredictor is a class from PyCpep package to predict a deviation in the heat capacity measurement (at 298~K) due to the improper amount of the sample or/and calibration standard in Tian-Calvet microDSC. PyCpep package works on the well-trained artificial neural network (ANN) model.

## useage:
## importing module
from pycpep import DeviationPredictor
deviation = DeviationPredictor(Ref, Sam)
## calling help
help(deviation)
## quick info
deviation.info()
## downloading trained model locally
deviation.load_locally()
## deviation prediction
deviation.deviation_prediction()


```
## Minimum Working Example
```
# to load pkg
from PyCpep import DeviationPredictor
deviation = DeviationPredictor()

# help
help(deviation)

# info
deviation.info()

# Minimum working example download for a quick start
deviation.laod_locally()

# deviation prediction
R = 1 # Reference amount
S = 1 # Sample amount
deviation.deviation_prediction(R,S)

# NOTE: enter the sample and reference material amount as mentioned below
    ## Full cell:               1.0     [0.80 to 1.00 ml]
    ## Two Third full cell:     0.66    [0.40 to 0.80 ml]
    ## One half full cell:      0.5     [0.26 to 0.40 ml]
    ## One third full cell:     0.33    [0.10 to 0.26 ml]
# prediction of the deviation in heat capacity measurement
```