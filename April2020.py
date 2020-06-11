#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:54:29 2020

@author: zhangjinwen
"""

from urllib.parse import unquote, parse_qs
import pandas as pd
import json

#load the csv file using pandas, 
# put the parameter "error_bad_lines" if there is any 
# unsupported data that pandas can't deal with it will skip. 

data = pd.read_csv("~/Loggings/April 2020.csv",error_bad_lines=False)

# fill the empty string and blank fields with NULL value.
df = data.fillna('NULL')

# function that will decode the data (raw columns in csv file)
def title_parse(title):
    title = unquote(title)
    return title

# apply from pandas will help to all the decode text in  the csv
df['title'] = df.title.apply(title_parse)

# write the decoded data in a new csv file using "to_csv" method from pandas
df.to_csv('decoded.csv')

c = pd.read_csv("~/Loggings/decoded.csv",error_bad_lines=False)
    
# the first columns of data frame contained raw data
d = c.iloc[:,1] 

e = json.loads(d[1]) # fail in this step

dff['title'] = dff.title.apply(json.loads) # JSONDecodeError


 























