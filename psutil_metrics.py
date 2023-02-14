import os
import psutil
import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

l = pd.DataFrame()
while True:
    l = pd.concat([l, pd.DataFrame([[datetime.datetime.now(), psutil.cpu_percent(percpu=True)]], columns=['Date','CPU'])])
    l.to_csv('output.csv')
    time.sleep(0.5)
