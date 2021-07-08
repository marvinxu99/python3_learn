# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests

# TODO: work with status codes
# resp = requests.get("http://httpbin.org/status/404")
resp = requests.get("http://httpbin.org/status/200")
print(resp.status_code)
resp.raise_for_status()    # will raise for 404 

# TODO: examine response encoding
# resp = requests.get("http://httpbin.org/html")
# print(resp.encoding)
# print(resp.text)
# print(resp.content)    # Binary

# TODO: To read JSON content, use the json() function
resp = requests.get('http://httpbin.org/json')
print(resp.json())
print(resp.headers)
print(resp.headers['Content-Type'])