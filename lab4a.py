
import pandas as pd
pd.__version__

df = pd.read_excel('./singstats_maritalstatus.xlsx', index_col="Variables")
mydf = df['1980']
mydf

print(mydf.loc[ mydf[:] > 500000])
rowsMoreThan500k = mydf.loc[ mydf[:] > 500000].count()
print(rowsMoreThan500k)

print(mydf.loc[ mydf[:] < 500000])
rowsLessThan500k = mydf.loc[ mydf[:] < 500000].count()
print(rowsLessThan500k)

print('*** Data in 1980 column ***')
print(mydf)
print('\n')
print('Number of rows more than 500k is ', rowsMoreThan500k)
print('Number of rows less than 500k is ', rowsLessThan500k)

contains201 = '^201'
df_2010_and_after = df.filter(regex=contains201)
df_2010_and_after

newDF = df.head(10)
import numpy as np
print(" **** First 10 rows of original dataset ***")
myDF = newDF.replace('-', np.nan)
myDF

print("**** Remaining dataset after dropping columns with missing data ****")
myDF.dropna(1)
