# Cleaning and Structuring the Data

## make json file and import data

import json
data = {
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
        {"id": 3, "name": "", "friends": [1], "liked_pages": [101, 103]},
        {"id": 4, "name": "Sara", "friends": [2, 2], "liked_pages": [104]},
        {"id": 5, "name": "Amit", "friends": [], "liked_pages": []}
    ],
    "pages": [
        {"id": 101, "name": "Python Developers"},
        {"id": 102, "name": "Data Science Enthusiasts"},
        {"id": 103, "name": "AI & ML Community"},
        {"id": 104, "name": "Web Dev Hub"},
        {"id": 104, "name": "Web Development"}
    ]
}
with open("data2.json" , "w") as file:
   json.dump(data , file)

## clean the data 

import json
def clean_data(data) :
    # Remove user with missing names 
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    
    # Remove duplicate friendes 
    for user in data["users"]:
        user['friends'] = list(set(user['friends']))

    # Remove inactive users
    data["users"] = [user for user in data["users"] if user["friends"] or user['liked_pages']]

    # Remove duplicate pages
    unique_pages = {}
    for page in data["pages"] :
        unique_pages[page['id']] = page
    data['page'] = list(unique_pages.values())
    return data
# Load the data
data = json.load(open("data2.json"))
data = clean_data(data)
json.dump(data, open("cleaned_data2.json" , "w" ), indent=4)
print("data has been cleaned successfully")