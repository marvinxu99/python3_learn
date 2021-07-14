# working with JSON data
import urllib.request
import json


# TODO: use urllib to retrieve some sample JSON data
sample_url = "http://httpbin.org/json"
resp = urllib.request.urlopen(sample_url)
data = resp.read().decode('utf-8')

# TODO: use the JSON module to parse the returned data
json_data = json.loads(data)
print(json_data)

# TODO: when the data is parsed, we can access it like any other object
print(json_data['slideshow']['title'])
print(json_data['slideshow']['author'])
for slide in json_data['slideshow']['slides']:
    print(slide['title'])


# TODO: python objects can also be written out as JSON
objdata = {
    "name": "Joe Marini",
    "author": True,
    "titles": [
        "Learning Python", "Advanced Python", "Python Standard Library Essential Training"
    ]
}

json_data = json.dumps(objdata, indent=4)
print(json_data)

with open("json_output.json", 'w') as f:
    json.dump(objdata, f, indent=4)