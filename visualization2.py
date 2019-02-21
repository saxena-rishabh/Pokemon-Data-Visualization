# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:02:41 2019

@author: Rishabh
"""

import glob
import os
import shutil
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
import pandas as pd
from csv import DictReader
from urllib import request





  
# x-coordinates of left sides of bars  
left = [0, 5, 10, 15, 20] 

#left = [0,20,30,40,50,60,70,80,90,100,110,130,140,150,160,170]
  
# heights of bars 
height = [55, 84, 48, 49, 52 ] 
pokemon_name = ['Pikachu', 'Charizard', 'Squirtle', 'Bulbasaur', 'Charmander']
# labels for bars 
tick_label = pokemon_name

# naming the x-axis 
plt.xlabel('Name of Pokemon') 
# naming the y-axis 
plt.ylabel("Attack") 
# plot title 
plt.title(" Pokemon's Attack") 

plt.xticks(rotation=90)

# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 1, color = ['yellow', 'orange', 'blue', 'green', 'orange']) 

plt.savefig('test3.png', dpi=500,bbox_inches='tight')

  
# function to show the plot 
plt.show() 
