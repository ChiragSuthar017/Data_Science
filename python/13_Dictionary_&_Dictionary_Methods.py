print("Dictionary ")

# make empty dictionary
a = {}
print(a)
print(type(a))

b = {
    "name" : "chirag",
    "age" : 19,
    "course" : "bca"
}
print(b)

print(b["name"])

print("Dictionary Methods")

c = {
    "name" : "chirag",
    "age" : 19,
    "course" : "bca"
}
x = c.get("name")  # this method does not give any error
y = c.get("village")
print(x) 
print(y)

c["age"] = 20
print(c)

print(c.keys())

print(c.values())

print(c.items())

c.update({"age" : 19})
c.update({"last name" : "suthar"})
print(c)

print(c.pop("last name"))

print(c.popitem())

d = c.copy()
print(d)

d.clear()
print(d)

print("Dictionary Comprehension")

# create square using dictionary
square = {x**2 for x in range(1 , 6)}
print(square)

# odd number
f = {v for v in range (1 , 100) if (v % 2 == 0)}
print(f)