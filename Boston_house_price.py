
# coding: utf-8

# In[3]:

from sklearn import datasets
boston=datasets.load_boston()
# print(boston['DESCR'])


# In[6]:

import pandas as pd

boston_data=pd.DataFrame(boston.data)
boston_data.columns=boston['feature_names']
boston_data[:4]


# In[7]:

del boston_data['AGE']
del boston_data['INDUS']
boston_data[:4]


# In[11]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

y = boston['target']
x = boston_data['CRIM']
plt.ylabel('target')
plt.xlabel('CRIM')
plt.scatter(x,y)


# In[16]:

y = boston['target']
x = boston_data
x2 = sm.add_constant(x)
boston_model = sm.OLS(y,x2).fit()
boston_model.summary()


# In[ ]:



