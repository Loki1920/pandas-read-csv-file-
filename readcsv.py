
import pandas as pd
df = pd.read_csv('data.csv')
#print(df.to_string())
print(pd.options.display.max_rows)
pd.options.display.max_rows = 999
print(df)
