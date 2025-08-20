#!/usr/bin/env python
# coding: utf-8

# In[5]:


from faker import Faker 
import pandas as pd 
import random 
import os

# create data folder path
data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(data_folder, exist_ok=True)

fake = Faker()
data =[] 
countries = ['UAE', 'UK','India', 'Nigeria','Russia', 'USA']
pep_status = ["Yes", "No"]

for i in range(20):
    data.append({
        
        "client_id" : f"c{i+1:03d}",
        "name" : fake.name(),
        "country": random.choice(countries),
        "pep": random.choice(pep_status),
         "wallet_address": fake.hexify(text='0x^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    })

df = pd.DataFrame(data)
csv_path = os.path.join(data_folder, "clients.csv")
df.to_csv(csv_path, index=False)
print(f"Sample clients generated and saved to {csv_path}")


# In[ ]:




