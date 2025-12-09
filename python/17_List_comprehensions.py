print("List comprehensions")

# create table
table=[]
a= int(input("enter number : "))
for i in range (1,11):
    table.append(a*i)
print(table)

# in one Line
b = [4*i for i in range(1,11)]
print(b)

# with if 
c = [2*i for i in range(1,11) if (i%2==0)]
print(c)

d = {f:f**2 for f in range(1,5)}
print(d)

numbers = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(numbers)  # Output: ['Even', 'Odd', 'Even', 'Odd', 'Even']

pairs = [(x, y) for x in range(2) for y in range(3)]
print(pairs)  # Output: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

unique_numbers = {x for x in [1, 2, 2, 3, 4, 4]}
print(unique_numbers)  # Output: {1, 2, 3, 4}

