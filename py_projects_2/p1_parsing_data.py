# Parsing text file data in python 

with open(r"D:\Data_Science\py_projects_2\big_data.txt",encoding="utf-8") as f:
    data = f.read()
# print(data)

chunks = data.split("\n\n")
# print(chunks[0])

chunks = [c for c in chunks if len(c)>3]
# print(chunks)

def parse_chunks(chunk):
    chunk = chunk.strip()
    lines = chunk.split("\n")
    username = lines[0]
    posts = int(lines[1].split(" post")[0].replace(",", ""))
    followers = float(lines[2].split(" follower")[0].replace(",","").replace("K","").replace("M",""))
    if ("K" in lines[2]):
        followers = int(followers * 1000)
    elif ("M" in lines[2]):
        followers = int(followers * 1000000)
    else:
        followers = int(followers)  
    following = float(lines[3].split(" following")[0].replace(",","").replace("K","").replace("M",""))
    if ("K" in lines[3]):
        following = int(following * 1000)
    elif ("M" in lines[3]):
        following = int(following * 1000000)
    else:
        following = int(following)  
    name = lines[4]
    if (len(lines) > 5):
        type_of_page = lines[5]
        bio = lines[6:]
    else :
        type_of_page = "unknown"
        bio = "NaN"
    return {"username" : username , "posts" : posts, "followers" : followers , "following" : following , "name" : name , "type_of_page" : type_of_page , "bio" : bio}

# print(parse_chunks(chunks[0]))


all_chunks = []
for chunk in chunks :
    parse_chunk = parse_chunks(chunk)
    all_chunks.append(parse_chunk)
# print(all_chunks)

import json
s = json.dumps(all_chunks, indent=4)
a = open("big_data.json","w")
a.write(s)
# print(s)


print("\n -: username who have max post :-\n")
max_post = 0
for chunk in all_chunks:
    if(max_post<chunk['posts']):
        max_post = chunk['posts']
        details_with_max_posts = chunk
print(details_with_max_posts['username'])

print("\n -: username who have max followers :-\n")

max_followers = 0
for chunk in all_chunks:
    if(max_followers<chunk['followers']):
        max_followers  = chunk['followers']
        details_with_followers = chunk
print(details_with_followers['username'])

print("\n -: username who have max following :- \n")

max_following = 0
for chunk in all_chunks:
    if(max_following<chunk['following']):
        max_following = chunk['following']
        details_with_following = chunk
print(details_with_following['username'])

print("\n")

categories = set()
for chunk in all_chunks:
    categories.add(chunk['type_of_page'])
print("/n number of total categories : ",len(categories))