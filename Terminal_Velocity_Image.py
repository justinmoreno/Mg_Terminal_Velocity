#!/usr/bin/env python

from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3

import matplotlib as mpl
import matplotlib.pyplot as plt

# change the following to %matplotlib notebook for interactive plotting


# Optionally, tweak styles.
mpl.rc('figure',  figsize=(10, 5))
mpl.rc('image', cmap='gray')

import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience

import pims
import trackpy as tp

import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig


shots = [r'E:\Hyfire Data\MPP - Magnesium Plate Perforation (Yunho)\MPP_110221_1\Terminal Velocity']

labels = ['WC_B_90','WB_B_RC_90','WB_B_60','WB_B_RC_60','WB_B_30','WC_B_RC_30']

colors = ['black','grey','darkred','navy','forestgreen','fuchsia']

ylimits = [-.01,.2]
xlimits = [-10,60]

plt.figure(figsize = (10,6),facecolor='white')

for i,shot in enumerate(shots):

    os.chdir(shot)

    txt_files = glob.glob('C*.txt')

    #roi1 = readdatafile(txt_files[0])

    #roi1time = [i-20 for i in roi1['time']]

    #plt.plot(roi1['time'],roi1['voltage'],color = colors[i],label = labels[i],linewidth = 1)

#monitor = readdatafile(txt_files[3])
#monitor_adj = [i*.01 for i in monitor['voltage']]
#plt.plot(monitor['time'],monitor_adj,color = 'grey',label = labels[-1])

@pims.pipeline
def gray(image):
    return image[:, :, 1]  # Take just the green channel

frames = gray(pims.open('../sample_data/bulk_water/*.png'))







