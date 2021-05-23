import pandas as pd


df1 = pd.DataFrame({'city': ['mumbai','pune','goa','patna'],
        'temp':[44,65,36,54],
         'pop':[21,32,43,34]           })


df2 = pd.DataFrame({'city': ['mumbai','pune','goa','pujab'],
        'humidity':[24,35,54,86],
                    'pop': [21, 32, 43, 34]  })


df3 = pd.merge(df1,df2,on='city')

df4 = pd.concat([df1,df2],keys=['X','Y'],ignore_index=False,axis=0,sort=True)
#print("conate",df4)
print(df3)
print("-------------------------")
print("Concat of dataframe : ")
print(df4)