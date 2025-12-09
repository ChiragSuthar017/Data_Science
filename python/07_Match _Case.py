print("Match Case")

print("""case 404 : not found
case 200 : ok performed
case 400 : bed responce """)
def match_case() :
    code = int(input("enter a number : "))
    match code :
        case 404 :
            print("Not Found")
        case 200 :
            print("Ok Performed")
        case 400 :
            print("Bed Responce ")
        case _ :
            print("Not Match")
print(match_case())