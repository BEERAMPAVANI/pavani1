#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[2]:


data1 = pd.read_csv("NewspaperData.csv")
data1


# In[3]:


data1.info()


# #### Observation
# - 34 entries no null values

# In[4]:


print(type(data1))
print(data1.shape)
print(data1.size)


# In[5]:


plt.boxplot(data1["daily"], vert = False)


# In[6]:


plt.boxplot(data1["sunday"], vert = False)


# In[7]:


plt.scatter(data1["daily"],data1["sunday"])


# In[8]:


data1['daily'].corr(data1['sunday'])


# #### Observation
# - They have very high correlation strength between daily and sunday

# In[9]:


import statsmodels.formula.api as smf
model = smf.ols("sunday~daily",data = data1).fit()


# In[10]:


model.summary()


# In[11]:


x = data1["daily"].values
y = data1["sunday"].values
plt.scatter(x, y, color = "m", marker = "o", s = 30)
b0 = 13.84
b1 = 1.33
y_hat = b0 + b1*x
plt.plot(x, y_hat, color = "g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[12]:


x=data1["daily"]
y=data1["sunday"]
plt.scatter(data1["daily"],data1["sunday"])
plt.xlim(0,max(x)+100)
plt.ylim(0,max(y)+100)
plt.show()


# In[13]:


data1.corr(numeric_only=True)


# In[14]:


import statsmodels.formula.api as smf
model1=smf.ols("sunday~daily",data = data1).fit()


# In[15]:


model1.summary


# The probobility(P-values) for inter (beta_0) is 0.707 > 0.05
# Therefore the intercept co-efficient may not be that much significant in prediction
# However the p-values for "daily" (beta_1) is 0.00 < 0.05
# Therefore the beta_1 co-efficient is highly significant and is contributint to prediction.

# In[16]:


model1.params


# In[17]:


print(f'model t-values:\n{model1.tvalues}\n--------------------\nmodel p-values: \n{model1.pvalues}')


# In[18]:


(model1.rsquared,model1.rsquared_adj)


# In[19]:


newdata=pd.Series([200,300,1500])


# In[20]:


data_pred=pd.DataFrame(newdata,columns=['daily'])
data_pred


# In[21]:


model1.predict(data_pred)


# In[22]:


pred=model1.predict(data1["daily"])
pred


# In[23]:


data1["Y_hat"]=pred


# In[24]:


data1


# In[25]:


data1["residuals"]=data1["sunday"]-data1["Y_hat"]
data1


# In[26]:


mse=np.mean((data1["daily"]-data1["Y_hat"])**2)
rmse=np.sqrt(mse)
print("MSE: ",mse)
print("RMSE: ",rmse)


# In[27]:


plt.scatter(data1["Y_hat"], data1["residuals"])


# In[28]:


import statsmodels.api as sm
sm.qqplot(data1["residuals"],line='45',fit=True)
plt.show()


# In[ ]:


#### Assumptions in Linear simple linear regression
- Linear dependence between the x and y variables
- 

