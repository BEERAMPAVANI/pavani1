#!/usr/bin/env python
# coding: utf-8

# Multilinear regression
# 
# **Assumptions in Multilinear Regression 
# 1. Linearity: The relationship between the predictors and the resporse a linear 
# 2. Independence Deservations are ndependent of sach other 
# 3. Nomoscedasticity. The residuals (differences between observed and predicted values) exhibit constant variance at all levels of the predictor. 
# 4. Normal Distribution of Emons. The residuals of the model are normally distributed. 
# 5. No murticolineinty. The independent variables should not be too highly comslated with each other 
# 
# Violations of these assumptions may lead to inefficiency in the regression parameters and unreliable predictions 

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[3]:


cars=pd.read_csv("Cars.csv")
cars.head()


# In[4]:


cars= pd.DataFrame(cars,columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# ### Desription of columns
# - MPG : Milege of the car(Mile per Gallon)
# - HP : Horse Power of the car
# - VOL : Volume of the car(size)
# - SP : Top speed of the car(Miles per Hour)
# - WT : Weight of the car(Pounds)

# In[6]:


cars.isna().sum()


# Observations
# 
# - There are no missing values
# - There are 81 observations
# - The data typesof the columns are relevant and valid

# In[11]:


fig, (ax_box, ax_hist)=plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, 85)}) 
#Creating a bokpint 
sns.boxplot(data=cars, x='HP', ax=ax_box, orient="h") 
ax_box.set(xlabel=' ')
##Creating a histogram in the same art 
sns.histplot(data=cars,x='HP', ax=ax_hist, bins=38, kde=True, stat="density") 
ax_hist.set(ylabel="Density") 
plt.tight_layout() 
plt.show() 


# In[ ]:





# In[ ]:




