import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
import pkg_resources
import keras
from git.repo.base import Repo
import os
import joblib
import shutil

class DeviationPredictor:
  '''
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

  more details: https://github.com/nirmalparmarphd/PyCpep
  '''

  def __init__(self):
    # defining variables
    print("Imported DeviationPredictor sucessfully.")
    self.amount_info_msg ="""
    ERROR! --> Entered value of of the reference or/and the standard amount is NOT appropriate.

      # NOTE: enter the sample and reference material amount as mentioned below
      
        ## Full cell:               1.0     [0.80 to 1.00 ml]
        ## Two Third full cell:     0.66    [0.40 to 0.80 ml]
        ## One half full cell:      0.5     [0.26 to 0.40 ml]
        ## One third full cell:     0.33    [0.10 to 0.26 ml] 
        
      For more information please check https://github.com/nirmalparmarphd/PyCpep.
    """
    self.information ='''
      * This is a Deep learning (DL) ANN model to predict a deviation due to an inappropriate amount combination of the sample and a reference material in a batch cell of Tian-Calvet micro-DSC.

      * This ANN model predicts the possible deviation that may arise in the heat capacity measurement experiment due to in appropriate combination of the sample and the reference material amount!

      --> ANN Model accuracy on the test data is 99.83 [%] <--
      
      * more details: https://github.com/nirmalparmarphd/PyCpep
      
      '''
  ## ANN model loading method
  def load_locally(self):
    """
    ## DeviationPredictor.load_locally()
    load_locally method downloads a minimum working example(.py) for a quick start.

    ### useage:\n
    from pycpep import DeviationPredictor\n
    deviation = DeviationPredictor()\n
    deviation.load_locally() 
    """
    
    url_mwe = 'https://github.com/nirmalparmarphd/PyCpep/'
    cwd = os.getcwd()
    directory = 'pkg_pycpep'
    path = os.path.join(cwd, directory)
    self.path = path
    isExist = os.path.exists(path)
    if not isExist:    
      os.mkdir(path)
      print("Directory '% s' created" % directory)
      Repo.clone_from(url_mwe, directory)
      print(f'Downloaded the latest trained nureal network model from the PyCpep package source sucessfully at: {path}')
    else:
      print("Directory '% s' already exist!" % directory)
    # cleaning garbage 
    os.remove(os.path.join(path,"setup.py"))
    os.remove(os.path.join(path,"PyCpep/__init__.py"))
    os.remove(os.path.join(path,"PyCpep/pycpep.py"))
    os.remove(os.path.join(path,"PyCpep/setup.cfg"))
    shutil.rmtree(os.path.join(path,"PyCpep/__pycache__"),ignore_errors=True)

  ## deviation prediction method
  def deviation_prediction(self, Ref:float, Sam:float, scaler_pkl="scaler.pkl", mdl_h5="model.h5"):
    """
    ## DeviationPredictor.deviation_prediction()
    deviation_prediction method predicts a possible deviation in the heat capacity measurement as a function of the sample and the reference material amount.

    ### useage:\n
    from pycpep import DeviationPredictor\n
    deviation = DeviationPredictor()\n
    deviation.deviation_prediction() 
    """
    self.scaler_pkl = scaler_pkl
    self.mdl_h5 = mdl_h5
    self.Ref = Ref
    self.Sam = Sam
    assert 0 < Ref <= 1 and 0 < Sam <= 1, f"[Ref:{self.Ref}, Sam:{self.Sam}]: Please enter the correct amount of the sample and the reference material.\n {self.amount_info_msg}"
    
    if 0 < Ref <= 1 and 0 < Sam <= 1:
      # loading scaler
      scaler = joblib.load(f"{self.path}/PyCpep/mdl/{self.scaler_pkl}")
      # loading ann model
      model = tf.keras.models.load_model(f"{self.path}/PyCpep/mdl/{self.mdl_h5}")
      # calculating vol-rel
      vol_rel = (Ref*Ref)/Sam
      data = [Ref, Sam, vol_rel]
      data = pd.DataFrame([data])
      # scaling data
      data_ = scaler.transform(data)
      # prediction from ann model
      pred = model.predict(data_)
      pred_ = np.round(((pred*100)-100).astype(np.float64),2)
      print('-'*50)      
      print('Reference amount : ', Ref)
      print('Sample amount : ', Sam)
      
      if abs(pred_) <= 1.5:
        print(f'Heat capacity measurement deviation prediction {pred_} (%)')
        print('''COMMENT(s):
              You are Awesome!! The predicted deviation is below 1%!
              The combination of the sample and the reference amount is appropriate.
              ''')
        print('-'*50)
      else:
        print(f'Heat capacity measurement deviation prediction {pred_} (%)')
        print('''COMMENT(s): 
              The combination of the sample and the reference amount is NOT appropriate.
              ''')
        # NOTE:Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
      print('-'*50)
    else:
      print(f'{self.amount_info_msg}')
      print('-'*50)
      return

  def info(self):
      """
      ## DeviationPredictor.info()
      Get a quick info on a module useage.

      ### useage:\n
      from pycpep import DeviationPredictor\n
      deviation = DeviationPredictor()\n
      deviation.info() 
      """
      print(self.information)