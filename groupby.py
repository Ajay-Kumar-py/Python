
import pandas as pd
import re
import matplotlib.pyplot as plt

df =  pd.read_csv("D:\\Rnd Server\\testdata.csv")
print(df)
print(df['city'])
print(df.loc[1,'event'])
print("rained places",df.loc[df['event']=='rain'])
df['total']= df['temprature']  +  df['windspeed']
print(df)
cols = list(df.columns)
df = df[cols[0:2] + [cols[-1]] + cols[2:5]]
print(df)
print("show the sunny day inn newyorkk",df.loc[(df['city']=='new york') & (df['event']=='sunny')])

print("cloudy coyntries in paris whose temp is >20  : ",df.loc[(df['event'] == "cloudy") & (df['city']== "paris") & (df['temprature']>20)])

print("give the all etails which contain york",df.loc[df['city'].str.contains('york')])
#cf = df.loc[df['event'].str.contains('un[a-z]*  ',regex =True)]
#print(cf)
#df.replace(to_replace="cloudy",value = "ajay",inplace=True)
#print(df)
#df.drop("total",axis=1,inplace=True)
cf = df.loc[df['event']=="cloudy",'event']= 'abhi'
print("cf\\\\\\\\\\\\\\\\",cf)
df.reset_index(inplace=True)
print("---------------------------")
for index,row in df.iterrows():
    print(index,row)
print("---------------------------")
ff= df.rename(index = {0:'a'},columns = {"city":"country"})
#ff.set_index('index',inplace=True)
#print(ff.loc[1,"country"])
ff.drop("index",axis=1,inplace=True)
print(ff)
ff.to_csv("testdata.csv")
gf = ff.fillna({'temprature':0,
               "windspeed":0,
               'event':"not available",
                'total':0})
print(ff.groupby(['country','event']).sum())
#print("mum",ff.get_group(('mumbai','fog')))
#print(hf)

gf.to_csv("testdata.csv")