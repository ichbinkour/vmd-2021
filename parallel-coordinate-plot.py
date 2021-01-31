import sys
import re
import pandas as pd
import matplotlib.pyplot as plot
import plotly.express as px


df = pd.read_csv("data.csv", usecols=["hits", "potential", "overall"])
fig = px.parallel_coordinates(df,
                              color="overall",
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)
fig.show()
