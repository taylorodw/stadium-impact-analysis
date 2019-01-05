# Setting up our dataframe to process
import pandas as pd

datafile = "D:\Stadiums Projec\cali_acs2016.csv"

df_raw = pd.read_csv(datafile)

"""
We want to get populations as percentages. So we divide 'popwhiteE' by
'totalpopE' to find the percentage of a county that is white. Same structure for
all other population count statistics
"""

df_raw['pctwhite'] = df_raw['popwhiteE']/df_raw['totalpopE']
df_raw['pctblack'] = df_raw['popblackE']/df_raw['totalpopE']
df_raw['pctakna'] = df_raw['popaknaE']/df_raw['totalpopE']
df_raw['pctasian'] = df_raw['popasianE']/df_raw['totalpopE']
df_raw['pcthipi'] = df_raw['pophipiE']/df_raw['totalpopE']
df_raw['pctother'] = df_raw['popotherE']/df_raw['totalpopE']
df_raw['pct2ormore'] = df_raw['pop2ormoreE']/df_raw['totalpopE']
df_raw['pctpoverty'] = df_raw['poppovertyE']/df_raw['totalpopE']
df_raw['pctfoodstamps'] = df_raw['popfoodstampsE']/df_raw['totalpopE']
df_raw['unemploymentrate'] = df_raw['popunemploymentE']/df_raw['totalpopE']

# Now df_raw contains a per county percentage for each population group

# Check with df_raw.head (looks good!), then export as .csv and .html
df_raw.head()
df_raw.to_csv('D:\Stadiums Project\df_pcts.csv')
df_pcts.to_html('D:\Stadiums Project\df_pcts.html')

# Import csv as a new dataframe (I'm sure there is a more elegant way to do this?)
df_pcts = pd.read_csv(new_data)
new_data = "D:\Stadiums Project\df_pcts.csv"

# Checking that all of the % ethnicities add up to 100%, to ensure our method was correct

df_pcts['totalpct'] = df_pcts['pctwhite'] + df_pcts['pctblack'] + df_pcts['pctakna'] + df_pcts['pctasian'] + df_pcts['pcthipi'] + df_pcts['pctother'] + df_pcts['pct2ormore']

df_pcts.head()

# This should add up to 1 for each row
