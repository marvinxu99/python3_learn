# Using the URL parsing functions
import urllib.parse

sample_url = "http://server.example.com:8080/example.html?val1=1&val2=Hello+World"

# TODO: parse a URL with urlparse()
result = urllib.parse.urlparse(sample_url)
print(result)
print('scheme=', result.scheme)
print('hostname=', result.hostname)
print('path=', result.path)
print(result.geturl())

# TODO: quote() replaces special characters for use in URLs
sample_string = "Hello El Niño"
print(urllib.parse.quote(sample_string))
print(urllib.parse.quote_plus(sample_string))

# TODO: Use urlencode() to convert maps to parameter values
query_data = {
    'Name': "John Doe",
    "City": "Anytown USA",
    "Age": 30
}
result = print(urllib.parse.urlencode(query_data))
print(result)