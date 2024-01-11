import os 
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):    #The function `save_object` saves an object to a file using the pickle library.
        
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)        #dill.dump helps to create the pkl file

    except Exception as e:
        raise CustomException(e,sys)
    
