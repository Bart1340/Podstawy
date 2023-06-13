#!/usr/bin/env python
# coding: utf-8

# # Bag of Words

# In[1]:


from sklearn.feature_extraction.text import CountVectorizer


# Sklearn Bag of Words
# https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

# In[2]:


class Category:
    BOOKS = 'BOOKS'
    CLOTHING = 'CLOTHING'

train_x = ["i love the book", 'this is a great book', 'the fit is great', 'i love the shoes']
train_y = [Category.BOOKS, Category.BOOKS, Category.CLOTHING, Category.CLOTHING]


# ### Unigram (binary)

# In[3]:


vectorizer = CountVectorizer(binary=True)
train_x_vectors = vectorizer.fit_transform(train_x)
#print(vectorizer.get_feature_names())
#print(train_x_vectors.toarray())


# In[4]:


from sklearn import svm
clf_svm = svm.SVC(kernel='linear')
clf_svm.fit(train_x_vectors, train_y)


# In[5]:


test_x = vectorizer.transform(['shoes are all right'])
clf_svm.predict(test_x)


# ### Bigram (binary)

# In[6]:


vectorizer = CountVectorizer(binary=True, ngram_range=(1,2))
train_x_vectors = vectorizer.fit_transform(train_x)
#print(vectorizer.get_feature_names())
#print(train_x_vectors.toarray())

from sklearn import svm
clf_svm = svm.SVC(kernel='linear')
clf_svm.fit(train_x_vectors, train_y)

test_x = vectorizer.transform(['shoes are all right'])
clf_svm.predict(test_x)


# # Word Vectors (word embeddings)

# Spacy https://spacy.io/usage/embeddings-transformers

# In[7]:


get_ipython().system('pip install spacy')
get_ipython().system('python -m spacy download en_core_web_md')


# In[8]:


import spacy

nlp = spacy.load('en_core_web_md')


# In[9]:


#print(train_x)


# In[10]:


docs = [nlp(text) for text in train_x]
#print(docs[0].vector)

train_x_word_vectors = [x.vector for x in docs]


# In[11]:


from sklearn import svm
clf_svm_wv = svm.SVC(kernel='linear')
clf_svm_wv.fit(train_x_word_vectors, train_y)


# In[12]:


test_x = ['these earings hurt ']
test_docs = [nlp(text) for text in test_x]
test_x_word_vectors = [x.vector for x in test_docs]

clf_svm_wv.predict(test_x_word_vectors)


# # Regexes

# pattern matching of strings in Python

# https://cheatography.com/davechild/cheat-sheets/regular-expressions/
# 

# https://regex101.com/

# ### Checking if the phrase matches exactly

# In[13]:


import re 

regexp = re.compile(r'^ab[^\s]*cd$')

phrases = ['abcd','xxx','aaa abxxxcd ccc','ab cd']

matches = []
for phrase in phrases:
    if re.match(regexp, phrase):
        matches.append(phrase)

print(matches)


# ### Checking if the phrase exists in the string at all

# In[14]:



phrases = ['abcd','xxx','abxxxcd','ab cd']

matches = []
for phrase in phrases:
    if re.search(regexp, phrase):
        matches.append(phrase)

print(matches)


# ### Example

# In[15]:


regexp = re.compile(r'\bbread\b|\bstory\b|\bbook\b')

#\b - within word boundaries

phrases = ['i liked that story', 'the car treaded up the hill', 'this hat is nice']

matches = []
for phrase in phrases:
    if re.search(regexp, phrase):
        matches.append(phrase)

print(matches)


# # Stemming/Lemmatization

# ### Stemming 

# In[16]:


import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')


# In[17]:


from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

phrase = "reading the books"
words = word_tokenize(phrase)

stemmed_words = []
for word in words:
    stemmed_words.append(stemmer.stem(word))

" ".join(stemmed_words)


# ## Lemmatization

# In[18]:


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download('omw-1.4')

phrase = "reading the books"
words = word_tokenize(phrase)

lemmatized_words = []
for word in words:
    lemmatized_words.append(lemmatizer.lemmatize(word, pos='v'))
    
" ".join(lemmatized_words)


# # Stopwords Removal

# In[19]:


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = stopwords.words('english')
#print(stop_words)
#print(len(stop_words))

phrase  = "Here is an example sentence demonstrating the removal of stopwords"

words = word_tokenize(phrase)

stripped_phrase = []
for word in words:
    if word not in stop_words:
        stripped_phrase.append(word)

" ".join(stripped_phrase)


# # Spell correction, sentiment, pos tagging

# https://textblob.readthedocs.io/en/dev/api_reference.html
# 
# https://www.learntek.org/blog/categorizing-pos-tagging-nltk-python/

# In[20]:


get_ipython().system('pip install textblob')
from textblob import TextBlob
get_ipython().system('python -m textblob.download_corpora')


# In[22]:


phrase = "the book was horrible"

tb_phrase = TextBlob(phrase)

tb_phrase.correct() #spell correction

tb_phrase.tags #speech taging

tb_phrase.sentiment


# # Transformer architectures (neural networks)
# https://explosion.ai/blog/spacy-transformers

# In[33]:


get_ipython().system('pip install spacy-transformers')
get_ipython().system('python -m spacy download en_core_web_sm')


# In[34]:


import spacy
import torch

nlp = spacy.load('en_core_web_sm')
doc = nlp('Here is some text to encode')


# In[36]:


class Category:
    BOOKS = 'BOOKS'
    BANK = 'BANK'

train_x = ['good character and plot progression', 'check out the book', 'good story. would recomend', 'novel recommendation', 'need to make a deposit to the bank', 'balance inquiry savings', 'save money']
train_y = [Category.BOOKS, Category.BOOKS, Category.BOOKS, Category.BOOKS, Category.BANK, Category.BANK, Category.BANK]


# In[38]:


from sklearn import svm

docs = [nlp(text) for text in train_x]
train_x_vectors = [doc.vector for doc in docs]
clf_svm = svm.SVC(kernel='linear')

clf_svm.fit(train_x_vectors, train_y)

test_x = ['i need to write a check']
docs = [nlp(text) for text in test_x]
test_x_vectors = [doc.vector for doc in docs]

clf_svm.predict(test_x_vectors)


# https://github.com/KeithGalli/pycon2020

# In[ ]:




