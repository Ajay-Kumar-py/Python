
import json

data = {}
data["AJay"] = {
    "full_name" : "Ajay Kumar",
    "Bikes":["Discover","Yahaha FZ","Aciva 5g"],
    "Home":["tata","Patna","Bangalore"]
}

data["Abhi"] = {
            "full_name":"Abhishek Kumar",
            "interest" : ["pubg","coding","cycling"],
            "food":["briyani","khichdi","Pizza"]
}
print(type(data))

# convert to dict to json

s = json.dumps(data,indent=4)
print((s))
with open("C:\Pandas\json.txt","w") as f:
    f.write(s)

# convert json to dict

with open("C:\Pandas\json.txt","r") as f:
    s=f.read()
    jd = json.loads(s)


for i in jd['AJay']:
    print(i)

with open("C:\Pandas\datasets\\test.json",'r') as f:
    data_j = json.load(f)

print((data_j))
for state in data_j['states']:
    print(state['name'],state['abbreviation'])

