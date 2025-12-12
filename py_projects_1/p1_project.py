# Make json file using python

import json
data = {
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
        {"id": 3, "name": "Rahul", "friends": [1], "liked_pages": [101, 103]},
        {"id": 4, "name": "Sara", "friends": [2], "liked_pages": [104]}
    ],
    "pages": [
        {"id": 101, "name": "Python Developers"},
        {"id": 102, "name": "Data Science Enthusiasts"},
        {"id": 103, "name": "AI & ML Community"},
        {"id": 104, "name": "Web Dev Hub"}
    ]
}
with open("data.json" , "w" ) as file :
    json.dump(data, file)

# Import json file in python

import json 
def load_data(filename):
    with open (filename , "r") as f:
        data = json.load(f)
    return data
    data = load.data("data.json")

print(data)
print(type(data))

# Write a function to display user and their connections

def display_users(data):
    print("User and their connections\n")
    id_to_name = {user['id'] : user['name'] for user in data['users'] }
    for user in data['users']:
        friend_name = [id_to_name[fid] for fid in user['friends']]
        print(f"ID c{user['id']}. {user['name']} is a friend with : {friend_name} and like page are {user['liked_pages']}")
    print("\n page informatioin")
    for page in data['pages']:
        print(f"{page['id']} : {page['name']}")
display_users(data)