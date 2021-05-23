import pandas as pd
dict = {"name":["Ajay","Abhi","nisha","virendra","manju"],
        "marks":[88,88,55,87,99],
        "mark":[88,88,55,87,99],
        "Roll no":[23,45,67,88,34],
        "Grade":["B","B","B","E","E"]}

df = pd.DataFrame(dict)

print(df)

df.to_csv("dataframes.csv")

print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.dtypes)
print(df.sort_index(axis=0,ascending=False))

df.iloc[0,1]=88
print(df)
df.loc[0,1]=430
print(df)
print(df.drop(1,axis=1))
#print(df)
print(df.loc[[1,2],:])
print(df.loc[df['marks']>80])
print(df.drop([1],axis=1))
df_drop =df.drop_duplicates(['Grade','marks'],keep=False)
print(df_drop)
