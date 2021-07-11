# working with JSON data
import urllib.request
import json


# use urllib to retrieve some sample JSON data
req = urllib.request.urlopen("http://httpbin.org/json")
data = req.read().decode('utf-8')
print(data)

# use the JSON module to parse the returned data
obj = json.loads(data)

# when the data is parsed, we can access it like any other object
print(obj["slideshow"]["author"])
for slide in obj["slideshow"]["slides"]:
    print(slide["title"])

# python objects can also be written out as JSON
objdata = {
    "name": "Joe Marini",
    "author": True,
    "titles": [
        "Learning Python", "Advanced Python", "Python Standard Library Essential Training"
    ]
}

with open("jsonoutput.json", "w") as fp:
    json.dump(objdata, fp, indent=4)
