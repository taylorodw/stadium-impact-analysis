# This file will generate 3 maps - poverty rate, unemployment rate, and food stamp/SNAP usage rate
# It's set up for New York but that can easily be changed
# The counties are filtered by a list, then the dataframe is filtered by the same list
# The script can be adapted to map different parameters from our dataframe too
# the first time you run this, and after importing bokeh, you'll have to run bokeh.sampledata.download() to get the county boundaries

from bokeh.io import show, output_file
from bokeh.models import LinearColorMapper, ColorBar, Label, WheelZoomTool, HoverTool
from bokeh.models.tickers import ContinuousTicker, SingleIntervalTicker
from bokeh.palettes import viridis
from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.models.widgets import Panel, Tabs
from bokeh.embed import components
import pandas as pd
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

# getting the csv file
print("Choose a file for 2011.")
file_2011 = filedialog.askopenfilename()
print("Choose a file for 2016.")
file_2016 = filedialog.askopenfilename()
print("Selected: " + file_2011 + " and " + file_2016)

# Naming
print("Title the maps: ")
input_state = input("Name of the state > ")
desired_filename = input("Output filename > ")
parsed_filename = desired_filename + ".html"
print(parsed_filename)
output_file(parsed_filename, title=input_state + " change from 2011-2016")

# parsing name inputs
povertytitle = input_state + " Change in Poverty Rate, 2011-2016"
fsratetitle = input_state + " Change in Food Stamp/SNAP use, 2011-2016"
unemptitle = input_state + " Change in Unemployment Rate, 2011-2016"

# creating dataframes and filter to stats we'll use

df1_raw = pd.read_csv(file_2011)
df2_raw = pd.read_csv(file_2016)
df_difference = pd.DataFrame()
df_difference['NAME'] = df1_raw['NAME']
df_difference['totalpopE'] = df2_raw['totalpopE'] - df1_raw['totalpopE']
df_difference['2016pop'] = df2_raw['totalpopE']
df_difference['pctpoverty'] = df2_raw['pctpoverty'] - df1_raw['pctpoverty']
df_difference['2016poverty'] = df2_raw['pctpoverty']
df_difference['pctfoodstamps'] = df2_raw['pctfoodstamps'] - df1_raw['pctfoodstamps']
df_difference['2016fsrate'] = df2_raw['pctfoodstamps']
df_difference['unemploymentrate'] = df2_raw['unemploymentrate'] - df1_raw['unemploymentrate']
df_difference['2016unemprate'] = df2_raw['unemploymentrate']
#df_difference['stadium'] = 'Barclays Center'


# listing the counties we want the map to show
county_filter = ['Sullivan County, New York', 'Ulster County, New York', 'Dutchess County, New York', 'Orange County, New York', 'Putnam County, New York', 'Rockland County, New York', 'Westchester County, New York', 'Bronx County, New York', 'New York County, New York', 'Queens County, New York', 'Kings County, New York', 'Richmond County, New York', 'Nassau County, New York', 'Suffolk County, New York']

df_filter = df_difference['NAME'].isin(county_filter)
df_stats = df_difference[df_filter]

# filtering counties
counties = {
  code: county for code, county in counties.items() if county["state"] == "ny" and (county["detailed name"] in county_filter)
}

# getting x/y coords from the lon/lat in dataframe county
county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

# getting the data
county_pop_diff = df_stats['totalpopE']
county_pop = df_stats['2016pop']
county_names = df_stats['NAME']
county_poverty_diff = df_stats['pctpoverty']
county_poverty = df_stats['2016poverty']
county_fsrate_diff = df_stats['pctfoodstamps']
county_fsrate = df_stats['2016fsrate']
county_unemprate_diff = df_stats['unemploymentrate']
county_unemprate = df_stats['2016unemprate']

# x/y and label for stadium
barclays_y = 40.6826 #long/lat for stadium
barclays_x = -73.9754
barclays_label1 = Label(x=-74.52, y=barclays_y, text='Barclays Center', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7, text_font_size='9pt')
barclays_label2 = Label(x=-74.52, y=barclays_y, text='Barclays Center', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7, text_font_size='9pt')
barclays_label3 = Label(x=-74.52, y=barclays_y, text='Barclays Center', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7, text_font_size='9pt')

# setting up color mapping to data
pov_palette = viridis(7)
unemp_palette = viridis(9)
fs_palette = viridis(7)
fs_palette.reverse()
unemp_palette.reverse()
pov_palette.reverse()
pov_color_mapper = LinearColorMapper(palette=pov_palette, low=-0.015, high=0.02)
unemp_color_mapper = LinearColorMapper(palette=unemp_palette, low=-0.015, high=0.03)
fs_color_mapper = LinearColorMapper(palette=fs_palette, low=-0.004, high=0.03)

# assigning data to dictionary in order to feed them into bokeh
data=dict(
  x=county_xs,
  y=county_ys,
  name=county_names,
  povertydiff=county_poverty_diff,
  poverty=county_poverty,
  fsrate=county_fsrate,
  fsratediff=county_fsrate_diff,
  unemprate=county_unemprate,
  unempratediff=county_unemprate_diff,
  totpop=county_pop,
  popdiff=county_pop_diff
)

# assigning plot tools
TOOLS = "pan,wheel_zoom,reset,save"

# generating the poverty plot
poverty = figure(
  title=povertytitle, tools=TOOLS, toolbar_location=None,
  x_axis_location=None, y_axis_location=None)

