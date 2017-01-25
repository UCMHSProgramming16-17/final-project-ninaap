#import necessary modules
import csv

import pandas as pd

import bokeh

#import/read the csv file
df = pd.read_csv('parks.csv')

#import necessary visual imports
from bokeh.charts import Bar, output_file, save

#set up bar graph visuals
p = Bar(df,label='Park Name', values='Acres', color='Park Name', title="Parks By Size")

#create the output file
output_file("bar.html")

#save bar graph to output file
save(p)
