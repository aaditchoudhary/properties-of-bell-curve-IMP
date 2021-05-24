import pandas as pd
import plotly.express as px
import math
import csv
import plotly.figure_factory as ff
import statistics
df=pd.read_csv(r"C:\Users\a2z\Downloads\Data-visualization-master\Data-visualization-master\csv files\properties of bell curve.csv")
height=df["Height(Inches)"].tolist()
weight=df["Weight(Pounds)"].tolist()
height_stddev=statistics.stdev(height)
print(height_stddev)
#x= statistics.mean(height)
#print("mean",x)
#y= statistics.median(height)
#print("median",y)
#z= statistics.mode(height)
#print("mode",z)
#fig=ff.create_distplot([height],["Height(Inches)"],show_hist=False)
#fig.show()