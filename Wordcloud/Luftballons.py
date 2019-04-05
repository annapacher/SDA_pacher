#!/usr/bin/env python3
# -*- coding: latin1*-
"""
Created on Wed Apr  3 21:08:57 2019

@author: Patrick Plum
"""

"""
A magical depiction of the lyrics of the german pop song '99 Luftballons'
"""

# importing the necessery modules 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import csv 
import numpy as np
from PIL import Image



import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
stopwords = stopwords.words('german')
# file object is created 

file_ob = open('99Luftbalons.txt',encoding="latin1") 
  
# reader object is created 
reader_ob = csv.reader(file_ob) 
  
# contents of reader object is stored . 
# data is stored in list of list format. 
reader_contents = list(reader_ob) 
  
# empty string is declare 
text = "" 
  
# iterating through list of rows 
for row in reader_contents : 
      
    # iterating through words in the row 
    for word in row : 
  
        # concatenate the words 
        text = text + " " + word
        
#lowercase all words to exclude redundancies
text = text.lower()



############################################
#Image as mask for the wordcloud
wave_mask = np.array(Image.open('Ballon.png'))
#generating the wordcloud
wordcloud = WordCloud(width=800, height=800, background_color="white",colormap="Reds_r",stopwords=stopwords,mask=wave_mask).generate(text) 
  
# plot the WordCloud image  
plt.figure(figsize=(12,10),facecolor = 'white', edgecolor='blue')
plt.imshow(wordcloud,interpolation="bilinear")  
plt.axis("off") 
plt.margins(x=0, y=0)
plt.show() 
#########################################

wordcloud.to_file("99luftballons.png")

