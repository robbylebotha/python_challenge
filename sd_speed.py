#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import glob
import os

sns.set()

#4cb82c20117b.csv
#4cb82c2383ad
#Read in the CSV
#df = pd.read_csv('4cb82c20117b.csv', skiprows=0) #import single specific csv file
df = pd.concat(map(pd.read_csv, glob.glob('*.csv'))) #import all csv files in folder
df.head()
df.info()

#Create Dataframe
df.columns = ['serverTime', 'phoneTime', 'deviceId', 'lat', 'lon', 'acc', 'speed', 'ts']
df = df.drop(df[(df.lat == 0) & (df.lon == 0)].index) #remove entries where lat&lon is 0
df.head()


speed = df['speed']
lat = df['lat']
lon = df['lon']
acc = df['acc']
devID = df['deviceId']

df.serverTime = pd.to_datetime(df.serverTime) #convert servertime object to a date
df.phoneTime = pd.to_datetime(df.phoneTime)
df.ts = pd.to_datetime(df.ts)
df.set_index('serverTime', inplace=True) #set index of dataframe

# numDevices = len(df.index)

#plot graph
plt.figure(figsize=(9,8)) 
sns.distplot(speed)
plt.title('Standard Deviation', fontsize=30)

plt.show()
# %%
