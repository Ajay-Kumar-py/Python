

import matplotlib.pyplot as plt
from collections import Counter
import re
# x-axis values
#f = open("C:\\my-doc\\python files\\iso_8859-1.txt","r")
dict = {}
with open("C:\\my-doc\\python files\\iso_8859-1.txt") as lines:
    for line in lines:
        word = line.split()
        # for i in word:
        #     # dict[i] = dict.get(i,0)+1
        #     # print(i)
        #print(line)
        s= re.finditer(r'[A-Z]\s+[A-Z0-9]\s+\w+\s\w+\s[A-Za-z] \w+\sDIAERESIS$',line)
        for match in s:
            print(match)
#print(dict)