import requests
from bs4 import BeautifulSoup

# Data storage
data = {"Name": [], "img": []}

# Using a session for requests
with requests.Session() as session:
    # Open the file with URLs
    with open("C:\\Users\\hungbui\\Desktop\\KhanhProject\\HSGKHANH\\Crawdata\\text.txt", "r") as file:
        for line in file:
            url = line.strip()
            full_url = f"https://www.1sttheworld.com{url}"
            print(url)
            
            try:
                # Make a request
                res = session.get(full_url)

                if res.status_code == 200:
                    soup = BeautifulSoup(res.content, "html.parser")
                    name = soup.find('h1', class_="h4 d-block product__name mt0 mb12 product__name-product").text
                    if name:
                        data["Name"].append(name)
                        # Add code here to extract image URL or data
                    else:
                        print("Name not found")
                else:
                    print(f"Error accessing {full_url}")

            except Exception as e:
                print(f"An error occurred: {e}")

# You can then process 'data' as needed
