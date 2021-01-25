import pandas as pd
import numpy as np
import sys
import re
import matplotlib.pyplot as plot

param = 'overall'

for x in sys.argv:
    if (x == '--help'):
        print ("To define a specific range use '--range=row:row' \n Example: '--range=3:5'")
        print ("To define a specific option use '--option=option' \n Example: '--option=age'")
        exit()
    if ("--option" in x):
        a = x.split('=', 1)
        option = a[1]
        print (option)
        if (option == "age" or option == "hits"):
            param = option
        else:
            print ("Wrong parameter, check --help")

    if ("--range=" in x):
        res = [int(num) for num in re.findall(r"\d+", x)]
        nbrows = (res[1] - res[0]) + 1
        skip_range = range(1, res[0])
        dataset = pd.read_csv("data.csv", skiprows=skip_range,nrows=nbrows)
    else:
        dataset = pd.read_csv("data.csv")


print(dataset) 
pd.show_versions()
# change here to print different variable 
dataset.plot.scatter(y='hits', x='potential', c=param, colormap='viridis' , title= "Scatter plot between potential and hits")
# show the scatter plot 
plot.show(block=True);