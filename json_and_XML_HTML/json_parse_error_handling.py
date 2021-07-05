'''
Parsing functions:
- obj = load(file)
- obj = load(string)

Serialization functions:
- dump(obj, file)
- str = dumps(obj)
'''
import json
from json import JSONDecodeError

def main():
    # define a string of JSON code
    jsonStr = ''' {
        "sandwich": "Reuben",
        "toasted": true,
        "toppings": [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ]
        "price": 8.99
    }'''

    # Parsing the JSON data using loads
    try:
        data = json.loads(jsonStr)
    except JSONDecodeError as err:
        print('Whoops, JSON decoding error:')
        print(err.msg)
        print(err.lineno, err.colno)

    # print information from the data structure
    print("Sandwich: " + data['sandwich'])
    if (data['toasted']):
        print('And it is toasted')
    for topping in data['toppings']:
        print('Topping: ' + topping)

if __name__ == "__main__":
    main()
