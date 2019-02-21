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

with open('Pokemon.csv') as f:
    namelist = [row["Name"] for row in DictReader(f)]

with open('Pokemon.csv') as f:
    hplist = [row["HP"] for row in DictReader(f)]

with open('Pokemon.csv') as f:
    attacklist = [row["Attack"] for row in DictReader(f)]

with open('Pokemon.csv') as f:
    type1list = [row["Type 1"] for row in DictReader(f)]

temp = set(type1list)

totaltype = list(temp)

poison = 0
dark = 0
normal =0
fairy = 0
ice = 0
fire = 0
rock = 0
psychic = 0
dragon = 0
ghost = 0
bug = 0
grass = 0
water = 0
flying = 0
ground = 0
electric = 0
fighting = 0
steel = 0

for i in range(len(hplist)):
    if type1list[i] == 'Poison':
        poison +=1
    elif type1list[i] == 'Dark':
        dark +=1
    elif type1list[i] == 'Normal':
        normal +=1
    elif type1list[i] == 'Fairy':
        fairy+=1
    elif type1list[i] == 'Ice':
        ice +=1
    elif type1list[i] == 'Fire':
        fire +=1
    elif type1list[i] == 'Rock':
        rock +=1
    elif type1list[i] == 'Psychic':
        psychic+=1
    elif type1list[i] == 'Dragon':
        dragon+=1
    elif type1list[i] == 'Ghost':
        ghost+=1
    elif type1list[i] == 'Bug':
        bug+=1
    elif type1list[i] == 'Grass':
        grass+=1
    elif type1list[i] == 'Water':
        water+=1
    elif type1list[i] == 'Flying':
        flying+=1
    elif type1list[i] == 'Ground':
        ground+=1
    elif type1list[i] == 'Electric':
        electric+=1
    elif type1list[i] == 'Fighting':
        fighting+=1
    elif type1list[i] == 'Steel':
        steel+=1


import matplotlib.pyplot as plt 
  
# x-coordinates of left sides of bars  
left = [0, 5, 10, 15, 20,25,30,35,40,45,50,55,60,65,70,75,80,85] 


  
# heights of bars 
height = [44, 17, 69, 24, 98,27,28,52,32,27,112,70,44,57,4,32,31,32] 
  
# labels for bars 
tick_label = totaltype

# naming the x-axis 
plt.xlabel('Pokemon Type') 
# naming the y-axis 
plt.ylabel('Number of Pokemon') 
# plot title 
plt.title('Pokemon') 

plt.xticks(rotation=90)

# plotting a bar chart 
plt.bar(left, height, tick_label = tick_label, 
        width = 0.8, color = ['red', 'green']) 

plt.savefig('test2.png', dpi=500,bbox_inches='tight')

  
# function to show the plot 
plt.show() 


    
        
    
