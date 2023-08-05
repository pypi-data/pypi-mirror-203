### To play around with code in the other files ###

# if __name__ == '__main__':
from toolkit_lennart.plot import *

df = pd.DataFrame([1,1,2,3,5,8,13,21,34,55], list(range(10)))
fig = df_col_plot(df, df.index, 0)
fig.show()