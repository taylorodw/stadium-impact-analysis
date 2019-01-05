# This file will generate 3 maps - poverty rate, unemployment rate, and food stamp/SNAP usage rate
# It's set up for New York but that can easily be changed
# The counties are filtered by a list, then the dataframe is filtered by the same list
# The script can be adapted to map different parameters from our dataframe too
# the first time you run this, and after importing bokeh, you'll have to run bokeh.sampledata.download() to get the county boundaries

from bokeh.io import show, output_file
from bokeh.models import LinearColorMapper, ColorBar, Label, WheelZoomTool
from bokeh.models.tickers import ContinuousTicker, SingleIntervalTicker
from bokeh.palettes import viridis
from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.layouts import row
import pandas as pd
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

# getting the csv file
file_input = filedialog.askopenfilename()
print("Selected: " + file_input)

# Naming
print("Title the maps: ")
input_state = input("Name of the state > ")
input_year = input("Year of the map > ")
desired_filename = input("Output filename > ")
parsed_filename = desired_filename + ".html"
print(parsed_filename)
output_file(parsed_filename)

# parsing name inputs
povertytitle = input_state + " Poverty Rate, " + input_year
fsratetitle = input_state + " Food Stamp/SNAP use, " + input_year
unemptitle = input_state + " Unemployment Rate, " + input_year

# creating dataframes and filter to stats we'll use
datafile = file_input
df_pcts = pd.read_csv(datafile)
df_stats_unfiltered = df_pcts[['totalpopE', 'NAME', 'pctpoverty', 'pctfoodstamps', 'unemploymentrate']]

# listing the counties we want the map to show
county_filter = ['Sullivan County, New York', 'Ulster County, New York', 'Dutchess County, New York', 'Orange County, New York', 'Putnam County, New York', 'Rockland County, New York', 'Westchester County, New York', 'Bronx County, New York', 'New York County, New York', 'Queens County, New York', 'Kings County, New York', 'Richmond County, New York', 'Nassau County, New York', 'Suffolk County, New York']

df_filter = df_stats_unfiltered['NAME'].isin(county_filter)
df_stats = df_stats_unfiltered[df_filter]

# filtering counties
counties = {
  code: county for code, county in counties.items() if county["state"] == "ny" and (county["detailed name"] in county_filter)
}

# getting x/y coords from the lon/lat in dataframe county
county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

# getting the data
county_pop = df_stats['totalpopE']
county_names = df_stats['NAME']
county_poverty = df_stats['pctpoverty']
county_fsrate = df_stats['pctfoodstamps']
county_unemprate = df_stats['unemploymentrate']

# setting up color mapping to data
pov_palette = viridis(11)
unemp_palette = viridis(14)
fs_palette = viridis(13)
pov_palette.reverse()
unemp_palette.reverse()
fs_palette.reverse()
pov_color_mapper = LinearColorMapper(palette=pov_palette, low=0, high=0.11)
unemp_color_mapper = LinearColorMapper(palette=unemp_palette, low=0, high=0.07)
fs_color_mapper = LinearColorMapper(palette=fs_palette, low=0, high=0.13)

# assigning data to dictionary in order to feed them into bokeh
data=dict(
  x=county_xs,
  y=county_ys,
  name=county_names,
  poverty=county_poverty,
  fsrate=county_fsrate,
  unemprate=county_unemprate,
  totpop=county_pop
)

# assigning plot tools
TOOLS = "pan,wheel_zoom,reset,hover,save"

# generating the poverty plot
poverty = figure(
  title=povertytitle, tools=TOOLS, toolbar_location=None,
  x_axis_location=None, y_axis_location=None,
  tooltips=[
    ("Name", "@name"), ("Population", "@totpop"), ("Poverty %", "@poverty{1.11%}"), ("(Long, Lat)", "($x, $y)")
  ]
)
poverty.grid.grid_line_color = None
poverty.hover.point_policy = "follow_mouse"

# using the patches glyph on poverty
poverty.patches('x', 'y', source=data,
  fill_color={'field': 'poverty', 'transform': pov_color_mapper},
  fill_alpha=1, line_color="white", line_width=0.5)

# generating the SNAP plot
fsrate = figure(
  title=fsratetitle, tools=TOOLS, toolbar_location=None,
  x_axis_location=None, y_axis_location=None,
  tooltips=[
    ("Name", "@name"), ("Population", "@totpop"), ("SNAP %", "@fsrate{1.11%}"), ("(Long, Lat)", "($x, $y)")
  ]
)
fsrate.grid.grid_line_color = None
poverty.hover.point_policy = "follow_mouse"

# using the patches glyph on fsrate
fsrate.patches('x', 'y', source=data,
  fill_color={'field': 'fsrate', 'transform': fs_color_mapper},
  fill_alpha=1, line_color="white", line_width=0.5)

# generating the unemployment plot
unemprate = figure(
  title=unemptitle, tools=TOOLS, toolbar_location=None,
  x_axis_location=None, y_axis_location=None,
  tooltips=[
    ("Name", "@name"), ("Population", "@totpop"), ("Unemployment Rate", "@unemprate{1.11%}"), ("(Long, Lat)", "($x, $y)")
  ]
)
unemprate.grid.grid_line_color = None
unemprate.hover.point_policy = "follow_mouse"

# using the patches glyph on fsrate
unemprate.patches('x', 'y', source=data,
  fill_color={'field': 'unemprate', 'transform': unemp_color_mapper},
  fill_alpha=1, line_color="white", line_width=0.5)

# making scroll active by default
poverty.toolbar.active_scroll = poverty.select_one(WheelZoomTool)
fsrate.toolbar.active_scroll = fsrate.select_one(WheelZoomTool)
unemprate.toolbar.active_scroll = unemprate.select_one(WheelZoomTool)

# making a legend
pov_color_bar = ColorBar(color_mapper=LinearColorMapper(palette=pov_palette, low=0, high=11), ticker=SingleIntervalTicker(interval=1), title="Population in poverty (%)",
                     label_standoff=12, width=220, orientation="horizontal", border_line_color=None, location=(0,0))

unemp_color_bar = ColorBar(color_mapper=LinearColorMapper(palette=unemp_palette, low=0, high=7), ticker=SingleIntervalTicker(interval=.5), title="Unemployment rate (%)",
                     label_standoff=12, width=220, orientation="horizontal", border_line_color=None, location=(0,0))

fs_color_bar = ColorBar(color_mapper=LinearColorMapper(palette=fs_palette, low=0, high=13), ticker=SingleIntervalTicker(interval=1), title="Food Stamps/SNAP use (%)",
                     label_standoff=12, width=220, orientation="horizontal", border_line_color=None, location=(0,0))

# adding the legend below each map
poverty.add_layout(pov_color_bar, 'below')
unemprate.add_layout(unemp_color_bar, 'below')
fsrate.add_layout(fs_color_bar, 'below')

# linking the zoom/pan
unemprate.x_range = poverty.x_range
fsrate.x_range = poverty.x_range
unemprate.y_range = poverty.y_range
fsrate.y_range = poverty.y_range

# citing sources
citation = Label(x=0, y=0, x_units='screen', y_units='screen', text='Source: US Census American Community Survey', border_line_color=None, background_fill_color='white', background_fill_alpha=0.7)
poverty.add_layout(citation)

# arranging our maps in a row
layout = row(poverty, unemprate, fsrate)

show(layout)
