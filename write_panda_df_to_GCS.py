#!/usr/bin/env python
# coding: utf-8

# # import required Libraries

# In[1]:


import os
import pandas_gbq
# Imports the Google Cloud client library
from google.cloud import storage


# # set up the authentication with GCP

# In[2]:


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\hemant\Desktop\python\rare-botany-344514-28d0a845d6c3.json"


# # Read query data into dataframe

# In[3]:


#Reading from bq
# TODO: Set project_id to your Google Cloud Platform project ID.
project_id = "rare-botany-344514"

sql = """
SELECT * FROM mydataset1.emp1
"""
df = pandas_gbq.read_gbq(sql, project_id=project_id)


# # Write the dataframe to GCS bucket

# In[5]:


##Writing dataframe to gcs bucket
# Imports the Google Cloud client library


# Instantiates a client
storage_client = storage.Client()

bucket_name = "rare-botany-344514_source_data"

#get bucket details
bucket = storage_client.get_bucket(bucket_name)

#declare blob object name
blob = bucket.blob('my-test-file5.csv')

#Adding df to GCS using df.to_csv() method
blob.upload_from_string(df.to_csv(index=False),content_type='application/octet-stream')

#blob.upload_from_string(df.to_csv(sep=';',index=False,encoding='utf-8'),content_type='application/octet-stream')


# # List blobs in a bucket

# In[7]:


bucket_name = "rare-botany-344514_source_data"

#get bucket details
bucket = storage_client.get_bucket(bucket_name)

#get list of Blobs
blobs = bucket.list_blobs()

print("Blobs in {}:".format(bucket.name))
for item in blobs:
    print("\t" + item.name)







