import pandas as pd

df = pd.read_csv("C:\\Users\\abhishek\\PycharmProjects\\ajay\\example.csv")
print("My data",df)

df['duplicates'] = df.duplicated(["name","marks","roll no","age"])
print("df1",df)
df3 = df.loc[df['duplicates']==True]
print("df3",df3)

df.drop_duplicates(keep='first')



