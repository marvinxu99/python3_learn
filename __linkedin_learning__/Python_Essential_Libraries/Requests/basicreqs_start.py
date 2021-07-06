# Python Essential Libraries by Joe Marini course example
# Example file for Requests library
import requests

# TODO: create a basic request for data
# resp = requests.get("http://httpbin.org/xml")
# print(resp.status_code)
# print(resp.text)

# TODO: create a request using parameters
args = {"key1": 1, "key2": 'two', 'key3': False}
resp = requests.get("http://httpbin.org/get", params=args)
print(resp.status_code)
print(resp.text)


# TODO: create a request using POST


# TODO: create a request using custom headers
