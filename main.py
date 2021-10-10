"""Script"""

__author__ = 'Viktor Redecker'

import pandas as pd
import sklearn

class Housing:
    def __init__(self):
        self.df_train = pd.read_csv("data/train.csv")
        self.df_test = pd.read_csv("data/test.csv")