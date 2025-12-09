print("If else Conditionals")

a = int(input("write a number : "))
print(f"your number is {a}")

if (a==50) :
    print("a is greater equal 50 ")
elif (a>=100) : 
    print("a is greater then 100 ")
else :
    print("a is smaller then 50 ")

print("\n")
print("Functions")

# find average using finction
def avg(a , b=10) :
    return(a+b)/2
avg(4)
print(avg(4))
