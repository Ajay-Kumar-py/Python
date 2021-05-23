s = {"ajay","abhi","sam","max","foo","baz"}
s1 = {"soi","dff","dd","sam","max","foo"}
print("sym diff",s.symmetric_difference(s1))

for i in s:
    print(i)
s.add("nisha")
print(s)
s.discard("ajay")
print(s)

print(s.intersection(s1))

print(s.union(s1))
print(s.difference(s1))

g1 = {1,2,3,4}
g2 = {2,3,5,6}

print(g1.symmetric_difference(g2))
print(g1.issubset(g2))

g1.update([8,9])
print(g1)


