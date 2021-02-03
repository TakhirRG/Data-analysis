#!/usr/bin/env python
# coding: utf-8

# #1. Обучить модель mnist, сделать предсказание для картинки (у себя в ноутбуке). При запуске веб сервера должен выводиться результат предсказания (использовать метод POST)
# 2.	Исправить код и добиться точного распознавания.
# 

# In[1]:


import numpy as np
from flask import Flask
import threading


# In[2]:


app = Flask(__name__)


# In[3]:


type(app)


# In[4]:


@app.route('/')
def hello():
    return 'Why I cant change the output on Hello world!!!'


# In[5]:


hello()


# In[6]:


threading.Thread(target = app.run, kwargs = {'host' : 'localhost', 'port':5000}).start()


# In[7]:


import requests


# In[8]:


r = requests.get('http://localhost:5000')
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
print(r.text)


# In[9]:


pip install keras


# In[10]:


import keras
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam
from keras import backend as K


# In[ ]:


from keras.datasets import mnist


# In[ ]:




