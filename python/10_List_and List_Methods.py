print("List")

l = [1,2,3,4,5,10]
print(l)
print(type(l))

print("List Methods")

a = [1,1,2,3,4,5,10]
b = [6,8]
c = [11,12,13]
a.append(7) # add number
print(a)
a.extend(b) # add n in a
print(a)
num=a.pop(2)
print(a)
print(num)
a.insert(3,2)
print(a)
print(a.index(2))
print(a.count(1))
a.sort()
print(a)
print(a+c) # add two list and return new list
print(a)
print(c)
# check element in list 
# first method
if 2 in a:
    print("yes. 2 in a ")
# second method
print(2 in a)
d = "chirag-suthar-bca-gls"
print(d.split("-")) # split string to list