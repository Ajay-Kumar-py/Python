import zipfile
import time
import os
import sys




path_c = input("ENTER FILE PATH : ")
name = input("ENTER FILE NAME WITH (.ZIP) : ")
result = []
for root,dir,files in os.walk(path_c):
    if name in files:

        result.append(os.path.join(root ,name))

with zipfile.ZipFile(result[0], 'r') as zip_ref:
    zip_ref.extractall(path_c)
time.sleep(2)
print("!! SUCCESS !!")
input("!! PRESS ENTER TO EXIT !!")

#D:\travello
#travello.zip

