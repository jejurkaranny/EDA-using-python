#!/usr/bin/env python
# coding: utf-8

# # Covid Varient EDA using Python

# Importing required libraries.
# For Analysis we are using libreries to visualize inforamtion.

# In[2]:


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

# In[3]:


dt=pd.read_csv("C:\\Users\\Admin\\Downloads\\covid-variants.csv")


# 1. Finding Basic information about data 

# In[4]:


dt.columns


# In[5]:


dt.head(10)


# In[6]:


dt.tail()


# In[7]:


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

# In[8]:


dt.describe()


# 2.showing data types of columns if required then we can change the data type.

# In[9]:


dt.info() 


# In[10]:


#converting date Dtype oject to Dtype date
dt["date"]=dt["date"].apply(pd.to_datetime, dayfirst=True)
dt=dt.fillna(0)


# In[11]:


dt.info()


# 3.Finding the Null values

# In[12]:


#count or check any missing values
dt.isnull().sum() 


# 4.Finding Duplicate values

# In[13]:


# find any duplicate
dt.duplicated().sum()


# 3.Unique values in the data

# In[14]:


# countries
countries=dt['location'].unique()
countrie=pd.Series(countries)
countrie


# In[15]:


# types of varients 
var=dt['variant'].unique()
varients=pd.Series(var)
varients


# 5.varient wise number of sequence occured 

# In[16]:


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


# In[17]:


sb.barplot(variant_set.number_of_sequence.head(10),variant_set.variant.head(10))
plt.show()


# 6.Last date analysis of covid variant data

# In[21]:


last_date_data_df = sample.groupby(["variant", "Location"])["date"].max().reset_index()
print(last_date_data_df.shape)
last_date_data_df


# In[22]:


last_date_data_df = last_date_data_df.merge(sample, how="left")#merging data using left join
print(last_date_data_df.shape)
last_date_data_df.head()


# In[23]:


print(f"Countries number: {last_date_data_df.Location.nunique()}")
print(f"Date number: {last_date_data_df.date.nunique()}")
print(f"Variants number: {last_date_data_df.variant.nunique()}")
print(f"Variants names: {last_date_data_df.variant.unique()}")


# In[24]:


fig = px.treemap(last_date_data_df, path = ['variant', 'Location'], values = 'perc_sequences',
                title="Percentage sequences per country and variant (last time registered/variant and country)")
fig.show()


# The tree map of last day data shows the delta and omicron varients are more active in lots of countries as compair to
# other varients.

# 7.country wise sequence

# In[25]:


# Using groupby() and sum() to  check country wise sequence in desc
data3 = dt.groupby(['location'])['num_sequences_total'].sum().sort_values(ascending=False)
data3


# In[26]:


country=data3.head(10)
plt.figure(figsize=(10,5))
sb.barplot(data3.head(10).values,data3.head(10).index)
plt.title("top 10 country sequence wise")
plt.ylabel("country",fontsize=10)
plt.xlabel("number of sequence",fontsize=10)
plt.show()


# In given data set number of sequence occures is higher in US follwed by UK.so we can conclude that US and UK are most affected areas in covid.

# In[20]:


sample  = dt.rename(columns={"location":"Location","num_sequences_total":"Number of Case"})
sample


# 8.Tree map of a all data set to visualize the affection of covid varients country wise.

# In[27]:


fig = px.treemap(sample, path=[px.Constant('Number of Case'),'Location'],values='Number of Case',hover_data=['Location'],
                title='country wise cases of covid')


# In[28]:


fig.show()


# 9.Yearwise total cases of cove from given data set

# In[49]:


#get year from corresponding date column
dt['year']=pd.DatetimeIndex(dt['date']).year


# In[50]:


#yearwise sequences occured..
data2 = dt.groupby(['year'])['num_sequences_total'].sum()
data2


# In[34]:


#correlation between data
dt.corr()


# In[253]:


#Correlation Plot 
Correlation_Plot=sb.heatmap(dt.corr())


# # Conclusion

# from the above analysis of file we found, The data (COVID-19 Variants) contains the following information:
# 1.From barplot of varients vs occurence we can conclude the most number of sequences occure varient is delta. also we can see the top 10 varient in geven data set.
# 
# 2. from the tree map of Percentage sequences per country and variant (last time registered/variant and country) we found the affection od varients country wise.delta and omicron afected in more countries.
# 
# 3.In bar chart of location and sequences we can see that  number of sequence occures is higher in US follwed by UK.so we can conclude that US and UK are most affected areas in covid.
# 
# 4. from given data also found that highest number of occurence in year 2021.
