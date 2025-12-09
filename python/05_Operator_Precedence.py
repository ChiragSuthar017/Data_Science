print(" Operator Precedence")

# parantheses() :- operations inside parantheses are evalute first
# for example :-
#  2+2*(4-2)
#  2+2*(2)
#  2+4
#  6

result = 2+2*(4-2) 
print(result)

# exponents ** :- after parantheses() evalute exponents on Right-to-left exponentiation 
# for example :-
#  3**2**2 
#  solve right to left 2*2 = 4
#  3**4 = 3*3*3*3 = 81
#  so 3**2**2 = 81

a = 3 ** 2 ** 2
print(a)

# after exponents ** solve firstly Multiplication *, division/ , floor division// , modulus% . evalute form left-to-right
# for example :-
#  10 + 2 * 2 
#  10 + 4
#  14

b = 10 + 2 * 2 
print(b)

# after Multiplication *, division/ , floor division// ,
#  modulus% ecvalute Addition+ , subtraction- . from left-to-right

c = 10 + 2
print(c)