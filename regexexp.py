import re

txt = "I have complted my diploma in abhi23@gmail.com electronics 2014, i came to ajay.23432@gmail.com bangalore 2011, my brother came to bangalore 2016"

pattern1 = re.compile("[1-9]\d\d\d")
result1 = pattern1.findall((txt))
print(result1)
pattern = re.compile("[^aeiou]")

print(" ".join(pattern.findall(txt)))

pattern2 = re.compile("[^\w\s]")
result2 = pattern2.findall(txt)
print(result2)

txt1 = """What is your name
Who is that guy"""
pattern3 = re.compile("(What|Who) is")
result3 = pattern3.findall(txt1)
print(result3)

txt2 = """I have two dogs, one dog is older than other, one dogS id very cute"""
pattern4 = re.compile("dogs?")
result4 = pattern4.findall(txt2)
print("find me : ",result4)

txt3 = """file1.txt
file_one.txt
file.txt
file09.txt
fil.txt
file.xml
"""
pattern5 = re.compile("file\d+\.txt")
result5 =pattern5.findall(txt3)
print(result5)

txt4 = """555-555-5555 
555 555 5555 
5555555555"""
pattern6 = re.sub("\d{3}[\s-]?\d{3}[\s-]?\d{4}")
result6 = pattern6.findall(txt4)
print(result6)