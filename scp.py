import pandas
from bs4 import BeautifulSoup
import requests
import time
import re

base_url = 'https://www.pakwheels.com/used-cars/search/-/mk_suzuki/mk_daihatsu/yr_2000_2024/ct_islamabad/ct_karachi/md_alto/md_mira/'
response = requests.get(base_url)


soup = BeautifulSoup(response.text, "html.parser")

main = soup.select("div.col-md-9.grid-style")
print(main)

data = []
year_pattern = r"\b(20[0-1][0-9]|202[0-4])\b"
data["year"] = []
data["make"] = []
data["model"] = []

def find_year(title):
    match = re.search(year_pattern, title)
    if match:
        return match.group() 
    else:
        return None 

def extract_make_model(title):
    words = title.split()
    if len(words) >= 2:
        make = words[0].capitalize()  
        model = words[1].capitalize()
        return make, model
    return None, None

for mains in main:
 
        titles = mains.select_one("a.car-name.ad-detail-path").text
        print(titles)    

        year = find_year(titles)
        print(year)

        make, model = extract_make_model(titles)

        prices = mains.select_one("div.price-details.generic-dark-grey").text
        print(prices)

        cities = mains.select_one("ul.list-unstyled.search-vehicle-info.fs13").text
        print(cities)

        temp_dict = {"title":titles.replace('\n', ''.strip()), "price":prices.replace('\n', '').strip(), "city":cities.replace('\n', ''.strip()), "year": year, "make": make, "model": model}
        data.append(temp_dict)
print(data)

df = pandas.DataFrame.from_dict(data)
print(df)

df.to_json("data.json", orient="records", indent=3)

