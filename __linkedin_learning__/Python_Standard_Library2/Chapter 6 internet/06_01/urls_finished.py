# Using the URL parsing functions
import urllib.parse

sample_url = "http://server.example.com:8080/example.html?val1=1&val2=Hello+World"

# parse a URL with urlparse()
result = urllib.parse.urlparse(sample_url)
print(result)
print(result.scheme, result.hostname, result.path)
print(result.geturl())


# quote() replaces special characters for use in URLs
sample_string = "Hello El Niño"
print(urllib.parse.quote(sample_string))
print(urllib.parse.quote_plus(sample_string))


# Use urlencode() to convert maps to parameter strings
query_data = {
    'Name': "John Doe",
    "City": "Anytown USA",
    "Age": 37
}
result = urllib.parse.urlencode(query_data)
print(result)
