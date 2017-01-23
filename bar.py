import csv

import pandas as pd

import bokeh

df = pd.read_csv('parks.csv')

from bokeh.charts import Bar, output_file, save

p = Bar(df, 'Park Name', color='Park Name', title="Parks By Size")

output_file("bar.html")

save(p)