# using the patches glyph on poverty
pov_patches = poverty.patches('x', 'y', source=data,
  fill_color={'field': 'povertydiff', 'transform': pov_color_mapper},
  fill_alpha=1, line_color="white", line_width=0.5)

pov_hover = HoverTool(tooltips=[
  ("Name", "@name"), ("Population", "@totpop"), ("Population Change", "@popdiff"), ("Poverty %", "@poverty{1.11%}"), ("Poverty % Change", "@povertydiff{1.11%}"), ("(Long, Lat)", "($x, $y)")
], renderers=[pov_patches])
poverty.add_tools(pov_hover)
poverty.grid.grid_line_color = None
poverty.hover.point_policy = "follow_mouse"
poverty.circle(x=barclays_x, y=barclays_y, size=10, line_color="black", fill_color="silver", line_width=0.5)

# generating the SNAP plot
fsrate = figure(
  title=fsratetitle, tools=TOOLS, toolbar_location=None,
  x_axis_location=None, y_axis_location=None)

# using the patches glyph on fsrate
fs_patches = fsrate.patches('x', 'y', source=data,
  fill_color={'field': 'fsratediff', 'transform': fs_color_mapper},
  fill_alpha=1, line_color="white", line_width=0.5)

fs_hover = HoverTool(tooltips=[
   ("Name", "@name"), ("Population", "@totpop"), ("Population Change", "@popdiff"), ("SNAP %", "@fsrate{1.11%}"), ("SNAP % Change", "@fsratediff{1.11%}"), ("(Long, Lat)", "($x, $y)")
 ], renderers=[fs_patches])
fsrate.add_tools(fs_hover)
fsrate.grid.grid_line_color = None
fsrate.hover.point_policy = "follow_mouse"
fsrate.circle(x=barclays_x, y=barclays_y, size=10, line_color="black", fill_color="silver", line_width=0.5)

# generating the unemployment plot
unemprate = figure(
  title=unemptitle, tools=TOOLS, toolbar_location=None,
  x_axis_location=None, y_axis_location=None)

# using the patches glyph on fsrate
un_patches = unemprate.patches('x', 'y', source=data,
  fill_color={'field': 'unempratediff', 'transform': unemp_color_mapper},
  fill_alpha=1, line_color="white", line_width=0.5)

un_hover = HoverTool(tooltips=[
  ("Name", "@name"), ("Population", "@totpop"), ("Population Change", "@popdiff"), ("Unemployment Rate", "@unemprate{1.11%}"), ("Unemployment Rate Change", "@unempratediff{1.11%}"), ("(Long, Lat)", "($x, $y)")
], renderers=[un_patches])
unemprate.add_tools(un_hover)
unemprate.grid.grid_line_color = None
unemprate.hover.point_policy = "follow_mouse"
unemprate.circle(x=barclays_x, y=barclays_y, size=10, line_color="black", fill_color="silver", line_width=0.5)

# making scroll active by default
poverty.toolbar.active_scroll = poverty.select_one(WheelZoomTool)
fsrate.toolbar.active_scroll = fsrate.select_one(WheelZoomTool)
unemprate.toolbar.active_scroll = unemprate.select_one(WheelZoomTool)

# making a legend
pov_color_bar = ColorBar(color_mapper=LinearColorMapper(palette=pov_palette, low=-1.5, high=2), ticker=SingleIntervalTicker(interval=0.5), title="Change in Poverty (%) from 2011 to 2016",
                     label_standoff=12, width=220, orientation="horizontal", border_line_color=None, location=(0,0))

unemp_color_bar = ColorBar(color_mapper=LinearColorMapper(palette=unemp_palette, low=-1.5, high=3), ticker=SingleIntervalTicker(interval=0.5), title="Change in Unemployment rate (%) from 2011 to 2016",
                     label_standoff=12, width=220, orientation="horizontal", border_line_color=None, location=(0,0))

fs_color_bar = ColorBar(color_mapper=LinearColorMapper(palette=fs_palette, low=-0.5, high=3), ticker=SingleIntervalTicker(interval=0.5), title="Change in Food Stamps/SNAP use (%) from 2011 to 2016",
                     label_standoff=12, width=220, orientation="horizontal", border_line_color=None, location=(0,0))

# adding the label on barclays and legend below each map
poverty.add_layout(pov_color_bar, 'below')
unemprate.add_layout(unemp_color_bar, 'below')
fsrate.add_layout(fs_color_bar, 'below')
poverty.add_layout(barclays_label1)
fsrate.add_layout(barclays_label2)
unemprate.add_layout(barclays_label3)

# linking the zoom/pan
unemprate.x_range = poverty.x_range
fsrate.x_range = poverty.x_range
unemprate.y_range = poverty.y_range
fsrate.y_range = poverty.y_range

# citing sources
citation = Label(x=0, y=0, x_units='screen', y_units='screen', text='Source: US Census American Community Survey', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7)
citation2 = Label(x=0, y=0, x_units='screen', y_units='screen', text='Source: US Census American Community Survey', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7)
citation3 = Label(x=0, y=0, x_units='screen', y_units='screen', text='Source: US Census American Community Survey', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7)
poverty.add_layout(citation)
unemprate.add_layout(citation2)
fsrate.add_layout(citation3)

# arranging our maps in tabs
tab1 = Panel(child=poverty, title='Poverty')
tab2 = Panel(child=unemprate, title='Unemployment')
tab3 = Panel(child=fsrate, title='SNAP')
tabs = Tabs(tabs=[tab1, tab2, tab3])

show(tabs)
