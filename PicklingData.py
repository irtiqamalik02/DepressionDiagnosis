#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 21:12:05 2021

@author: irtiqamalik
"""

import pickle
import pandas as pd


data = pd.read_csv("no_depression_data.csv") 

#convert csv files of depressed and non depressed into pickle

with open ("non_depressed.pickle", "wb") as file:
    pickle.dump(data,file)
    