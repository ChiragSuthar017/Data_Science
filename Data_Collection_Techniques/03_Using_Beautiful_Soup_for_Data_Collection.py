from bs4 import BeautifulSoup
import pandas as pd

with open(r"D:\Data_Science\Data_Collection_Techniques\htmls/page1.html") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
h3s = soup.find_all("h3")
# print(h3s)
articles = soup.select("article.product_pod") 
items = []
for article in articles:
    title = article.find("h3").find("a")['title']
    price = article.select_one("p.price_color").text.split("Ã‚Â")[1]
    rating_element = article.select_one("p.star-rating")
    rating = rating_element['class'][1]
    items.append([title, price, rating])

df = pd.DataFrame(items, columns=['books name', 'price', 'rating'])
print(df)

df.to_csv("data.csv",index=False) 