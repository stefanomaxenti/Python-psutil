import psutil
import time
import datetime
import pandas as pd

l = pd.DataFrame()
while True:
    l = pd.concat([l, pd.DataFrame([[datetime.datetime.now(), psutil.cpu_percent(percpu=True), psutil.virtual_memory()]], columns=['Date','CPU', 'RAM'])])
    l.to_csv('output.csv')
    time.sleep(0.5)
