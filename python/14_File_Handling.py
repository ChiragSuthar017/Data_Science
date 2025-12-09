# File Handling

# print("Read txt file ")

# a=open("txt.txt","r")
# a.read()
# a.close()

print("Create and Write in txt file ")

b="chirag suthar"
c = open("chirag.txt","w")
c.write(b)
c=open("chirag.txt","r")
c.read()
c.close()

print("append")

d=open("chirag.txt","a")
d.write("\nthis is new line")
d.close()

d=open("chirag.txt","r")
d.read()

print("Open file using 'with' statement")

with open ("chirag.txt","r") as file:
    e = file.read()
    print(e)

print("Check file is exist ")

import os
if os.path.exists("chirag.txt"):
    print("file is exist")
else:
    print("file does not exist")

print("Delete file ")

import os 
if os.path.exists("txt.txt"):
    os.remove("txt.txt")
    print("file deleted")
else:
    print("file does not exist")