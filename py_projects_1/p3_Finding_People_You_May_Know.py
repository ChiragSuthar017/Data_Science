# Finding _"People You May Know"_

import json
def load_data(filename):
    with open(filename , "r" ) as f:
        return json.load(f)
def finding_people(user_id , data ):
    user_friends = {}
    for user in data['users']:
        user_friends[user['id']] = set(user['friends'])

    if user_id not in user_friends:
        return []

    direct_friends = user_friends[user_id]
    suggestions = {}
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends: 
                # Count mutual friends 
                suggestions[mutual] = suggestions.get(mutual , 0) + 1
    stored_suggestions = sorted(suggestions.items(), key = lambda x : x[1] , reverse=True)
    return [user_id for user_id , mutual_count in stored_suggestions]
# enter user_id
user_id = int(input("eneter user id : "))
# Load the data 
data = load_data("data.json")
# user_id = n
recc = finding_people(user_id , data)
print(recc)