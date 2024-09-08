from flask import Flask, jsonify, request
import json

with open('data.json', 'r') as file:
    todo_list = json.load(file)

with open('Json_data_file.json', 'r') as file:
    todo_list2 = json.load(file)

with open('cmpana.json', 'r') as file:
    todo_list3 = json.load(file)


app = Flask(__name__)

@app.route('/')
def main():
    return "this is todo list"

@app.route('/pakwheels')
def all():
    return jsonify(todo_list)

@app.route('/pkmotors')
def all2():
    return jsonify(todo_list2)

@app.route('/scrapper/api/v1/pkmotors/scrap/<string:city>/<string:make>/<string:model>/<string:year>')
def Scraper2(city, make, model, year):
    result = [] 
   
    for items in todo_list2:
        if items['city'].lower() == city.lower() and items['make'].lower() == make.lower() and items['model'].lower() == model.lower() and items['year'].lower() == year.lower() : # Case-insensitive comparison
            result.append(items) 
   
    if result:
        return jsonify(result)  # Return all matching entries as a JSON response
    else:
        return jsonify({"message": f"Items: {city} {make} {model} {year}  not found"})

@app.route('/scrapper/api/v1/pakwheels/scrap/<string:city>/<string:make>/<string:model>/<string:year>')
def Scraper(city, make, model, year):
    result = [] 
   
    for items in todo_list:
        if items['city'].lower() == city.lower() and items['make'].lower() == make.lower() and items['model'].lower() == model.lower() and items['year'].lower() == year.lower() : # Case-insensitive comparison
            result.append(items) 
   
    if result:
        return jsonify(result)  # Return all matching entries as a JSON response
    else:
        return jsonify({"message": f"Items: {city} {make} {model} {year}  not found"})
    

@app.route('/scrapper/api/v1/competitor_analysis/scrap/<string:city>/<string:make>/<string:model>/<string:year>')
def Scraper3(city, make, model, year):
    result = [] 
   
    for items in todo_list3:
        if items['city'].lower() == city.lower() and items['make'].lower() == make.lower() and items['model'].lower() == model.lower() and items['year'].lower() == year.lower() : # Case-insensitive comparison
            result.append(items) 
   
    if result:
        return jsonify(result)  # Return all matching entries as a JSON response
    else:
        return jsonify({"message": f"Items: {city} {make} {model} {year}  not found"})
    


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )