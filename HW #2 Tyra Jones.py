#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.__version__


# In[2]:


df = pd.read_csv("abuse.csv")


# In[3]:


df


# In[15]:


df.columns


# In[17]:


df[['characteristic','race-ethnicity','Male-%']].head()


# In[20]:


import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')


# In[21]:


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
_ = df[['characteristic', 'Male-%']].plot.bar(ax=ax)
_ = ax.set_xticklabels(zip(df['characteristic'], df['race-ethnicity'] ))
labels = [f'{c}\n{re}' for c,re in zip (df[characteristic], df['race-ethnicity'])]
_= ax.set_sticklables(labels, rotation=90)


# In[27]:


fig.ax=plt.subplots()
_=ax.set_title("Alcohol in Blacks")
_=percent['race-ethnicity'].str.match('Black')|plot.bar(ax=ax)
_=ax.set_sticklabels(percent['characteristic'])
_=ax.grid()


# In[28]:


fig.ax=plt.subplots()
_=ax.set_title("Alcohol in 18-29")
_=percent['characteristic'].str.match('18-19')|plot.bar(ax=ax)
_=ax.set_sticklabels(percent['characteristic'])
_=ax.grid()


# In[ ]:




