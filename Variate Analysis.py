#!/usr/bin/env python
# coding: utf-8

# ### Univariate, Bivariate and Multivariate analysis

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')


# In[4]:


df.head()


# In[6]:


df.shape


# In[17]:


df['species'].unique()


# In[15]:


df['species'].value_counts()


# ## Univariate analysis

# In[22]:


df_setosa = df.loc[df['species']=='setosa']


# In[28]:


df_versicolor = df.loc[df['species']=='versicolor']
df_virginica = df.loc[df['species']=='virginica']


# In[47]:


# since this is a univariate plot we only take the X value
# np.zewros_like is a function in matplotlib that plots against a null axis
plt.plot(df_setosa['sepal_length'],np.zeros_like(df_setosa['sepal_length']),'*')
plt.plot(df_virginica['sepal_length'],np.zeros_like(df_virginica['sepal_length']),'o')
plt.plot(df_versicolor['sepal_length'],np.zeros_like(df_versicolor['sepal_length']),'1')


# ## Bivariate Analysis

# In[68]:


sns.FacetGrid(df,hue='species',aspect=2,height = 5).map(plt.scatter,'sepal_length','sepal_width').add_legend()


# In[77]:


# trying with petal_length and pelt_width
sns.FacetGrid(df,hue='species',height= 5, aspect=2).map(plt.scatter,'petal_length','petal_width').add_legend()


# ## Multivariate analysis
#     - More than 2 features

# In[78]:


sns.pairplot(df,hue = 'species')

