# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:07:20 2020

@author: sjliu
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import rasterio
from rasterio import plot as rsplt

dfile = r'E:\t20200914_psu_test\AIS_ASCII_by_UTM_Month\2016/AIS_2016_01_Zone18.csv'
df = pd.read_csv(dfile)

#%%
raster = rasterio.open("data/ny3035.tif")

#%% show large area
maxnum = 1000000
fig,ax = plt.subplots(figsize=(8,6),dpi=200)

rsplt.show((raster,[1,2,3]), ax=ax, adjust=None)
plt.scatter(df.loc[0:maxnum]['LON'],df.loc[0:maxnum]['LAT'],marker='*',c='red',s=0.01,alpha=0.5)

plt.xlim(-79,-71)
plt.ylim(30,43)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()

#%% show small area
maxnum = 1000000
fig,ax = plt.subplots(figsize=(8,6),dpi=200)

rsplt.show((raster,[1,2,3]), ax=ax, adjust=None)
plt.scatter(df.loc[0:maxnum]['LON'],df.loc[0:maxnum]['LAT'],marker='*',c='red',s=0.01,alpha=0.5)

plt.xlim(-77,-75)
plt.ylim(36,38)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.tight_layout()
plt.show()