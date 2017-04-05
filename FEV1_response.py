
# coding: utf-8

# In[10]:

import pandas as pd
import numpy as np

my_data = pd.read_csv("F:/graduate study/semester1/BIA652/assignment 2/lung.csv")
my_data[:4]


# In[11]:

y = my_data["FEV1_father"]
x = my_data['Age_father']
# y[:4]
#x[:4]


# In[12]:

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

plt.ylabel('FEV1 father')
plt.xlabel('Age_father')
plt.scatter(x,y)


# In[13]:

import statsmodels.api as sm
x2 = sm.add_constant(x)
est_lung = sm.OLS(y,x2).fit()
est_lung.params.values
#linear function yi=β0+β1xi+ϵiyi=β0+β1xi+ϵi
#get the β̂ 0, β̂ 1


# In[14]:

y_predict=x2.dot(est_lung.params.values)
plt.scatter(x,y)
plt.plot(x, y_predict,'r--')
plt.show()


# In[17]:

import scipy.stats as stats

est_lung.summary()
df=150-2
print(stats.t.ppf(1-0.05/2, df))
est_lung.summary()


# In[ ]:



