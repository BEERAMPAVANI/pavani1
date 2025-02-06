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

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[2]:


cars=pd.read_csv("Cars.csv")
cars.head()


# In[3]:


cars= pd.DataFrame(cars,columns=["HP","VOL","SP","WT","MPG"])
cars.head()


# ### Desription of columns
# - MPG : Milege of the car(Mile per Gallon)
# - HP : Horse Power of the car
# - VOL : Volume of the car(size)
# - SP : Top speed of the car(Miles per Hour)
# - WT : Weight of the car(Pounds)

# In[4]:


cars.isna().sum()


# Observations
# 
# - There are no missing values
# - There are 81 observations
# - The data typesof the columns are relevant and valid

# In[5]:


fig, (ax_box, ax_hist)=plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, 85)}) 
#Creating a bokpint 
sns.boxplot(data=cars, x='HP', ax=ax_box, orient="h") 
ax_box.set(xlabel=' ')
##Creating a histogram in the same art 
sns.histplot(data=cars,x='HP', ax=ax_hist, bins=38, kde=True, stat="density") 
ax_hist.set(ylabel="Density") 
plt.tight_layout() 
plt.show() 


# Observations from boxplot and histograms
# 
# 1.There are some extreme values loutiersi observed in towards the right tail of SP and HP distributions 
# 
# 2.In VOL and WT columns, a few others are observed in both tais of their distributions 
# 
# 3.The extreme values of cars data may have come from the specially designed nature of cars 
# 
# 4.As this is multi-dimensional data the outliers with respect to spatial dimansions may have to be considered while building the regression madel 
# 
# Checking for duplicated rows 

# In[7]:


cars[cars.duplicated()]


# Pair plot Correlation Cofficients

# In[10]:


sns.set_style(style="darkgrid")
sns.pairplot(cars)


# In[11]:


cars.corr()


# Observations
# 
# 1.Trong correlation between HP and SP.
# 
# 2.VOL and WT show a very strong positive correlation.
# 
# 3.A negative relationship between HP and MPG, VOL and MPG, SP and MPG, and WT and MPG indicates that cars with higher performance characteristics.

# Observations from correlation plots and Coeffcients 
# 
# 1.Betwop the x variables showing moderate to high con slution strengths,highest being between HP and MPG 
# 
# 2.Therefore the dataset qualities for bulliding a multiple lincear regression model to predict MPG 
# 
# 3.Among x columns(x1,x2 x3 and x4) some very high correlation strengths are observed between SP vs HP, VOL vs WT 
# 
# 4.The high comelation among columns is not desirable as it might lead to multi collinearity problem 
# 

# Preparing a preliminary model considering all X columns 

# In[16]:


model1=smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[17]:


model1.summary()


# In[ ]:




