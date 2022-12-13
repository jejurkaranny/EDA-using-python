#!/usr/bin/env python
# coding: utf-8

# importing required libraries.
# For Analysis we are using libreries to visualize inforamtion.

# In[242]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import datetime as datetime
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import tools
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import warnings
warnings.filterwarnings("ignore")


# Reading the file using read.csv using pandas

# In[192]:


dt=pd.read_csv("C:\\Users\\Admin\\Downloads\\covid-variants.csv")


# 1. Finding Basic information about data 

# In[193]:


dt.columns


# In[194]:


dt.head(10)


# In[98]:


dt.tail()


# In[99]:


dt.shape


# from the above details of file we found,
# The data (COVID-19 Variants) contains the following information:
# 
# location- this is the country for which the variants information is provided.
# 
# date - date for the data entry.
# 
# variant - this is the variant corresponding to this data entry.
# 
# num_sequences - the number of sequences processed (for the country, variant and date).
# 
# perc_sequences - percentage of sequences from the total number of sequences (for the country, variant and date).
# 
# num_sequences_total - total number of sequences (for the country, variant and date).

# In[100]:


dt.describe()


# showing data types of columns if required then we can change the data type.

# In[49]:


data.info() 


# In[101]:


#converting date Dtype oject to Dtype date
dt["date"]=dt["date"].apply(pd.to_datetime, dayfirst=True)
dt=dt.fillna(0)


# In[103]:


dt.info()


#  Finding the Null values

# In[104]:


#count or check any missing values
dt.isnull().sum() 


#  Finding Duplicate values

# In[105]:


# find any duplicate
dt.duplicated().sum()


# Unique values in the data

# In[106]:


# countries
countries=dt['location'].unique()
countrie=pd.Series(countries)
countrie


# In[107]:


# types of varients 
var=dt['variant'].unique()
varients=pd.Series(var)
varients


# varient wise number of sequence occured 

# In[216]:


variants=dt.variant.unique()
variant_num_seq=[]
for i in variants:
    x=dt[dt.variant.values==i]
    num_seq=sum(x.num_sequences)
    variant_num_seq.append(num_seq)
    
    
variant_set=pd.DataFrame({"variant":variants,"number_of_sequence":variant_num_seq})
var_index=variant_set.number_of_sequence.sort_values(ascending=False).index.values
variant_set=variant_set.reindex(var_index)
variant_set


# In[244]:


sb.barplot(variant_set.number_of_sequence.head(10),variant_set.variant.head(10))
plt.show()


# From above barplot wd can conclude the most number of sequences occure varient is delta.
# also we can see the top 10 varient in geven data set.

# In[ ]:


Last date analysis of covid variant data


# In[245]:


last_date_data_df = sample.groupby(["variant", "Location"])["date"].max().reset_index()
print(last_date_data_df.shape)
last_date_data_df


# In[231]:


last_date_data_df = last_date_data_df.merge(sample, how="left")#merging data using left join
print(last_date_data_df.shape)
last_date_data_df.head()


# In[233]:


print(f"Countries number: {last_date_data_df.Location.nunique()}")
print(f"Date number: {last_date_data_df.date.nunique()}")
print(f"Variants number: {last_date_data_df.variant.nunique()}")
print(f"Variants names: {last_date_data_df.variant.unique()}")


# In[238]:


fig = px.treemap(last_date_data_df, path = ['variant', 'Location'], values = 'perc_sequences',
                title="Percentage sequences per country and variant (last time registered/variant and country)")
fig.show()


# the tree map of last day data shows the delta and omicron varients are more active in lots of countries as compair to
# other varients.

# In[129]:


# Using groupby() and count() to  check country wise sequence in desc
data3 = dt.groupby(['location'])['num_sequences_total'].sum().sort_values(ascending=False)
data3


# In[243]:


country=data3.head(10)
plt.figure(figsize=(10,5))
sb.barplot(data3.head(10).values,data3.head(10).index)
plt.title("top 10 country sequence wise")
plt.ylabel("country",fontsize=10)
plt.xlabel("number of sequence",fontsize=10)
plt.show()


# In given data set number of sequence occures is higher in US follwed by UK.so we can conclude that US and UK are most affected areas in covid.

# In[108]:


sample  = dt.rename(columns={"location":"Location","num_sequences_total":"Number of Case"})
sample


# Tree map of a all data set to visualize the affection of covid varients country wise.

# In[248]:


fig = px.treemap(sample, path=[px.Constant('Number of Case'),'Location'],values='Number of Case',hover_data=['Location'],
                title='country wise cases of covid')


# In[249]:


fig.show()


# Yearwise total cases of cove from given data set

# In[111]:


#get year from corresponding date column
data['year']=pd.DatetimeIndex(dt['date']).year


# In[114]:


#yearwise sequences occured..
data2 = data.groupby(['year'])['num_sequences_total'].sum()
data2


# In[115]:


#correlation between data
dt.corr()


# In[253]:


#Correlation Plot 
Correlation_Plot=sb.heatmap(dt.corr())


# In[ ]:




