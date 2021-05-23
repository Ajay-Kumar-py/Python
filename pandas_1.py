
import pandas as pd
import pathlib as Path


try:

    df = pd.read_csv("C:\\my-doc\\Datasets\\1000 Sales Records.csv")

except FileNotFoundError:
    print("No file")
else:
 
##print(df)
##print(df.head(2))
##print(df['Units Sold'].max())

##print(df[['Sales Channel','Units Sold']])
##print(df.loc['Region']['Item Type'== 'Clothes'])
    df_region = df.loc[df['Item Type']=="Clothes"]
    ##print(df_region)
    df_region = df.loc[df['Sales Channel']=='Online']

    df_region.to_csv("total.csv")
    #dk= df_region.to_csv("total.txt",sep='*')
    ##print("txt file",dk)


  #  df_offline = df_region.loc[df['Sales Channel']=="Offline"]

 #   df_sum = df.groupby(['Region', 'Country','Item Type','Sales Channel'])['Total Revenue'].sum().reset_index()

#df_sum.to_csv("total.csv",index=None)

    ##print(df['Region'],['Country'])
    #print(df.loc[:'Country'])
    #print(df['Country'])
    #print(df)
    #print(df.loc[[8,9],["Region","Order ID","Ship Date"]])
    ##print(df.iloc[0:3])
    ##print(df.iloc[2,1])
    df_unitsell = df.loc[(df['Units Sold']>5000) & (df["Sales Channel"]=='Offline')]
    df_unitsell.to_csv("unitsell.csv")

    df.loc[13,'Units Sold']=2000
    df.to_csv('total.csv')
    df_china = df.loc[df['Region']== 'Asia']
    df_china = df_china.loc[df_china['Sales Channel'] == 'Online']
    df_china = df_china.loc[df_china["Country"] == 'China']
    df_china.to_csv('Asischaina.csv')
    k = df_china['Total Profit'].sum()
    df_china.loc[5,'Total Cost'] = "To00tal"
    df_china.loc[5,'Total Profit'] = k
    #print(df_china)
    df_china.to_csv('Asischaina.csv')
    #print(df['Region'][df['Units Sold'] == 5100])
    #print(df_china.shape)
    #print("slicing")
    #print(df_china[1:3])
    #print(df_china['Region'])
    #print(df[df["Units Sold"]>5000])
    #print(df["Country"][df["Item Type"]== "Fruits"])
    #print(df.index)
    #print(df.set_index("Region"))
    #print(df)
    df6 = pd.DataFrame([["ajay",21,88,89],['abhi',32,56,77],['nisha',77,67,88],["ajay",21,88,89],['nisha',77,67,88]])
    df6.columns = ['name','marks','rollno','age']
    #df5 = pd.read_csv("example.csv",header = None,names=["name","rollno","maths","marks"])
    #print("df6",df6)
    df6.to_csv("example.csv")
   # df5 = pd.read_csv("example.csv",na_values= {'kuchbhi':["n.a.","not available",55],
                                               # "Country" :["n.a.","not available"] })

    ##print(df5)
   # df6.drop(["marks",'sub'],axis = 1)
    df6['duplicates']= df6.duplicated(['name','marks','rollno','age'])
    print(("df6",df6))
    print("------------------")
    df7 = df6.loc[df6['duplicates']==True]
    print(df6.duplicated(["name"]))
    print("-------------------")
    print((df7))

    df9= df6.drop_duplicates(["name"],keep = "last",inplace=True)
    #df6.reset_index(level = 2, inplace = True, col_level = 1)
    #df9 = df8.reset_index()
    #df9 = df6.drop(["duplicates"],axis =1)
    #df9.drop
    #print(df9)



