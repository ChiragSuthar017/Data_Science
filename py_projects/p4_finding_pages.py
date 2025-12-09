# Finding "Pages You Might Like"

import json

# load json data
def load_data(filename) :
    with open(filename) as f:
        return json.load(f) 

# Fing pages a user might like based on comman interests 
def find_pages(user_id , data):
    #store user intersctions with pages 
    user_pages = {}

    # populate the dictionary
    for user in data['users'] :
        user_pages[user['id']] = set(user['liked_pages'])

    # if the user is not found, return in empty list
    if user_id not in user_pages:
        return []
    user_liked_pages = user_pages[user_id]
    page_suggestion = {}

    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                page_suggestion[page] = page_suggestion.get(page , 0) + len(shared_pages)
    sorted_pages = sorted(page_suggestion.items(), key=lambda x:x[1] , reverse=True)
    return [page_id for page_id , score in sorted_pages]

# ask user id 
n = int(input("enter user id "))
data = load_data("Messive_data.json")
user_id = n
page_recommendation = find_pages(user_id , data)
print(f"Pages You Might Like for User {user_id}: {page_recommendation}")