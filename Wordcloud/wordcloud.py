# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:34:12 2019

@author: Anna
"""

# importing the necessery modules 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import csv
import os
from os import path
from PIL import Image
import numpy as np
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

# Please change the working directory to your path!
root_path = os.getcwd()

#import german stopwords (these are words that will be excluded from the wordcloud,
#for instance articles and prepositions)
stopwords = stopwords.words('german')


# file object is created 
file_ob = open(path.join(root_path, 'musil.txt'), encoding='utf-8') 

# the imported text are the first to chapter of Musil's book "Der Mann ohne Eigenschaften"
# and is taken form http://musilonline.at/musiltext/
  
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
 
    
# Mask
man_pic = np.array(Image.open(path.join(root_path, "manwithhat.jpg")))
    

#########################################
# remove stopwords from WordCloud,  show  150 words in the wordcloud . 
wordcloud = WordCloud(width=480, height=480, max_words=150,
            stopwords=stopwords, mask= man_pic,
            mode='RGBA', background_color=None).generate(text) 
  
# plot the WordCloud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 

# store to file
#plt.savefig('wordcloud.png')
# store to file
wordcloud.to_file("wordcloud.png")


#########################################
wordcloud = WordCloud(width=480, height=480,
                      stopwords=stopwords,
                      mask= man_pic,
                      background_color="black").generate(text) 
  
# plot the WordCloud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 
