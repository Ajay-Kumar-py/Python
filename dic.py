dict ={"name":["ajay","vinod"],
       "age":[12,15],
       "ID":[2,3],
       #"sex":["male","male"]
       }
t={}
for j in range(3):
    s= input("Enter name : ")
    a=int(input("enter age"))
    d=int(input("Enter IDS"))
    d1 = (input("Enter sex"))
    t.setdefault("name",[]).append(s,"pop")
    t.setdefault("age",[]).append(a)
    t.setdefault("ID",[]).append(d)
    t.setdefault("sex", []).append(d)
print("new dic",t)

for key in dict:
    if key in t:
        dict[key] = dict[key]+t[key]




print("my new dict :",dict)
