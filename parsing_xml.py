"""
Learning project focused on working with XML data in Python.

In this script, I fetch XML data from an external URL, parse it, and convert it into structured
Python dictionaries. The project includes:
- HTTP requests handling
- XML parsing and safe data extraction
- Data transformation and cleanup
- Filtering and sorting operations
- Clean, modular code organization

This project is intended as a practical exercise to understand real-world data processing workflows.
"""
import xml.etree.ElementTree as ET
import requests

url="https://www.w3schools.com/xml/simple.xml"
def fetch(url):
    response = requests.get(url)
    response.raise_for_status()
    xml_data=response.text
    root=ET.fromstring(response.text)
    def get_text(parent,tag,default=None):
        element=parent.find(tag)
        return element.text if element is not None else default
    foods=[]
    for food_element in root.findall('food'):
        food_dict = {'name': get_text(food_element, 'name', 'Unknown'),
                     'price': float(get_text(food_element, 'price', '0').replace('$', '')),
                     'calories': int(get_text(food_element, 'calories', '0')),
                     'description': get_text(food_element, 'description', '')
                     }
        foods.append(food_dict)
    return foods
if __name__=='__main__':
    foods=fetch(url)
    print('Filter foods that contain the word "Salad" in the name.there is none')

    Salad_low_calorie_foods = [food for food in foods if (food['calories'] < 800 and 'Salad' in food['name'])]
    for food in Salad_low_calorie_foods:
        print(f'Salad food:,{food['name']} - {food['calories']} calories')

    print('Filter foods that contain the word "Waffles" in the name.')
    waffle_foods = [food for food in foods if food['calories'] < 800 and "Waffles" in food['name']]
    for food in waffle_foods:
        print(f"Waffle food: {food['name']} - {food['calories']} calories")

    print("Foods sorted by price (descending):")
    foods_sorted = sorted(foods, key=lambda f: f['price'], reverse=True)
    for food in foods_sorted:
        print(f'{food['name']} - ${food['price']}')

    print("Low calories foods sorted by price (descending):")
    filtered_low_calories_food = sorted(foods, key=lambda food: food['price'], reverse=True)
    for food in filtered_low_calories_food:
        print(f'{food["name"]} - {food['calories']} cal - ${food['price']}')


