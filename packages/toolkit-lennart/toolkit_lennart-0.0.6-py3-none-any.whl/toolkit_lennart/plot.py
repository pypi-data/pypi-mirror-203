import pandas as pd
import numpy as np
import plotly.express as px
import os


def helpfile():
    DIR = os.path.dirname(os.path.abspath(__file__))
    f = open(DIR + '/plot_help.txt', mode='r')
    print(f.read())
    return


# Desired functions:
# DF to line/scatter
# DF to multiple line/scatter in 1 plot
# DF to multiple line/scatter plots
# ...

def df_col_plot(df=None, x_name=None, y_name=None, help=False):
    if help:
        print('Plots two df columns. Arguments: df, x_name (df.index for index), y_name')
        return

    fig = px.scatter(df, x_name, y_name)
    return fig

def df_col_plot2(df=None, x_name=None, y_name=None, help=False):
    if help:
        print('Plots two df columns. Arguments: df, x_name (df.index for index), y_name')
        return

    fig = px.scatter(df, x_name, y_name)
    return fig
