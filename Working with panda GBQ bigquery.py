#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas-gbq')


# In[3]:


import os


# In[4]:


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\hemant\Desktop\python\rising-cable-340114-2e9cf13ab951.json"


# # Reading from Bigquery table

# In[5]:


import pandas_gbq

# TODO: Set project_id to your Google Cloud Platform project ID.
project_id = "rising-cable-340114"

sql = """
SELECT * FROM `rising-cable-340114.mydataset1.emp1`
"""
df = pandas_gbq.read_gbq(sql, project_id=project_id)


# In[10]:


df


# # write result to bigquery

# In[11]:


table_id="mydataset1.emp3"
pandas_gbq.to_gbq(df, table_id, project_id=project_id,if_exists='replace')


# In[ ]:




