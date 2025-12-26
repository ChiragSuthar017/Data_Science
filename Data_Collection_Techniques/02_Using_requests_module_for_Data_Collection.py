import requests

# a = requests.get("https://books.toscrape.com/")
# print(a.text)
# print(a.status_code)

for i in range(1 , 51):
    a = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    with open(f"htmls/page{i}.html","w", encoding="utf-8") as f:
        f.write(a.text)
        print(f"page {i} download successfully")