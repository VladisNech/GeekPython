import pandas as pd
import matplotlib.pyplot as plt

my_series = pd.Series([-1, 5, 6, 7, 8, 9, 10])
print(my_series[4])
print(my_series)

print(my_series.index)
print(my_series.values)

print(my_series[my_series > 0])
print(my_series[my_series > 0] * 2)

df = pd.read_csv('apple.csv', index_col='Date', parse_dates=True)
df = df.sort_index()
print(df.info())

print(df.loc['2012-Feb', 'Close'].mean())
print(df.loc['2012-Feb':'2015-Feb', 'Close'].mean())
print(df.resample('W')['Close'].mean())


new_sample_df = df.loc['2012-Feb':'2017-Feb', ['Close']]
new_sample_df.plot()
plt.show()
