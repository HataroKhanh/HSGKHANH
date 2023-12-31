import requests
from bs4 import BeautifulSoup
import os

urlname = "https://www.1sttheworld.com/collections/scottish-tartan-hoodie"
res = requests.get(urlname)

links = []
for i in range(2,136):
    url = f"https://www.1sttheworld.com/collections/scottish-tartan-hoodie?page={i}"
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        divs = soup.find_all('div', class_="row mt16 product-grid")
        for div in divs:
            a_tags = div.find_all('a', href=True)
            for a in a_tags:
                links.append(a['href'])

        for link in links:
            print(link)
    else:
        print("Failed to retrieve the page")
with open("text.txt",'w') as f:
    for i in links:
        f.write(f"{i}\n")
        


        