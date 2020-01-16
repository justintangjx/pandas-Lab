import pandas as pd
pd.__version__
import matplotlib.pyplot as plt
import numpy as np

df_rainfall = pd.read_csv('./rainfall-monthly-total.csv', index_col="month")

moreThan300DF = df_rainfall.loc[df_rainfall['total_rainfall'] > 300]
top12 = moreThan300DF.sort_values(by='total_rainfall', ascending=False).head(12)
# top12.count()
index = np.arange(12)
plt.bar(index, top12['total_rainfall'])
plt.xlabel('month', fontsize=8)
plt.xticks(index, top12.index, fontsize=6)

plt.show()
