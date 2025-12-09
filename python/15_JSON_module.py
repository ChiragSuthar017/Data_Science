# JSON Module

print("Dumps and loads JSON file")

import json
a = {"name" : "chirag" , "age" : 19 , "city" : "banswara" }
b = json.dumps(a)
print(b)
print(type(b))

c = json.loads('{"name" : "chirag" , "age" : 19 , "city" : "banswara" }')
print(c)
print(type(c))

print("Create and dump or load json file")

# create and write json file 
import json
d = {"name" : "chirag" , "age" : 19 , "city" : "banswara" }
with open ("data.json","w")as file :
    json.dump(d,file)

    # read json file
with open ("data.json","r")as file :
    e = json.load(file)
    print(e)

print("if more then two main argument")

d = {"name": "chirag", "age": 19, "city": "banswara"}
f = {"sname": "suthar"}
g = {"lol ": "lol"}
merged = {**d, **f, **g}
with open("data.json", "w") as file:
    json.dump(merged, file)

# read json file
with open ("data.json","r")as file :
    l=json.load(file)
    print(l)