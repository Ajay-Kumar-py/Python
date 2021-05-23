


import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

matches= pd.read_csv("C:\\my-doc\\Datasets\\matches.csv")
print(matches.columns)
print(matches.head(5))
print(matches[["dl_applied","win_by_runs","city"]])
#print(matches.columns)
print(matches.shape)

print("________Analysis_______\n")
print("Total Matches in Dataset : ",matches['id'].count())
print("Total seasons : ",len(matches['season'].unique()))

print("Team and max run : ",matches.loc[matches['win_by_runs'].idxmax(),["winner","win_by_runs"]])
print(matches['win_by_runs'].idxmax())
#
# print("Won by maximum wickets",matches.loc[matches["win_by_wickets"].idxmax()][["winner","win_by_wickets"]])
# print(matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()])
#
# print(matches.loc[matches[matches["win_by_wickets"].ge(1)].win_by_wickets.idxmin()])



ss=matches["toss_winner"]==matches["winner"]
print(ss.value_counts())

df = matches[matches["winner"]=="Sunrisers Hyderabad"]["player_of_match"].value_counts()
print(df.head(5))

print(matches[(matches['season']==2017) & (matches['venue']=="M Chinnaswamy Stadium")][['winner',"win_by_runs"]].max())
print("________________________________________")
print(matches[(matches["city"]=="Bangalore") & (matches["winner"]=="Kolkata Knight Riders")]['winner'].value_counts())

print("no of na ",matches.isnull().sum())
print("good team",matches.loc[matches['winner'].value_counts().max()]["winner"])
matches.drop("umpire3",axis=1,inplace=True)
print(matches.head(5))

matches.fillna({
                "city":"Not available",


},inplace=True)



g = matches.groupby("team1")
print(g.win_by_runs.sum())

matches.replace("Rising Pune Supergiant",'Rising Pune Supergiants',inplace=True)
print(matches['team1'].value_counts())
print("______________")
print(matches.columns)
print(matches[matches["toss_decision"]=="bat"]["toss_winner"].count())

#print((matches['toss_decision'].value_counts()/matches['toss_decision'].count())*100)
print(matches['toss_decision'].value_counts())
print(matches.columns)
g = matches.groupby(["city"])
print("wii",g.winner.value_counts())
print(matches["dl_applied"].isnull().value_counts())

avg = matches["dl_applied"].mean()
print(matches["dl_applied"])
matches['dl_applied'] = matches['dl_applied'].apply(lambda x: x + 5)
#matches.replace({
 #                  "dl_applied":{0:avg}
#},inplace=True)
print(matches["dl_applied"])

print("How many times RCB won in Bangalore : ",matches[(matches["city"] == "Bangalore") & (matches["winner"]== "Royal Challengers Bangalore")]["winner"].count())
print(matches[(matches["team2"] =="Royal Challengers Bangalore") & (matches["toss_winner"] =="Royal Challengers Bangalore")]["team1"])
print(matches[matches["result"]=="tie"]["city"])
print(matches[matches["player_of_match"] ==  "Yuvraj Singh"]["venue"])
print(matches["result"].value_counts())


#print("Won by maximum wickets",matches.loc[matches["win_by_wickets"].idxmax()][["winner","win_by_wickets"]])
#print(matches.iloc[matches[matches['win_by_runs'].ge(1)].win_by_runs.idxmin()])

print("Analysis\n",matches.loc[matches[matches["win_by_wickets"].ge(1)].win_by_wickets.idxmin()])

print(matches.loc[matches["win_by_wickets"].idxmax(),["win_by_wickets"]])
