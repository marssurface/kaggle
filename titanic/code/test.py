#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/5 12:32
# @Author  : JiangPeng
# @File    : a.py

import numpy as np
import pandas as pd
import os
import seaborn
import matplotlib.pyplot as plt

path_dir = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(path_dir, '../data/train.csv')

train_data = pd.read_csv(path)

print(train_data.head())
