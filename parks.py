import csv

import pandas as pd

import bokeh

df = pd.read_csv('parks.csv')

from bokeh.charts import Donut, output_file, save

from bokeh.palettes import plasma

d = Donut(df, label='Park Name', values='State' and 'Acres', title='Parks by Size', text_font_size='7pt', hover_text='#', palette=plasma(18))

output_file("piegraph.html")

save(d)
