
import pandas as pd

from pandas_profiling import ProfileReport

df = pd.read_csv("https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv")
print(df.head())

profile = ProfileReport(df)

profile.to_file(output_file="housing.html")
