import json
import pandas as pd

with open('data.json', 'r') as c1:
    first_data_1 = json.load(c1)
print(first_data_1)

with open('Json_data_file.json', 'r') as c2:
    second_data_2 = json.load(c2)
print(second_data_2)

def String_Normal_data(value):
    if value is None:
        return ''
    return value.strip().lower()

def mtch_cars(first_data_1, second_data_2):
    matching_data = []
    
    for my_car_1 in first_data_1:
        for my_car_2 in second_data_2:
            if (
                String_Normal_data(my_car_1.get("city")) == String_Normal_data(my_car_2.get("city")) and
                String_Normal_data(my_car_1.get("make")) == String_Normal_data(my_car_2.get("make")) and
                String_Normal_data(my_car_1.get("model")) == String_Normal_data(my_car_2.get("model")) and
                String_Normal_data(my_car_1.get("year")) == String_Normal_data(my_car_2.get("year"))
            ):
                matching_data.append({
                    "city": my_car_1.get("city"),
                    "year": my_car_1.get("year"),
                    "make": my_car_1.get("make"),
                    "model": my_car_1.get("model"),
                    "Pakwheels_Price": my_car_1.get("price"),
                    "PKMotors_Price": my_car_2.get("price")
                })
    return matching_data  

Usama_scrapped_data = mtch_cars(first_data_1, second_data_2)
print(Usama_scrapped_data)

df = pd.DataFrame(Usama_scrapped_data)
print(df)
df.to_json("cmpana.json", orient="records", indent=3)