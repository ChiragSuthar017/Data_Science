print("Set")

# Create empty set 
a = set()
print(a)
print(type(a))

b = {1,2,3,4,4,5,6}
print(b)
print(type(b))

print("Set Methods")

c=set([1,2,3,4,5])
print(c)

c.add(6) # add only one number
print(c)

c.update([7,8,9]) # add multiple number
print(c)

c.remove(10) # give error if 10 is not found in set
print(c)

c.discard(10) # does not give any error if not found
print(c)
c.discard(9)
print(c)

d={1,2,3,4,5}
e={4,5,6,7,8,9}
print(d.union(e)) # union = add both sets and give new set

print(d.intersection(e))

f={1,2,3,4,5}
g={4,5}
print(g.issubset(f))

print(f.issuperset(g))

print(f.difference(g))