import pandas as pd

df1 = pd.read_csv("example.csv")
df2 = pd.read_excel("student.xlsx")
df3 = pd.concat(([df1,df2]))
print(df3)