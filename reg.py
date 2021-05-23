import re

result = re.findall(r'\w',"AV is largest analyst community in India")
print(result)

result = re.findall(r'\w*','AV is largest analystics community in india')
print(result)
result = re.findall(r'\w+',"AV is largest analyst community of india")
print((result))
result = re.findall(r'^\w+',"AV is largest analytics of india")
print(result)
result = re.findall(r'\w$',"AV is largest analytics of india")
print(result)
##Return first two char of the each word

result = re.findall(r'\w\w','AV is largest analystics community in india')
print(result)
result=re.findall(r'\b\w\w','AV is largest analystics community in india')
print(result)

## Return the domain type of given email-ids
result = re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)
result = re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)
result = re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print(result)

result = re.findall(r'\d{2}-\d{2}-(\d{4})',"Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009")
print(result)

print("\\\\\\\\\\\Return all words of a string those starts with vowel\\")

result = re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print(result)
result=re.findall(r'\b[^aeiouAEIOU]\w+','Av is largest Analytics community of India')
print(result)


li=['9999999999','999999-999','99999x9999']
for val in li:
 if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
     print('yes')
 else:
     print('no')