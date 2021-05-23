people = {1:{"name":"john","Age":24,"sex":"male"},
           2:{"name":"abhi","age":45,"sex" :"male"} }

print(people)

print(people[1]["name"])
n={"name":"ajay","age":21,"sex":"male"}
for pid,p_info in people.items():
    print(pid)
    for key in p_info:
        print(key ,  ':', p_info[key])


for key in n:
    print(key,":",n[key])
