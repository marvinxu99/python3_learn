# retrieve data from the internet
import urllib.request


sample_url = "http://httpbin.org/xml"

# Create a request to retrieve data using urllib.request
resp = urllib.request.urlopen(sample_url, timeout=5)

# Check the status
status_code = resp.status
print(status_code)

# if no error, then read the response contents
if status_code >= 200 and status_code < 300:
    # work with response headers
    print(resp.getheaders())
    print(resp.getheader('Content-length'))
    print(resp.headers['Content-Type'])

    # read the data from the URL
    data = resp.read().decode('utf-8')
    print(data)
