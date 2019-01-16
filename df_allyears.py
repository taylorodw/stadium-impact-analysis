import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


# getting data
print("Choose a file for 2011.")
file_2011 = filedialog.askopenfilename()
print("Chosen: " + file_2011)
print("Choose a file for 2012.")
file_2012 = filedialog.askopenfilename()
print("Chosen: " + file_2012)
print("Choose a file for 2013.")
file_2013 = filedialog.askopenfilename()
print("Chosen: " + file_2013)
print("Choose a file for 2014.")
file_2014 = filedialog.askopenfilename()
print("Chosen: " + file_2014)
print("Choose a file for 2015.")
file_2015 = filedialog.askopenfilename()
print("Chosen: " + file_2015)
print("Choose a file for 2016.")
file_2016 = filedialog.askopenfilename()
print("Chosen: " + file_2016)

# dfing the data
df_2011 = pd.read_csv(file_2011)
df_2012 = pd.read_csv(file_2012)
df_2013 = pd.read_csv(file_2013)
df_2014 = pd.read_csv(file_2014)
df_2015 = pd.read_csv(file_2015)
df_2016 = pd.read_csv(file_2016)

# creating master df, df_allyears
df_allyears = pd.DataFrame()
df_allyears['NAME'] = df_2011['NAME']

# poverty
df_allyears['pov2011'] = df_2011['pctpoverty']
df_allyears['pov2012'] = df_2012['pctpoverty']
df_allyears['pov2013'] = df_2013['pctpoverty']
df_allyears['pov2014'] = df_2014['pctpoverty']
df_allyears['pov2015'] = df_2015['pctpoverty']
df_allyears['pov2016'] = df_2016['pctpoverty']

# food stamps/SNAP
df_allyears['fs2011'] = df_2011['pctfoodstamps']
df_allyears['fs2012'] = df_2012['pctfoodstamps']
df_allyears['fs2013'] = df_2013['pctfoodstamps']
df_allyears['fs2014'] = df_2014['pctfoodstamps']
df_allyears['fs2015'] = df_2015['pctfoodstamps']
df_allyears['fs2016'] = df_2016['pctfoodstamps']

# unemployment
df_allyears['unemp2011'] = df_2011['unemploymentrate']
df_allyears['unemp2012'] = df_2012['unemploymentrate']
df_allyears['unemp2013'] = df_2013['unemploymentrate']
df_allyears['unemp2014'] = df_2014['unemploymentrate']
df_allyears['unemp2015'] = df_2015['unemploymentrate']
df_allyears['unemp2016'] = df_2016['unemploymentrate']

# gentrification?
df_allyears['white2011'] = df_2011['pctwhite']
df_allyears['white2012'] = df_2012['pctwhite']
df_allyears['white2013'] = df_2013['pctwhite']
df_allyears['white2014'] = df_2014['pctwhite']
df_allyears['white2015'] = df_2015['pctwhite']
df_allyears['white2016'] = df_2016['pctwhite']

# income
df_allyears['hhinc2011'] = df_2011['hhincomeE']
df_allyears['hhinc2012'] = df_2012['hhincomeE']
df_allyears['hhinc2013'] = df_2013['hhincomeE']
df_allyears['hhinc2014'] = df_2014['hhincomeE']
df_allyears['hhinc2015'] = df_2015['hhincomeE']
df_allyears['hhinc2016'] = df_2016['hhincomeE']

print("Choose a filename to write the unfiltered dataframe to .csv and .html")
save_name = filedialog.asksaveasfilename()
full_csv_name = save_name + ".csv"
full_html_name = save_name + ".html"

df_allyears.to_csv(full_csv_name)
df_allyears.to_html(full_html_name)

county_filter = ['Sullivan County, New York', 'Ulster County, New York', 'Dutchess County, New York', 'Orange County, New York', 'Putnam County, New York', 'Rockland County, New York', 'Westchester County, New York', 'Bronx County, New York', 'New York County, New York', 'Queens County, New York', 'Kings County, New York', 'Richmond County, New York', 'Nassau County, New York', 'Suffolk County, New York']
df_filter = df_allyears['NAME'].isin(county_filter)
df_stats = df_allyears[df_filter]

print("Choose a filename to write the county-filtered dataframe to .csv and .html")
save_name = filedialog.asksaveasfilename()
full_csv_name = save_name + ".csv"
full_html_name = save_name + ".html"

df_stats.to_csv(full_csv_name)
df_stats.to_html(full_html_name)
