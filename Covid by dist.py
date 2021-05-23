
import json
import requests
api_address = "https://api.covid19india.org/state_district_wise.json"

covid = requests.get(api_address).json()
st = str(input("Enter state"))
n = str(input("Enter dist"))

for i in covid:
    #print(i)
    if i == st:
        print(st,n)
        print(covid[st]["districtData"][n])
        print(covid[st]["districtData"][n]['delta'])









