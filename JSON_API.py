import requests
import json
import time
r = requests.get("https://formulae.brew.sh/api/formula.json")
packages_json = r.json()

print(len(packages_json))
result = []
data = {}
for package in packages_json:


    packages_name = package['name']
    packages_desc = package['desc']

    packages_url = f'https://formulae.brew.sh/api/formula/{packages_name}.json'

    r = requests.get(packages_url)
    package_json = r.json()

    package_str = json.dumps(package_json,indent = 2)


    install_30 = package_json['analytics']["install_on_request"]['30d'][packages_name]
    install_60 = package_json['analytics']["install_on_request"]['90d'][packages_name]
    install_365 = package_json['analytics']["install_on_request"]['365d'][packages_name]
    #https://formulae.brew.sh/api/formula/a2ps.json



    data = {
        'name' :packages_desc,
        'desc' : packages_desc,
        'analytics' : {
            '30d' : install_30,
            '90d' : install_60,
            '365d' : install_365
        }
    }

    result.append(data)
    time.sleep(r.elapsed.total_seconds())

    #print(packages_name, packages_desc, install_30, install_60, install_365)

#print(result)

with open('json_json.json','w') as f:
    json.dump(result,f,indent=2)