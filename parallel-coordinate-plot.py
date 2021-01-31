import sys
import re
import pandas as pd
import matplotlib.pyplot as plot
import plotly.express as px

param = 'age'

for x in sys.argv:
    if (x == '--help'):
        print("To define a specific range use '--range=row:row' \n Example: '--range=3:5'")
        print(
            "To define a specific option use '--option=option' \n (age, hits, potential) \n Example: '--option=age'")
        exit()
    if ("--option" in x):
        a = x.split('=', 1)
        option = a[1]
        if (option == "age" or option == "hits" or option == "potential"):
            param = option
        else:
            print("Wrong parameter, check --help")

    if ("--range=" in x):
        res = [int(num) for num in re.findall(r"\d+", x)]
        nbrows = (res[1] - res[0]) + 1
        skip_range = range(1, res[0])
        dataset = pd.read_csv("data.csv",  usecols=[
                              "hits", "potential", "age"], skiprows=skip_range, nrows=nbrows)
    else:
        dataset = pd.read_csv("data.csv",  usecols=[
                              "hits", "potential", "age"])


fig = px.parallel_coordinates(dataset,
                              color=param,
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)
fig.show()
