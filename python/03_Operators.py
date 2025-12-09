# Operators

print("Arithmatic Operators")

a = 10
b = 5
print(a+b) #Additon
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a/b) #Division
print(a//b) #Floor Division
print(a%b) #Modulus
print(a**b) #Exponention for example a = 2 , b = 3 so a**b is 2*2*2 = 8


print("Comparison Operators")

a==b # equal to == 
a!=b # not equal !=
a>b # greater then >
a<b # less then <
a>=b # greater equal then >=
a<=b # less then <=

print("Logical Operators")

x = True
y = False

x and y 
x or y 
not x
not y

print("Bitwise Operators")

a = 5
b = 3

a & b #And bitwise operator 
a | b #Or bitwise operators 

print("Assignment Operators")

a = 5 # a is 5
print(a)
a += 5 # a = 5+5 because a is 5 
print(a)
b = 5
b -= 5 # b = 5-5 because b is 5 
print(b)
c = 5
c *= 5 # c = 5*5 because c is 5  
print(c)
d = 5
d /= 5 # d = 5/5 because d is 5  
print(d)
e = 5
e //= 5 # e = 5//5 because e is 5  
print(e)
f = 5
f %= 5 # f = 5%5 because f is 5  
print(f)
g = 5
g **= 5 # g = 5**5 because g is 5  
print(g)

print("Memebership and Identity operators")

a = 42
lst = [1,2,3,4]
print(lst)
z = 2
print(z in lst) # for check z avalable in lst
print(z not in lst) # for check z not avalable in lst
print(a is lst )# for check a is same oblect
print(a is not lst) # for check a is differnt object