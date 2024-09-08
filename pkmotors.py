import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

# Yahan per hum ab bases URL website ka get krnge to scrape

pk_motors_url = 'https://www.pkmotors.com/used/car/suzuki/alto/2024/karachi'
respone = requests.get(pk_motors_url)

#Ye line HTML response ko parse kregi beautifulSoup use kr kay
soup = BeautifulSoup(respone.text, "html.parser")

# Select krega main container
main = soup.select("div.itemdetail")
create_list = []
# Ye function year, make , model or city ko extract krega title sy
def extract_data_title(title):
    words = title.split()
    if len(words) >= 6:
        year = words[0]
        make =words[1]
        model = words[2]
        city = words[-1]
        return year, make, model, city
    return None, None, None, None

# Ye function cars ki listing to iterate krega
for cars in main:
    title = cars.select_one("h1").text
    print(title)

    price = cars.select_one("div.itemprice").text
    print(price)

    # Yahan hum title sy finally data get krenge
    year, make, model, city = extract_data_title(title)
    print(f"Year: {year}, Make: {make}, Model: {model} City: {city}, price: {price}")

    # Jo data uper extract kia h usy hum list me append kr denge
    new_appended_data = {"year": year, "make": make, "model": model, "city": city, "price": price}
    create_list.append(new_appended_data)

# data ko dataFrame me convert krega
df = pd.DataFrame(create_list)
print(df)

# ye method data to new file me json form me save krega
df.to_json("Json_data_file.json", orient="records", indent=3)



