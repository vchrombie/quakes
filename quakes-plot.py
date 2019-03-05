#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  20 10:02:56 2019

@author: vchrombie
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# loading the dataset using pandas
DATA_URL = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv'
df = pd.read_csv(DATA_URL)

# creating the basic plots
fig, ax = plt.subplots()
earth = Basemap(ax=ax)

# creating the earth map
earth.drawcoastlines(color='#556655', linewidth=0.5)
                     
# plotting the data on the map
ax.scatter(df['longitude'], df['latitude'], df['mag'] ** 2, c='red', alpha=0.5, zorder=10)

# saving the plot
ax.set_xlabel("4.5M+ earthquakes monthly plot")
fig.savefig('usgs-4.5m-plain.png', dpi=350)
earth.bluemarble(alpha=0.42)
fig.savefig('usgs-4.5m-earth.png', dpi=350)