import pandas as pd

matrix = [(222, 34, 23),
          (333, 31, 11),
          (444, 16, 21),
          (555, 32, 22),
          (666, 33, 27),
          (777, 35, 11)
          ]

# Create a DataFrame object
dfObj = pd.DataFrame(matrix, columns=list('abc'))
print(dfObj)
#dfObj = dfObj.apply(lambda x:x*10+20)
#print(dfObj)
def multiplyData(x):
    return x*10

#dfObj = dfObj.apply(multiplyData)

dfObj = dfObj['a'].apply(lambda x:x*100)
print(dfObj)

