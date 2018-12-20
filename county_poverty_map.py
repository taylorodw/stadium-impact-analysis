from bokeh.io import show, output_file
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.plotting import figure
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.unemployment import data as unemployment
import pandas as pd

datafile = "D:\\Stadiums Project\\df_pcts.csv"
ca_pcts = pd.read_csv(datafile)
ca_poverty = ca_pcts[['NAME', 'pctpoverty']]

# the first time you run this, and after importing bokeh, you'll have to run bokeh.sampledata.download()

palette.reverse()

# is this a lambda function? a dictionary?
counties = {
  code: county for code, county in counties.items() if county["state"] == "ca"
}

# getting x/y coords from the lon/lat in dataframe county
county_xs = [county["lons"] for county in counties.values()]
county_ys = [county["lats"] for county in counties.values()]

# getting the data
county_names = ca_poverty['NAME']
county_rates = ca_poverty['pctpoverty']
color_mapper = LogColorMapper(palette=palette)

# assigning data to shorter variables in order to feed them into bokeh
data=dict(
  x=county_xs,
  y=county_ys,
  name=county_names,
  rate=county_rates,
)

output_file('ca_county_poverty.html')

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
  title="California Poverty, 2016", tools=TOOLS,
  x_axis_location=None, y_axis_location=None,
  tooltips=[
    ("Name", "@name"), ("Poverty %", "@rate{1.11%}"), ("(Long, Lat)", "($x, $y)")
  ]
)
p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

# using the patches glyph on p
p.patches('x', 'y', source=data,
  fill_color={'field': 'rate', 'transform': color_mapper},
  fill_alpha=0.7, line_color="white", line_width=0.5)

show(p)
