# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:34:12 2019

@author: Anna
"""

# importing the necessery modules 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import csv

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
#import german stopwords (these are words that will be excluded from the wordcloud,
#for instance articles and prepositions)
stopwords = stopwords.words('german')


# file object is created 
file_ob = open('musil.txt', encoding='utf-8') 

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
  
# show  50 words in the wordcloud . 
wordcloud = WordCloud(width=480, height=480, max_words=50).generate(text)

# plot the WordCloud image  (here no stopwords are defined) 
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 

#########################################
# remove stopwords from WordCloud . 
wordcloud = WordCloud(width=480, height=480, 
            stopwords=stopwords).generate(text) 
  
# plot the WordCloud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 
#########################################
wordcloud = WordCloud(width=480, height=480,
                      stopwords=stopwords,
                      background_color="pink").generate(text) 
  
# plot the WordCloud image  
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
plt.margins(x=0, y=0) 
plt.show() 
