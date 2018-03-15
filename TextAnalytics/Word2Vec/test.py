# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 17:20:03 2018

@author: Ben Brock
"""

'''
Part 1: Computing the Word Mover's Distance
'''


from time import time
start_nb = time()

# Initialize logging.
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')

sentence_obama = 'Obama speaks to the media in Illinois'
sentence_president = 'The president greets the press in Chicago'
sentence_obama = sentence_obama.lower().split()
sentence_president = sentence_president.lower().split()

# Import and download stopwords from NLTK.
from nltk.corpus import stopwords
from nltk import download
download('stopwords')  # Download stopwords list.

# Remove stopwords.
stop_words = stopwords.words('english')
sentence_obama = [w for w in sentence_obama if w not in stop_words]
sentence_president = [w for w in sentence_president if w not in stop_words]


print '\nSENTENCE_OBAMA\n'
print sentence_obama 

print '\nSENTENCE_PRESIDENT\n'
print sentence_president



start = time()
import os

# Print current working directory
print "\nCurrent working dir : %s" % os.getcwd()

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora, models, similarities

from gensim.models import KeyedVectors
if not os.path.exists('GoogleNews-vectors-negative300.bin.gz'):
    raise ValueError("SKIP: You need to download the google news model")
    
model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

print('Cell took %.2f seconds to run.' % (time() - start))

