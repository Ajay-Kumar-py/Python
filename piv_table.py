
import pandas as pd

df = pd.read_csv("pivt_table.csv")
print(df)
print("------------------")
df1 =df.pivot(index="date",columns="city")
print(df1)

df2 = pd.read_csv('pivt2.csv')
print("-----df2----",df2)
df3 =df2.pivot_table(index='city',columns='date',aggfunc='sum',margins=True)
print(df3)
print("--------------")
df4 = pd.read_csv('pivt1.csv')
print("--------df4------grpr--",df4)
df4['date']=pd.to_datetime(df['date'])
print(df4)
df5 = df4.pivot_table(index=pd.Grouper(freq='B',key='date'),columns='city')
print(df5)