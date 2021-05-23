import pandas as pd

df1 = pd.DataFrame({
                    "city":["mumbai","delhi","bangalore","goa"],
                    "temprature":[46,49,34,29],
                    "humdity":[21,24,67,31]
})


df2 = pd.DataFrame({
                    "city":["delhi","mumbai","bangalore","pune"],
                    "temprature":[46,48,67,49],
                    "humidity":[23,43,29,39]
})

print(df1)
print(df2)
df3=pd.concat([df1,df2],keys=['india',"us"])
print(df3)

df4 = pd.merge(df1,df2,on='city',how="outer",indicator=True)
print("merging",df4)

df5 = pd.read_csv("weather_Data.csv")
print(df5)

print(df5.pivot_table(index="city",columns="day",margins =True))