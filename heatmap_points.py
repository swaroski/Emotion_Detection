#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
#This function assumes that the CSV has 3 columns X, Y, name

#@getCordinatesDict  
def getCordinatesDict(csv_file):
    data = pd.read_csv(csv_file)
    df = pd.DataFrame(data)
    df['XY'] = df[['X', 'Y']].apply(tuple, axis=1)
    new_dict = df.groupby('frame')['XY'].apply(list).to_dict()
    return new_dict

