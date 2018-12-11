import pandas as pd

datafile = "D:\Stadiums Project\cali_acs2016.csv"

df_raw = pd.read_csv(datafile)

df_raw.to_html('D:\Stadiums Project\df_raw.html')
