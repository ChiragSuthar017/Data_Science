print("For Loop")

l = [3,4,5,6,7,8,9]
print(l)
for item in l :
    print(item)

print("\n")
print("For loop in range ")

for i in range (1 , 10):
    print(i)

print("\n")
print("make table using for loop ")

a = int(input("enter number : "))
for b in range(1,11):
    print(f"{a} X {b} = {a*b}")

print("\n")

print("While Loop")

a = 0 
while a<11:
    print(a)
    a = a+1

print("\n")
print("Loop Control Statements")

# Pass :- Does nothing (used as a placeholder)
# for example :-
# for item in l :
#     pass
# print("hello")
# # for loop does not execute   

for item in l :
    pass
print("hello")

# Break :- exit the loop
# for example :- 
# l = ["apple","bananas","tomatoes"]
# for item in l :
#     if (item == "bananas"):
#         break
#     print(item)
# # print apple because we use break statement in bananas 

l = ["apple","bananas","tomatoes"]
for item in l :
    if (item == "bananas"):
        break
    print(item)

# Continue :- skip and return next iteration
# for example :-
# l = ["apple","bananas","tomatoes"]
# for item in l :
#     if (item == "bananas"):
#         continue
#     print(item)
# # skip the banans because we use continue in bananas

l = ["apple","bananas","tomatoes"]
for item in l :
    if (item == "bananas"):
        continue
    print(item)