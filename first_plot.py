import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool, ColumnDataSource, NumeralTickFormatter

# loading a dataframe to visualize
datafile = 'D:\Stadiums Project\df_pcts.csv'
df_pcts = pd.read_csv(datafile)

# setting the filename
output_file('hhincome_pctpoverty.html')

# telling bokeh to use our dataframe
source = ColumnDataSource(df_pcts)

# formatting the tooltip for hover-over behavior
hover = HoverTool(tooltips=[("County", "@NAME")])

# formatting the graph with labels
plot = figure(x_axis_label='Average Household Income (dollars)', y_axis_label='Percentage of population in poverty')

# adding the hover-over behavior
plot.add_tools(hover)

# formatting the units. Y axis goes from decimal to percentage, X axis displays a regular number (for some reason bokeh defaults to scientific notation here, so we have to correct that)
plot.yaxis.formatter = NumeralTickFormatter(format='0 %')
plot.xaxis.formatter = NumeralTickFormatter(format="00")

# putting the data into the graph! this is the money part.
plot.circle('hhincomeE', 'pctpoverty', source=source, hover_color='red', size=8)

show(plot)
