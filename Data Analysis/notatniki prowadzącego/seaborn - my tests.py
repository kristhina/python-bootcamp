import seaborn as sns
import pandas as pd

data = pd.read_csv("dane_csv.csv")
sns.distplot(data['wzrost'], kde = True)