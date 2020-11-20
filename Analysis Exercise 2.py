#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv("datasets/axisdata.csv")
df.head()


# In[8]:


import pandas as pd
Location = "datasets/axisdata.xlsx"
df = pd.read_excel(Location)
df.columns =['FirstName', 'Last Name','Gender','Hours Worked Per Week','Sales Training','Years of Experience','Cars Sold Per Month']
df.head()


# In[9]:


import pandas as pd
Location = "datasets/axisdata.xlsx"
df = pd.read_excel(Location)
df.columns =['First Name', 'Last Name','Gender','Hours Worked Per Week','Sales Training','Years of Experience','Cars Sold Per Month']
meanCarsSoldPerMonth = df['Cars Sold Per Month'].mean()
stdCarsSoldPerMonth = df['Cars Sold Per Month'].std()
toprange = meanCarsSoldPerMonth + stdCarsSoldPerMonth * 1.96
botrange = meanCarsSoldPerMonth - stdCarsSoldPerMonth * 1.96
copydf = df
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           > toprange].index)
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           < botrange].index)
copydf


# In[10]:


import pandas as pd
Location = "datasets/axisdata.xlsx"
df = pd.read_excel(Location)
df.columns =['First Name', 'Last Name','Gender','Hours Worked Per Week','Sales Training','Years of Experience','Cars Sold Per Month']
q1 = df['Cars Sold Per Month'].quantile(.25)
q3 = df['Cars Sold Per Month'].quantile(.75)
iqr = q3- q1
toprange = q3 + iqr * 1.5
botrange = q1 - iqr * 1.5
copydf = df
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           > toprange].index)
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           < botrange].index)
copydf


# In[11]:


q1 = df['Cars Sold Per Month'].quantile(.25)
q3 = df['Cars Sold Per Month'].quantile(.75)
iqr = q3- q1
toprange = q3 + iqr * 1.5
botrange = q1 - iqr * 1.5
copydf = df
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           > toprange].index)
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           < botrange].index)
copydf


# In[12]:


meanCarsSoldPerMonth = df['Cars Sold Per Month'].mean()
stdCarsSoldPerMonth = df['Cars Sold Per Month'].std()
toprange = meanCarsSoldPerMonth + stdCarsSoldPerMonth * 1.96
botrange = meanCarsSoldPerMonth - stdCarsSoldPerMonth * 1.96
copydf = df
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           > toprange].index)
copydf = copydf.drop(copydf[copydf['Cars Sold Per Month']
                           < botrange].index)
copydf


# In[13]:


df_no_missing = df.dropna()
df_no_missing


# In[14]:


df.duplicated()


# In[15]:


df.drop_duplicates()


# In[20]:


df['Cars Sold Per Month'].mean()


# In[21]:


df['Cars Sold Per Month'].max()


# In[22]:


df['Cars Sold Per Month'].min()


# In[23]:


df[['Gender','Cars Sold Per Month']].head()


# In[25]:


df.loc[df['Gender']=='F']['Cars Sold Per Month'].mean()


# In[26]:


df.loc[df['Gender']=='M']['Cars Sold Per Month'].mean()


# In[28]:


df[['Last Name','Hours Worked Per Week','Cars Sold Per Month']].head()


# In[46]:


df.loc[df['Cars Sold Per Month'] > 3]['Hours Worked Per Week'].mean()


# In[47]:


df['Years of Experience'].mean()


# In[59]:


df.loc[df['Cars Sold Per Month'] > 3]['Years of Experience'].mean()


# In[64]:


df[['Sales Training','Cars Sold Per Month']].head()


# In[69]:


df.loc[df['Sales Training']=='Y']['Cars Sold Per Month'].mean()


# In[71]:


df = df.sort_values(by='Sales Training')
df.head(1000)


# In[133]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
dataframe = pd.DataFrame({'Col':
            np.random.normal(size=200)})
plt.scatter(dataframe.index, dataframe['Col'])
df = pd.read_excel('datasets/axisdata.xlsx', delimiter=',', nrows=40)


# In[134]:


df


# In[137]:


y = df['Cars Sold'];
x = df['Years Experience']


# In[138]:


plt.xlabel('Years Experience'); plt.ylabel('Cars Sold')
plt.scatter(x,y)


# In[139]:


df.plot()


# In[131]:


df.boxplot(column = "Hours Worked", by = "Gender")


# In[132]:


df.boxplot(column = "Cars Sold", by = "Gender")
axis1 = df.boxplot(by = "Gender", column = "Cars Sold" )
axis1.set_ylim(3,6)


# In[ ]:




