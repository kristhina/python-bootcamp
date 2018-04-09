import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("dane_csv.csv")
print(data)

sns.distplot(data['wzrost'], kde = True)

plt.show()