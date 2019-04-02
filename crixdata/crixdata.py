# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 18:58:09 2019

@author: Anna Pacher

data taken from http://data.thecrix.de/data/crix.json


"""


       
import json
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# read file
with open('crixdata_020419.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

#create dataframe from json
crixdata = pd.DataFrame(obj)
print (crixdata)

#plot prices against date
crixdata.plot(x='date', y='price')
plt.savefig('pricevsdate.png')

#calculate log returns: they are calculated by taking the ln of the ending value
#divided by the beginning value, i.e. log returen(i) = ln(price(i)/price(i-1))
crixdata['logreturn'] = np.log(crixdata['price']).diff()

#make histogramm of prices and log returns
crixdata.hist()
plt.savefig('hist_price_logreturn.png')


#plot prices against date
crixdata.plot(x='date', y='logreturn')
plt.savefig('logreturnvsdate.png')