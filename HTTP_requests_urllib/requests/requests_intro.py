# https://docs.python-requests.org/en/master/

'''
simple API - each HTTP verb is a method name
Makes working with parameters, headers, and cookies easier
Automatically decodes returned content
automatically parses JSON content when detected.
Handles redirects, timeouts, and errors

'''

import requests

url = "http://httpbin.org/html"
response = requests.get(url)
print(f"response status: { response.status_code }")
if (response.status_code == 200):
    print(response.text)