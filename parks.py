#import necessary modules
import csv

import pandas as pd

import bokeh

#read csv data frame
df = pd.read_csv('parks.csv')

#import necessary plotting imports
from bokeh.charts import Donut, output_file, save

#import palette
from bokeh.palettes import plasma

#set up the bar graph components
d = Donut(df, label='Park Name', values='State' and 'Acres', title='Parks by Size', text_font_size='7pt', hover_text='#', palette=plasma(18))

#create output file
output_file("piegraph.html")

#save the pie graph to file
save(d)
