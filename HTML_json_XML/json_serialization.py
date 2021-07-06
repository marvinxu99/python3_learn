'''
Parsing functions:
- obj = load(file)
- obj = load(string)

Serialization functions:
- dump(obj, file)
- str = dumps(obj)
'''
import json

def main():
    # define a string of JSON code
    pythonData = {
        "sandwich": "Reuben",
        "toasted": True,
        "toppings": [
            "Thousand Island Dressing",
            "Sauerkraut",
            "Pickles"
        ],
        "price": 8.99
    }

    # Serialize to JSON using dumps
    jsonStr = json.dumps(pythonData, indent=4)

    # print out the JSON string
    print(jsonStr)

if __name__ == "__main__":
    main()


