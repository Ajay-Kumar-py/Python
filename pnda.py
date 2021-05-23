import pandas as pd
import numpy as np

dict1 = {"name":["harry","ajay","mohan","tom"],
         "marks":[44,66,99,88],
         "city":["chennai","tata","patna","punjab"]}

df = pd. DataFrame(dict1)
print(df)
df.to_csv("friends.csv")
df.to_csv("friends_index_false.csv",index=False)
print(df.head(2))
print(df.tail(2))

print(df.describe())

harry = pd.read_csv("harry.csv")
print(harry)
print(harry['speed'][0])
harry['speed'][0]=187
print(harry)
harry.to_csv("harry.csv")
harry.index=["first",'second',"third","forth"]
print(harry)
ser  = pd.Series(np.random.rand(12))
print(ser)
newdf = pd.DataFrame(np.random.rand(334,5),index =np.arange(334))
print(newdf)
print(newdf.head((5)))
print(type(newdf))

print(newdf.sort_index(axis=0,ascending=False))
print(newdf[0])
newdf.loc[0,0]=54
newdf.loc[1,0]=64
print(newdf)
newdf.columns=list("ABCDE")
print(newdf)
newdf.loc[0,'A']=557
print(newdf)

print(newdf.loc[[1,2],:])
print(newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)])
print(newdf.head(5))
print(newdf.iloc[1,4])
print(newdf.head(5))
print(newdf.iloc[[0,1],[1,2]])
print(newdf.head(3))
#print(newdf.drop['A','C'],axis=1)
newdf.loc[:,['B']]=000
print(newdf)
df=pd.DataFrame({"name":['ajay','mohan','sohan'],
                 'toy':[np.nan,'batmobile','bullwhip'],
                 'born':[np.nan,pd.Timestamp("1940-04-25"),np.nan]})
print(df)
print(df.dropna(thresh=1))
